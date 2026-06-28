import random
import time
import sys
import os
from typing import Dict, Optional, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.engine import SimulationEngine
from app.map_generator import MapGenerator
from app.database import init_db, register_default_agents, save_match_results, get_db_connection
from app.metrics_tracker import MetricsTracker

# Find project root and add to sys.path
current_dir = os.path.abspath(__file__)
project_root = None
for _ in range(10):
    if os.path.isdir(os.path.join(current_dir, 'agents')):
        project_root = current_dir
        break
    parent = os.path.dirname(current_dir)
    if parent == current_dir:
        break
    current_dir = parent
if project_root and project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import all agents
from agents.minimax_agent import MinimaxAgent
from agents.expectimax_agent import ExpectimaxAgent
from agents.random_agent import RandomAgent
from agents.bfs_agent import BFSAgent
from agents.dfs_agent import DFSAgent
from agents.astar_agent import AStarAgent
from agents.greedy_agent import GreedyAgent
from agents.hill_climbing_agent import HillClimbingAgent
from agents.simulated_annealing_agent import SimulatedAnnealingAgent
from agents.and_or_search_agent import AndOrSearchAgent
from agents.online_search_agent import OnlineSearchAgent
from agents.backtracking_agent import BacktrackingAgent
from agents.min_conflicts_agent import MinConflictsAgent

# Agent registry: name -> factory function
AGENT_REGISTRY = {
    "minimax":             lambda: MinimaxAgent(depth=2),
    "expectimax":         lambda: ExpectimaxAgent(depth=2),
    "random":             lambda: RandomAgent(),
    "bfs":                lambda: BFSAgent(),
    "dfs":                lambda: DFSAgent(depth_limit=5),
    "astar":              lambda: AStarAgent(),
    "greedy":             lambda: GreedyAgent(),
    "hill_climbing":      lambda: HillClimbingAgent(),
    "simulated_annealing": lambda: SimulatedAnnealingAgent(),
    "and_or_search":      lambda: AndOrSearchAgent(depth=2),
    "online_search":      lambda: OnlineSearchAgent(),
    "backtracking":       lambda: BacktrackingAgent(max_depth=6),
    "min_conflicts":      lambda: MinConflictsAgent(),
}

AGENT_DISPLAY_NAMES = {
    "minimax":             "Minimax",
    "expectimax":         "Expectimax",
    "random":             "Random",
    "bfs":                "BFS",
    "dfs":                "DFS",
    "astar":              "A*",
    "greedy":             "Greedy",
    "hill_climbing":      "Hill Climbing",
    "simulated_annealing": "Simulated Annealing",
    "and_or_search":      "AND-OR Search",
    "online_search":      "Online Search (LRTA*)",
    "backtracking":       "Backtracking",
    "min_conflicts":      "Min-Conflicts",
}

app = FastAPI(title="Bomberman AI Platform Demo API", version="1.0.0")

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global in-memory game engine and tracker
global_engine: Optional[SimulationEngine] = None
global_tracker: Optional[MetricsTracker] = None

class StepRequest(BaseModel):
    actions: Dict[str, int]

class InitRequest(BaseModel):
    # Map agent_id -> algorithm name (e.g. "player_2" -> "bfs")
    # player_1 is always human-controlled; other players default to "minimax"
    agent_configs: Optional[Dict[str, str]] = None

@app.on_event("startup")
def startup_event():
    # Automatically initialize SQLite database and insert default agent profiles on start
    init_db()
    register_default_agents()

@app.get("/")
def read_root():
    return {"message": "Bomberman AI Simulation Server is running"}

@app.get("/api/agents")
def list_agents():
    """Return list of available agent algorithms."""
    return {
        "agents": [
            {"id": k, "name": v}
            for k, v in AGENT_DISPLAY_NAMES.items()
        ]
    }

# Store per-game agent configs
global_agent_configs: Dict[str, str] = {}
# Store stateful agents (e.g. OnlineSearchAgent has internal state)
global_agent_instances: Dict[str, Any] = {}

