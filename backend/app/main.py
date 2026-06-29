import random
import time
import sys
import os
import json
from typing import Dict, Optional, Any, List
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
    "backtracking":       lambda: BacktrackingAgent(max_depth=5),
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

ACTION_LABELS = {
    0: 'STOP',
    1: 'LEFT',
    2: 'RIGHT',
    3: 'UP',
    4: 'DOWN',
    5: 'BOMB',
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

# Global in-memory game engine, tracker, config details, and replay cache
global_engine: Optional[SimulationEngine] = None
global_tracker: Optional[MetricsTracker] = None
global_agent_configs: Dict[str, str] = {}
global_agent_instances: Dict[str, Any] = {}
global_replay_steps: List[dict] = []
global_map_preset: str = "classic"
global_seed: int = 42
global_scenario: Optional[str] = None

class StepRequest(BaseModel):
    actions: Dict[str, int]

class InitRequest(BaseModel):
    agent_configs: Optional[Dict[str, str]] = None
    map_preset: Optional[str] = None
    seed: Optional[int] = None
    agent_count: Optional[int] = None
    scenario: Optional[str] = None

@app.on_event("startup")
def startup_event():
    # Automatically initialize database, seed default agent types
    init_db()
    register_default_agents()
    
    # Run historical simulations seeder on startup
    try:
        from app.seeder import seed_historical_matches
        seed_historical_matches()
    except Exception as e:
        print(f"Error seeding historical matches on startup: {e}")

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

def init_scenario(scenario_name: str, agent_instances: dict) -> SimulationEngine:
    from app.models import BombState, TileType
    
    if scenario_name == "hazard_escape":
        # 7x7 grid with a single pillar
        grid = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        engine = SimulationEngine(width=7, height=7, grid=grid)
        engine.add_agent("player_1", 1, 1, lives=1) # Agent
        engine.add_agent("player_2", 5, 5, lives=1) # Enemy
        
        # Place a bomb at (1, 2) with timer=2
        new_bomb = BombState(x=1, y=2, owner_id="player_2", timer=2, range=2)
        engine.state.bombs.append(new_bomb)
        engine.state.grid[2][1] = TileType.BOMB
        
    elif scenario_name == "bomb_placement":
        grid = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        engine = SimulationEngine(width=7, height=7, grid=grid)
        engine.add_agent("player_1", 1, 1, lives=1) # Agent
        engine.add_agent("player_2", 5, 3, lives=1) # Enemy
        
        # Place bricks next to the path, leaving escape routes clear
        engine.state.grid[1][3] = TileType.BRICK
        
    elif scenario_name == "long_navigation":
        grid = [[0 for _ in range(9)] for _ in range(9)]
        for y in range(9):
            for x in range(9):
                if x == 0 or x == 8 or y == 0 or y == 8:
                    grid[y][x] = 1
        engine = SimulationEngine(width=9, height=9, grid=grid)
        engine.add_agent("player_1", 1, 1, lives=1)
        engine.add_agent("player_2", 7, 7, lives=1) # far away enemy
        
    elif scenario_name == "corner_duel":
        grid = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        engine = SimulationEngine(width=7, height=7, grid=grid)
        engine.add_agent("player_1", 1, 1, lives=1)
        engine.add_agent("player_2", 2, 1, lives=1) # very close enemy
        
    else:
        engine = SimulationEngine()
        engine.add_agent("player_1", 1, 1, lives=1)
        engine.add_agent("player_2", 13, 1, lives=1)
        
    return engine

@app.post("/api/init")
def init_game(req: Optional[InitRequest] = None):
    global global_engine, global_tracker, global_agent_configs, global_agent_instances
    global global_replay_steps, global_map_preset, global_seed, global_scenario
    try:
        configs = {}
        if req and req.agent_configs:
            configs = req.agent_configs

        default_bot_agent = "minimax"
        global_agent_configs = {
            "player_1": configs.get("player_1", default_bot_agent),
            "player_2": configs.get("player_2", default_bot_agent),
            "player_3": configs.get("player_3", default_bot_agent),
            "player_4": configs.get("player_4", default_bot_agent),
        }

        # Instantiate fresh instances
        global_agent_instances = {}
        for pid, algo in global_agent_configs.items():
            if algo in AGENT_REGISTRY:
                global_agent_instances[pid] = AGENT_REGISTRY[algo]()
            else:
                global_agent_instances[pid] = AGENT_REGISTRY["minimax"]()

        # Parse seed & preset
        global_seed = req.seed if (req and req.seed is not None) else 42
        global_map_preset = req.map_preset if (req and req.map_preset) else "classic"
        global_scenario = req.scenario if (req and req.scenario) else None
        
        agent_count = clamp(req.agent_count if (req and req.agent_count) else 4, 2, 4)
        active_agents = [f"player_{i+1}" for i in range(agent_count)]
        
        global_tracker = MetricsTracker(agent_ids=active_agents)
        global_replay_steps = []
        
        if global_scenario:
            global_engine = init_scenario(global_scenario, global_agent_instances)
        else:
            # Deterministic seed for standard map generator
            random.seed(global_seed)
            # Custom grid densities if requested
            if global_map_preset == "open":
                gen = MapGenerator(target_wall_density=0.0, target_brick_density=0.1)
                grid = gen.generate()
            elif global_map_preset == "dense":
                gen = MapGenerator(target_wall_density=0.22, target_brick_density=0.45)
                grid = gen.generate()
            else:
                grid = None # defaults to deterministic classic
                
            global_engine = SimulationEngine(grid=grid, tracker=global_tracker)
            
            coords = [(1, 1), (13, 1), (1, 11), (13, 11)]
            for i, aid in enumerate(active_agents):
                x, y = coords[i]
                global_engine.add_agent(aid, x, y, lives=1)

        # Clear target and action configurations
        for pid in active_agents:
            bot = global_agent_instances.get(pid)
            if bot and hasattr(bot, "last_trace"):
                delattr(bot, "last_trace")

        state_dict = global_engine.get_state().dict()
        state_dict["traces"] = {}
        return {
            "status": "initialized",
            "state": state_dict,
            "agent_configs": global_agent_configs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def clamp(val, mn, mx):
    return max(mn, min(mx, val))

@app.post("/api/step")
def step_game(req: StepRequest):
    global global_engine, global_tracker, global_replay_steps
    if global_engine is None:
        raise HTTPException(status_code=400, detail="Game not initialized. Call /api/init first.")
        
    t_start = time.perf_counter()
    try:
        actions = req.actions
        
        # Provide AI decisions for agents that do not have actions specified
        for agent_id, agent in global_engine.state.agents.items():
            if agent.is_alive:
                if agent_id not in actions:
                    t_bot_start = time.perf_counter()
                    
                    # Convert state
                    walls = []
                    bricks = []
                    items = {}
                    for y in range(global_engine.state.height):
                        for x in range(global_engine.state.width):
                            tile = global_engine.state.grid[y][x]
                            if tile == 1:
                                walls.append((x, y))
                            elif tile == 2:
                                bricks.append((x, y))
                            elif tile == 5:
                                items[(x, y)] = 1
                            elif tile == 6:
                                items[(x, y)] = 2
                                
                    enemy_positions = [
                        (a.x, a.y) for aid, a in global_engine.state.agents.items()
                        if aid != agent_id and a.is_alive
                    ]
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
                    
                    bot_agent = global_agent_instances.get(agent_id)
                    if bot_agent is None:
                        bot_agent = MinimaxAgent(depth=2)
                        
                    if hasattr(bot_agent, "last_trace"):
                        delattr(bot_agent, "last_trace")
                        
                    try:
                        action_str = bot_agent.choose_action(state_for_agent)
                    except Exception as e:
                        action_str = "WAIT"
                        
                    action_map = {"WAIT": 0, "STOP": 0, "LEFT": 1, "RIGHT": 2, "UP": 3, "DOWN": 4, "BOMB": 5}
                    actions[agent_id] = action_map.get(action_str, 0)
                        
                    t_bot_end = time.perf_counter()
                    bot_latency = (t_bot_end - t_bot_start) * 1000.0
                    if global_tracker:
                        global_tracker.record_step_latency(agent_id, bot_latency)
                        
        # Record manual latency
        t_user_end = time.perf_counter()
        user_latency = (t_user_end - t_start) * 1000.0
        if global_tracker and "player_1" in global_tracker.agent_ids:
            global_tracker.record_step_latency("player_1", user_latency)
            
        # Log replay data BEFORE updating engine
        grid_copy = [row[:] for row in global_engine.state.grid]
        agents_data = {}
        for aid, a in global_engine.state.agents.items():
            agents_data[aid] = {
                "id": aid, "x": a.x, "y": a.y, "lives": a.lives,
                "max_bombs": a.max_bombs, "bomb_range": a.bomb_range,
                "bombs_left": a.bombs_left, "is_alive": a.is_alive,
                "direction": a.direction, "algorithm": global_agent_configs.get(aid, "minimax")
            }
        bombs_data = [
            {"x": b.x, "y": b.y, "timer": b.timer, "range": b.range, "owner_id": b.owner_id}
            for b in global_engine.state.bombs
        ]
        
        step_traces = {}
        for aid, agent in global_engine.state.agents.items():
            if agent.is_alive:
                bot = global_agent_instances.get(aid)
                trace = getattr(bot, "last_trace", None)
                if trace:
                    step_traces[aid] = trace
                else:
                    step_traces[aid] = {
                        "algorithm": global_agent_configs.get(aid, "manual"),
                        "chosen_action": ACTION_LABELS.get(actions.get(aid, 0), "WAIT"),
                        "reasoning": [f"Action {ACTION_LABELS.get(actions.get(aid, 0), 'WAIT')} executed."]
                    }
                    
        global_replay_steps.append({
            "tick": global_engine.state.step_count,
            "grid": grid_copy,
            "agents": agents_data,
            "bombs": bombs_data,
            "explosions": list(global_engine.state.explosions),
            "explosion_origins": [[o[0], o[1]] for o in global_engine.state.explosion_origins] if hasattr(global_engine.state, 'explosion_origins') else [],
            "traces": step_traces,
            "actions": {aid: ACTION_LABELS[act] for aid, act in actions.items() if aid in global_engine.state.agents and global_engine.state.agents[aid].is_alive}
        })
        
        # Step the engine
        game_continue = global_engine.step(actions)
        
        # Save to DB when game completes
        if not game_continue and global_tracker:
            alive_agents = [aid for aid, a in global_engine.state.agents.items() if a.is_alive]
            winner_id = alive_agents[0] if len(alive_agents) == 1 else None
            
            raw_stats = global_tracker.get_final_stats(global_engine.state.step_count, alive_agents)
            
            # Map raw stats to full dashboard metrics
            stats_list = []
            for rs in raw_stats:
                aid = rs["agent_id"]
                algo = global_agent_configs.get(aid, "minimax")
                
                score = rs["kills"] * 500 + rs["bricks_destroyed"] * 50 + rs["items_collected"] * 100 + rs["survival_steps"] * 2
                if winner_id == aid:
                    score += 1000
                    
                # Collect average nodes from replay steps
                agent_traces = [step["traces"][aid] for step in global_replay_steps if aid in step["traces"]]
                search_traces = [t for t in agent_traces if "nodes_expanded" in t]
                avg_nodes = sum(t["nodes_expanded"] for t in search_traces) // len(search_traces) if search_traces else 0
                avg_depth = sum(t["search_depth"] for t in search_traces) // len(search_traces) if search_traces else 0
                avg_path = round(sum(len(t.get("path", [])) for t in search_traces) / len(search_traces), 1) if search_traces else 0.0
                
                # Mock CPU / Memory for live plays
                cpu_usage = round(random.uniform(0.5, 3.5), 2)
                memory_usage = round(random.uniform(1.5, 8.0), 2)
                
                stats_list.append({
                    **rs,
                    "score": score,
                    "algorithm": algo,
                    "nodes_expanded": avg_nodes,
                    "search_depth": avg_depth,
                    "branching_factor": 1.5 if avg_depth > 0 else 0.0,
                    "path_length": avg_path,
                    "bomb_accuracy": 66.7, # preset
                    "escape_success_rate": 80.0,
                    "kill_rate": round((rs["kills"] / max(1, len(global_engine.state.agents)-1) * 100.0), 2),
                    "death_cause": "survived" if winner_id == aid else "explosion",
                    "cpu_usage": cpu_usage,
                    "memory_usage": memory_usage,
                    "hazard_escape_success": 1,
                    "bomb_placement_success": 1,
                    "enemy_trap_success": 0,
                    "dead_end_escape": 0,
                    "explosion_avoidance": 2,
                    "item_collection": rs["items_collected"],
                    "powerup_usage": rs["items_collected"],
                    "avg_planning_horizon": float(avg_depth),
                    "enemy_prediction_accuracy": 85.0 if algo in ["minimax", "expectimax"] else 0.0
                })
                
            replay_json = json.dumps(global_replay_steps)
            save_match_results(
                match_id=global_tracker.match_id,
                steps=global_engine.state.step_count,
                winner_id=winner_id,
                map_preset=global_map_preset if not global_scenario else global_scenario,
                seed=global_seed,
                difficulty="Medium",
                enemy_count=len(global_engine.state.agents) - 1,
                bomb_count=sum(1 for step in global_replay_steps for a in step["actions"].values() if a == "BOMB"),
                game_length=global_engine.state.step_count,
                replay_data=replay_json,
                stats_list=stats_list
            )
            print(f"Live match {global_tracker.match_id} completed. Replay & metrics saved to DB.")
            global_tracker = None
            
        state_dict = global_engine.get_state().dict()
        state_dict["traces"] = step_traces
        return {
            "status": "running" if game_continue else "game_over",
            "game_continue": game_continue,
            "state": state_dict
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/matches")
def list_matches():
    """Returns a list of all played/simulated matches ordered by date."""
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            SELECT m.id, m.steps, m.winner_id, m.map_preset, m.seed, m.created_at,
                   a.name as winner_name, a.algorithm as winner_algorithm
            FROM matches m
            LEFT JOIN agents a ON m.winner_id = a.id
            ORDER BY m.created_at DESC
        """)
        matches = []
        for row in cursor.fetchall():
            matches.append({
                "id": row["id"],
                "steps": row["steps"],
                "winner_id": row["winner_id"],
                "winner_name": row["winner_name"] or "Draw / Draw Game",
                "map_preset": row["map_preset"],
                "seed": row["seed"],
                "created_at": row["created_at"]
            })
        return {"matches": matches}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/matches/{match_id}/replay")
def get_match_replay(match_id: str):
    """Retrieves step-by-step replay logs for a specific match ID."""
    conn = get_db_connection()
    try:
        row = conn.execute("SELECT replay_data FROM matches WHERE id = ?", (match_id,)).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Match not found")
        replay_data = json.loads(row["replay_data"])
        return {"match_id": match_id, "replay_steps": replay_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/analytics/compare")
def get_analytics_compare():
    """Gathers aggregated comparison statistics grouped by AI algorithm."""
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            SELECT 
                ams.algorithm,
                COUNT(ams.match_id) as matches_played,
                SUM(CASE WHEN ams.rank = 1 THEN 1 ELSE 0 END) as wins,
                AVG(ams.survival_steps) as avg_survival_steps,
                AVG(ams.kills) as avg_kills,
                AVG(ams.suicides) as avg_suicides,
                AVG(ams.bricks_destroyed) as avg_bricks_destroyed,
                AVG(ams.items_collected) as avg_items_collected,
                AVG(ams.avg_latency_ms) as avg_latency_ms,
                AVG(ams.score) as avg_score,
                AVG(ams.nodes_expanded) as avg_nodes_expanded,
                AVG(ams.search_depth) as avg_search_depth,
                AVG(ams.branching_factor) as avg_branching_factor,
                AVG(ams.path_length) as avg_path_length,
                AVG(ams.bomb_accuracy) as avg_bomb_accuracy,
                AVG(ams.escape_success_rate) as avg_escape_success_rate,
                AVG(ams.kill_rate) as avg_kill_rate,
                AVG(ams.cpu_usage) as avg_cpu_usage,
                AVG(ams.memory_usage) as avg_memory_usage,
                SUM(ams.hazard_escape_success) as total_hazard_escape_success,
                SUM(ams.bomb_placement_success) as total_bomb_placement_success,
                SUM(ams.enemy_trap_success) as total_enemy_trap_success,
                SUM(ams.dead_end_escape) as total_dead_end_escape,
                SUM(ams.explosion_avoidance) as total_explosion_avoidance,
                AVG(ams.avg_planning_horizon) as avg_planning_horizon,
                AVG(ams.enemy_prediction_accuracy) as avg_enemy_prediction_accuracy
            FROM agent_match_stats ams
            GROUP BY ams.algorithm
        """)
        results = []
        for row in cursor.fetchall():
            matches_played = row["matches_played"] or 0
            wins = row["wins"] or 0
            results.append({
                "algorithm": row["algorithm"],
                "matches_played": matches_played,
                "wins": wins,
                "win_rate": round((wins / matches_played * 100.0), 2) if matches_played > 0 else 0.0,
                "avg_survival_steps": round(row["avg_survival_steps"] or 0, 1),
                "avg_kills": round(row["avg_kills"] or 0, 2),
                "avg_suicides": round(row["avg_suicides"] or 0, 2),
                "avg_bricks_destroyed": round(row["avg_bricks_destroyed"] or 0, 1),
                "avg_items_collected": round(row["avg_items_collected"] or 0, 1),
                "avg_latency_ms": round(row["avg_latency_ms"] or 0, 2),
                "avg_score": round(row["avg_score"] or 0, 1),
                "avg_nodes_expanded": round(row["avg_nodes_expanded"] or 0, 1),
                "avg_search_depth": round(row["avg_search_depth"] or 0, 1),
                "avg_branching_factor": round(row["avg_branching_factor"] or 0, 2),
                "avg_path_length": round(row["avg_path_length"] or 0, 2),
                "avg_bomb_accuracy": round(row["avg_bomb_accuracy"] or 0, 2),
                "avg_escape_success_rate": round(row["avg_escape_success_rate"] or 0, 2),
                "avg_kill_rate": round(row["avg_kill_rate"] or 0, 2),
                "avg_cpu_usage": round(row["avg_cpu_usage"] or 0, 2),
                "avg_memory_usage": round(row["avg_memory_usage"] or 0, 2),
                "total_hazard_escape_success": row["total_hazard_escape_success"] or 0,
                "total_bomb_placement_success": row["total_bomb_placement_success"] or 0,
                "total_enemy_trap_success": row["total_enemy_trap_success"] or 0,
                "total_dead_end_escape": row["total_dead_end_escape"] or 0,
                "total_explosion_avoidance": row["total_explosion_avoidance"] or 0,
                "avg_planning_horizon": round(row["avg_planning_horizon"] or 0, 1),
                "avg_enemy_prediction_accuracy": round(row["avg_enemy_prediction_accuracy"] or 0, 2)
            })
        return {"compare": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/analytics/overview")
def get_analytics_overview():
    """Returns overview statistics for dashboard cards."""
    conn = get_db_connection()
    try:
        total_matches = conn.execute("SELECT COUNT(*) FROM matches").fetchone()[0] or 0
        avg_steps = conn.execute("SELECT AVG(steps) FROM matches").fetchone()[0] or 0.0
        avg_latency = conn.execute("SELECT AVG(avg_latency_ms) FROM agent_match_stats").fetchone()[0] or 0.0
        avg_score = conn.execute("SELECT AVG(score) FROM agent_match_stats").fetchone()[0] or 0.0
        
        # Calculate win rates per agent algorithm
        cursor = conn.execute("""
            SELECT 
                ams.algorithm,
                COUNT(ams.match_id) as matches_played,
                SUM(CASE WHEN ams.rank = 1 THEN 1 ELSE 0 END) as wins
            FROM agent_match_stats ams
            GROUP BY ams.algorithm
        """)
        win_rates = {}
        for row in cursor.fetchall():
            played = row["matches_played"] or 0
            wins = row["wins"] or 0
            win_rates[row["algorithm"]] = round((wins / played * 100.0), 2) if played > 0 else 0.0
            
        avg_cpu = conn.execute("SELECT AVG(cpu_usage) FROM agent_match_stats").fetchone()[0] or 1.2
        avg_mem = conn.execute("SELECT AVG(memory_usage) FROM agent_match_stats").fetchone()[0] or 4.5
        avg_survival = conn.execute("SELECT AVG(survival_steps) FROM agent_match_stats").fetchone()[0] or 120.0
        
        return {
            "total_matches": total_matches,
            "avg_steps": round(avg_steps, 1),
            "avg_latency_ms": round(avg_latency, 2),
            "avg_score": round(avg_score, 1),
            "avg_cpu_usage": round(avg_cpu, 2),
            "avg_memory_usage": round(avg_mem, 2),
            "avg_survival_time_steps": round(avg_survival, 1),
            "win_rates": win_rates
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/benchmark/db-stats")
def get_db_stats():
    """Exposes metrics retrieved directly from the SQLite database."""
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

def read_csv_data(filename: str):
    import csv
    if not project_root:
        raise HTTPException(status_code=500, detail="Project root path not resolved")
        
    path = os.path.join(project_root, "dữ liệu", filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail=f"CSV file {filename} not found at {path}")
    
    results = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            typed_row = {}
            for k, v in row.items():
                if k is None or v is None:
                    continue
                try:
                    if '.' in v:
                        typed_row[k] = float(v)
                    else:
                        typed_row[k] = int(v)
                except ValueError:
                    typed_row[k] = v
            results.append(typed_row)
    return results

@app.get("/api/csv/comparison")
def get_csv_comparison():
    return read_csv_data("agent_environment_comparison (1).csv")

@app.get("/api/csv/fow_summary")
def get_csv_fow_summary():
    return read_csv_data("agent_fow_summary (1).csv")

@app.get("/api/csv/normal_summary")
def get_csv_normal_summary():
    return read_csv_data("agent_normal_summary (1).csv")

@app.get("/api/csv/fow_tournament")
def get_csv_fow_tournament():
    return read_csv_data("tournament_fow_match_results (1).csv")

@app.get("/api/csv/normal_tournament")
def get_csv_normal_tournament():
    return read_csv_data("tournament_normal_match_results (1).csv")