@app.post("/api/init")
def init_game(req: Optional[InitRequest] = None):
    global global_engine, global_tracker, global_agent_configs, global_agent_instances
    try:
        # Parse agent configs from request
        configs = {}
        if req and req.agent_configs:
            configs = req.agent_configs

        # Default configs for all players (no manual player)
        default_bot_agent = "minimax"
        global_agent_configs = {
            "player_1": configs.get("player_1", default_bot_agent),
            "player_2": configs.get("player_2", default_bot_agent),
            "player_3": configs.get("player_3", default_bot_agent),
            "player_4": configs.get("player_4", default_bot_agent),
        }

        # Instantiate stateful agents fresh for new game
        global_agent_instances = {}
        for pid, algo in global_agent_configs.items():
            if algo in AGENT_REGISTRY:
                global_agent_instances[pid] = AGENT_REGISTRY[algo]()
            else:
                global_agent_instances[pid] = AGENT_REGISTRY["minimax"]()

        # Initialize metrics tracker
        global_tracker = MetricsTracker(agent_ids=["player_1", "player_2", "player_3", "player_4"])
        
        # Initialize simulation engine with default layout (deterministic seeded grid)
        global_engine = SimulationEngine(tracker=global_tracker)
        
        # Add 4 agents in the four corners
        # player_1 is the keyboard-controlled user agent
        global_engine.add_agent("player_1", 1, 1, lives=1)
        global_engine.add_agent("player_2", 13, 1, lives=1)
        global_engine.add_agent("player_3", 1, 11, lives=1)
        global_engine.add_agent("player_4", 13, 11, lives=1)
        
        return {
            "status": "initialized",
            "state": global_engine.get_state(),
            "agent_configs": global_agent_configs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/step")
def step_game(req: StepRequest):
    global global_engine, global_tracker
    if global_engine is None:
        raise HTTPException(status_code=400, detail="Game not initialized. Call /api/init first.")
        
    t_start = time.perf_counter()
    try:
        actions = req.actions
        
        # Provide AI for other players if not specified, using selected agent algorithm
        for agent_id, agent in global_engine.state.agents.items():
            if agent.is_alive:
                if agent_id not in actions:
                    t_bot_start = time.perf_counter()
                    
                    # Convert engine state to agent state dict
                    walls = []
                    bricks = []
                    items = {}
                    for y in range(global_engine.state.height):
                        for x in range(global_engine.state.width):
                            tile = global_engine.state.grid[y][x]
                            if tile == 1:  # WALL
                                walls.append((x, y))
                            elif tile == 2:  # BRICK
                                bricks.append((x, y))
                            elif tile == 5:  # ITEM_RADIUS
                                items[(x, y)] = 1
                            elif tile == 6:  # ITEM_CAPACITY
                                items[(x, y)] = 2
                                
                    enemy_positions = [
                        (a.x, a.y) for aid, a in global_engine.state.agents.items()
                        if aid != agent_id and a.is_alive
                    ]
                    
                    # Map engine bomb timer to agent timer and include range
                    bomb_positions = [
                        (b.x, b.y, max(1, b.timer - 3), b.range) for b in global_engine.state.bombs
                    ]
                    
                    explosions = list(global_engine.state.explosions)
                    
                    state_for_agent = {
                        "self_position": (agent.x, agent.y),
                        "enemy_positions": enemy_positions,
                        "bomb_positions": bomb_positions,
                        "explosions": explosions,
                        "walls": walls,
                        "bricks": bricks,
                        "items": items,
                        "ammo": agent.bombs_left,
                        "blast_radius": agent.bomb_range,
                        "width": global_engine.state.width,
                        "height": global_engine.state.height
                    }
                    
                    # Use the selected agent instance (stateful agents reuse same instance)
                    bot_agent = global_agent_instances.get(agent_id)
                    if bot_agent is None:
                        bot_agent = MinimaxAgent(depth=2)
                    action_str = bot_agent.choose_action(state_for_agent)
                    
                    action_map = {
                        "WAIT": 0, "STOP": 0,
                        "LEFT": 1, "RIGHT": 2, "UP": 3, "DOWN": 4,
                        "BOMB": 5
                    }
                    actions[agent_id] = action_map.get(action_str, 0)
                        
                    t_bot_end = time.perf_counter()
                    bot_latency = (t_bot_end - t_bot_start) * 1000.0
                    if global_tracker:
                        global_tracker.record_step_latency(agent_id, bot_latency)
                        
        # Record latency for user action handling
        t_user_end = time.perf_counter()
        user_latency = (t_user_end - t_start) * 1000.0
        if global_tracker:
            global_tracker.record_step_latency("player_1", user_latency)
            
        # Step the engine
        game_continue = global_engine.step(actions)
        
        # If match is over, save statistics to the SQLite database
        if not game_continue and global_tracker:
            alive_agents = [aid for aid, a in global_engine.state.agents.items() if a.is_alive]
            winner_id = alive_agents[0] if len(alive_agents) == 1 else None
            
            # Compile stats
            stats = global_tracker.get_final_stats(global_engine.state.step_count, alive_agents)
            
            # Save transactionally to DB
            save_match_results(global_tracker.match_id, global_engine.state.step_count, winner_id, stats)
            print(f"Match {global_tracker.match_id} completed. Stats saved to database.")
            
        return {
            "status": "running" if game_continue else "game_over",
            "game_continue": game_continue,
            "state": global_engine.get_state()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/benchmark/db-stats")
def get_db_stats():
    """
    Exposes metrics retrieved directly from the SQLite database.
    """
    conn = get_db_connection()
    try:
        # Get total matches
        total_matches = conn.execute("SELECT COUNT(*) FROM matches").fetchone()[0]
        
        # Get average steps per match
        avg_steps = conn.execute("SELECT AVG(steps) FROM matches").fetchone()[0] or 0.0
        
        # Get leaderboard rankings (aggregated statistics)
        leaderboard = []
        cursor = conn.execute("""
            SELECT 
                a.id, 
                a.name, 
                a.algorithm,
                COUNT(ams.match_id) as matches_played,
                SUM(CASE WHEN ams.rank = 1 THEN 1 ELSE 0 END) as wins,
                AVG(ams.survival_steps) as avg_survival_steps,
                SUM(ams.kills) as total_kills,
                SUM(ams.suicides) as total_suicides,
                AVG(ams.avg_latency_ms) as avg_latency_ms
            FROM agents a
            LEFT JOIN agent_match_stats ams ON a.id = ams.agent_id
            GROUP BY a.id
            ORDER BY wins DESC, avg_survival_steps DESC
        """)
        
        for row in cursor.fetchall():
            matches_played = row["matches_played"] or 0
            wins = row["wins"] or 0
            leaderboard.append({
                "agent_id": row["id"],
                "name": row["name"],
                "algorithm": row["algorithm"],
                "matches_played": matches_played,
                "wins": wins,
                "win_rate": round((wins / matches_played * 100.0), 2) if matches_played > 0 else 0.0,
                "avg_survival_steps": round(row["avg_survival_steps"], 1) if row["avg_survival_steps"] is not None else 0.0,
                "total_kills": row["total_kills"] or 0,
                "total_suicides": row["total_suicides"] or 0,
                "avg_latency_ms": round(row["avg_latency_ms"], 2) if row["avg_latency_ms"] is not None else 0.0
            })
            
        return {
            "total_matches": total_matches,
            "avg_steps": round(avg_steps, 1),
            "leaderboard": leaderboard
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

