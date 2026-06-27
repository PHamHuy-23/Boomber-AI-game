"""
Detailed Match Analyser for Bomberman AI Agents.

Runs a single 4-agent match with selected agents under a specific seed.
Generates a detailed, step-by-step log showing:
- ASCII map visualization of each step
- Action decisions, latencies, and state info for each agent
- Event log: bomb placement, explosions, bricks destroyed, items collected, agent deaths
- Final stats summary table.
"""
import os
import sys
import time
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any

# Configure paths to import from project root and backend
PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_DIR = PROJECT_ROOT / "backend"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))


from app.engine import SimulationEngine
from app.metrics_tracker import MetricsTracker
from app.models import TileType

# Import all agents
from agents.random_agent import RandomAgent
from agents.bfs_agent import BFSAgent
from agents.dfs_agent import DFSAgent
from agents.greedy_agent import GreedyAgent
from agents.astar_agent import AStarAgent
from agents.hill_climbing_agent import HillClimbingAgent
from agents.simulated_annealing_agent import SimulatedAnnealingAgent
from agents.backtracking_agent import BacktrackingAgent
from agents.min_conflicts_agent import MinConflictsAgent
from agents.online_search_agent import OnlineSearchAgent
from agents.and_or_search_agent import AndOrSearchAgent
from agents.minimax_agent import MinimaxAgent
from agents.expectimax_agent import ExpectimaxAgent

AGENT_FACTORIES = {
    "Random": lambda: RandomAgent(seed=42),
    "BFS": lambda: BFSAgent(),
    "DFS": lambda: DFSAgent(),
    "Greedy": lambda: GreedyAgent(),
    "A*": lambda: AStarAgent(),
    "HillClimbing": lambda: HillClimbingAgent(),
    "SimulatedAnnealing": lambda: SimulatedAnnealingAgent(),
    "Backtracking": lambda: BacktrackingAgent(max_depth=2),
    "MinConflicts": lambda: MinConflictsAgent(max_depth=2, max_steps=20),
    "OnlineSearch": lambda: OnlineSearchAgent(),
    "AndOrSearch": lambda: AndOrSearchAgent(depth=2),
    "Minimax": lambda: MinimaxAgent(depth=2),
    "Expectimax": lambda: ExpectimaxAgent(depth=2),
}

def render_board_ascii(grid: List[List[int]], agents: Dict[str, Any], bombs: List[Any]) -> str:
    """Render the board state as an ASCII string."""
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    ascii_grid = [["." for _ in range(width)] for _ in range(height)]

    # 1. Fill walls and bricks
    for y in range(height):
        for x in range(width):
            val = grid[y][x]
            if val == TileType.WALL:
                ascii_grid[y][x] = "#"
            elif val == TileType.BRICK:
                ascii_grid[y][x] = "B"
            elif val == TileType.ITEM_RADIUS:
                ascii_grid[y][x] = "R"
            elif val == TileType.ITEM_CAPACITY:
                ascii_grid[y][x] = "C"
            elif val == TileType.EXPLOSION:
                ascii_grid[y][x] = "*"

    # 2. Fill bombs
    for bomb in bombs:
        ascii_grid[bomb.y][bomb.x] = "O"

    # 3. Fill agents
    # Order agents by key to represent them consistently as 1, 2, 3, 4
    sorted_agent_ids = sorted(agents.keys())
    for idx, aid in enumerate(sorted_agent_ids):
        agent = agents[aid]
        if agent.is_alive:
            # Use 1-indexed number
            ascii_grid[agent.y][agent.x] = str(idx + 1)
        else:
            # Only draw X if there's no alive agent there
            current_char = ascii_grid[agent.y][agent.x]
            if current_char not in [str(i+1) for i in range(len(sorted_agent_ids))]:
                ascii_grid[agent.y][agent.x] = "X"

    # Draw border
    border = "+" + "-" * (width * 2 - 1) + "+"
    lines = [border]
    for row in ascii_grid:
        lines.append("|" + " ".join(row) + "|")
    lines.append(border)
    return "\n".join(lines)

def run_analyzed_match(agent_names: List[str], seed: int, fog_of_war: bool = False) -> str:
    """Run a single 4-agent match and return a detailed markdown log."""
    if len(agent_names) != 4:
        raise ValueError("Exactly 4 agents are required for a match.")

    # Order agents as player_1, player_2, player_3, player_4
    order = [f"player_{i+1}" for i in range(4)]
    agent_mapping = {order[i]: agent_names[i] for i in range(4)}

    # Seed the global random number generator for reproducible map generation
    import random
    random.seed(seed)

    # Generate a reachability-guaranteed map layout using MapGenerator (CSP)
    from app.map_generator import MapGenerator
    map_gen = MapGenerator()
    grid = map_gen.generate()

    # Initialize tracker and simulation engine with generated grid
    tracker = MetricsTracker(agent_ids=order)
    engine = SimulationEngine(grid=grid, tracker=tracker)

    # ThreadPool for enforcing 100ms timeouts on actions
    from concurrent.futures import ThreadPoolExecutor, TimeoutError
    thread_pool = ThreadPoolExecutor(max_workers=4)



    # Spawn points
    spawn_points = [(1, 1), (13, 1), (1, 11), (13, 11)]
    for pid, (x, y) in zip(order, spawn_points):
        engine.add_agent(pid, x, y, lives=1)

    # Initialize bot instances
    bot_instances = {pid: AGENT_FACTORIES[agent_mapping[pid]]() for pid in order}

    # Setup report headers
    report = []
    report.append(f"# Bomberman AI Detailed Match Analysis")
    report.append(f"**Seed:** {seed}")
    report.append(f"**Fog of War:** {'Enabled (Radius: 4)' if fog_of_war else 'Disabled'}")
    report.append(f"**Roster:**")
    for i, pid in enumerate(order):
        report.append(f"- **Agent {i+1} ({pid}):** {agent_mapping[pid]}")
    report.append("\n" + "="*40 + "\n")

    done = False
    step = 0

    while not done:
        step = engine.state.step_count
        step_header = f"## STEP {step}"
        report.append(step_header)
        print(f"Running Step {step}...")

        # 1. Capture state before actions
        prev_agents_state = {pid: engine.state.agents[pid].model_copy() for pid in order}
        prev_bricks = set()
        for y in range(engine.height):
            for x in range(engine.width):
                if engine.state.grid[y][x] == TileType.BRICK:
                    prev_bricks.add((x, y))
        prev_bombs = [b.model_copy() for b in engine.state.bombs]

        # 2. Get decisions from all agents
        actions = {}
        decision_details = []

        # Render board ascii
        board_ascii = render_board_ascii(engine.state.grid, engine.state.agents, engine.state.bombs)
        report.append("### Board State:")
        report.append("```\n" + board_ascii + "\n```")

        agent_metadata = []
        for i, pid in enumerate(order):
            agent = engine.state.agents[pid]
            status = "ALIVE" if agent.is_alive else "DEAD"
            agent_metadata.append(
                f"- **{agent_mapping[pid]} (Agent {i+1}):** {status} | Pos: ({agent.x}, {agent.y}) | Lives: {agent.lives} | Ammo: {agent.bombs_left}/{agent.max_bombs} | Range: {agent.bomb_range}"
            )
        report.append("\n".join(agent_metadata) + "\n")

        report.append("### Actions Decided:")
        for i, pid in enumerate(order):
            agent = engine.state.agents[pid]
            if not agent.is_alive:
                actions[pid] = 0 # STOP
                report.append(f"- **Agent {i+1} ({agent_mapping[pid]}):** dead (forced STOP)")
                continue

            # Build local state dict for agent
            walls = []
            bricks = []
            items = {}
            for y in range(engine.state.height):
                for x in range(engine.state.width):
                    tile = engine.state.grid[y][x]
                    if tile == TileType.WALL:
                        walls.append((x, y))
                    elif tile == TileType.BRICK:
                        bricks.append((x, y))
                    elif tile == TileType.ITEM_RADIUS:
                        items[(x, y)] = 1
                    elif tile == TileType.ITEM_CAPACITY:
                        items[(x, y)] = 2

            enemy_positions = [(a.x, a.y) for aid, a in engine.state.agents.items() if aid != pid and a.is_alive]
            bomb_positions = [(b.x, b.y, max(1, b.timer - 3)) for b in engine.state.bombs]
            explosions = list(engine.state.explosions)

            # Apply Fog of War filtering
            if fog_of_war:
                r = 4
                # Visible if within Chebyshev distance <= r of self OR any alive enemy
                vision_centers = [(agent.x, agent.y)] + enemy_positions
                def is_visible(tx, ty):
                    for cx, cy in vision_centers:
                        if max(abs(tx - cx), abs(ty - cy)) <= r:
                            return True
                    return False

                walls = [w for w in walls if is_visible(w[0], w[1])]
                bricks = [b for b in bricks if is_visible(b[0], b[1])]
                items = {k: v for k, v in items.items() if is_visible(k[0], k[1])}
                bomb_positions = [b for b in bomb_positions if is_visible(b[0], b[1])]
                explosions = [e for e in explosions if is_visible(e[0], e[1])]

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
                "width": engine.state.width,
                "height": engine.state.height,
                "legal_actions": ["WAIT", "LEFT", "RIGHT", "UP", "DOWN", "BOMB"],
            }

            t0 = time.perf_counter()
            future = thread_pool.submit(bot_instances[pid].choose_action, state_for_agent)
            try:
                action_str = future.result(timeout=0.100) # 100ms timeout limit
                t1 = time.perf_counter()
                latency = (t1 - t0) * 1000.0
                report.append(f"- **Agent {i+1} ({agent_mapping[pid]}):** chose `{action_str}` (took {latency:.2f} ms)")
            except TimeoutError:
                action_str = "WAIT"
                latency = 100.0
                report.append(f"- **Agent {i+1} ({agent_mapping[pid]}):** TIMEOUT (>100ms) - forced WAIT")

            tracker.record_step_latency(pid, latency)

            action_map = {"WAIT": 0, "STOP": 0, "LEFT": 1, "RIGHT": 2, "UP": 3, "DOWN": 4, "BOMB": 5}
            actions[pid] = action_map.get(action_str, 0)

        # 3. Step the engine
        game_continues = engine.step(actions)
        done = not game_continues

        # 4. Capture state after actions to log events
        post_agents_state = engine.state.agents
        post_bricks = set()
        for y in range(engine.height):
            for x in range(engine.width):
                if engine.state.grid[y][x] == TileType.BRICK:
                    post_bricks.add((x, y))
        post_bombs = engine.state.bombs

        report.append("\n### Events during this step:")
        events = []

        # Bomb placements
        for pid in order:
            if prev_agents_state[pid].is_alive and actions[pid] == 5:
                # Check if bomb list has a new bomb at this position
                has_bomb = any(b.x == prev_agents_state[pid].x and b.y == prev_agents_state[pid].y for b in post_bombs)
                if has_bomb:
                    events.append(f"- 💣 **{agent_mapping[pid]}** placed a bomb at ({prev_agents_state[pid].x}, {prev_agents_state[pid].y})")

        # Bomb explosions
        exploded_coords = engine.state.explosions
        if exploded_coords:
            # Find which bombs exploded
            exploded_bombs = [b for b in prev_bombs if (b.x, b.y) in exploded_coords]
            for eb in exploded_bombs:
                events.append(f"- 💥 Bomb owned by **{agent_mapping[eb.owner_id]}** exploded at ({eb.x}, {eb.y}) with range {eb.range}")

            # Bricks destroyed
            destroyed_bricks = prev_bricks - post_bricks
            for bx, by in destroyed_bricks:
                events.append(f"- 🧱 Brick destroyed at ({bx}, {by})")

        # Item collections
        for pid in order:
            prev_item_count = tracker.items_collected.get(pid, 0)
            # Find pickups by checking items_collected diff or powerup changes
            prev_agent = prev_agents_state[pid]
            curr_agent = post_agents_state[pid]
            if curr_agent.bomb_range > prev_agent.bomb_range:
                events.append(f"- 💎 **{agent_mapping[pid]}** collected **BOMB_RANGE** item (Range: {prev_agent.bomb_range} -> {curr_agent.bomb_range})")
            if curr_agent.max_bombs > prev_agent.max_bombs:
                events.append(f"- 💎 **{agent_mapping[pid]}** collected **BOMB_CAPACITY** item (Capacity: {prev_agent.max_bombs} -> {curr_agent.max_bombs})")

        # Agent deaths
        for pid in order:
            if prev_agents_state[pid].is_alive and not post_agents_state[pid].is_alive:
                events.append(f"- 💀 **{agent_mapping[pid]}** died at ({post_agents_state[pid].x}, {post_agents_state[pid].y})!")

        if not events:
            report.append("- *No major events*")
        else:
            report.append("\n".join(events))

        report.append("\n" + "-"*40 + "\n")

    # Shutdown the thread pool to free resources
    thread_pool.shutdown(wait=False)

    # 5. Compile final statistics
    report.append("## Match Summary")
    alive_agents = [aid for aid, a in engine.state.agents.items() if a.is_alive]
    winner_id = alive_agents[0] if len(alive_agents) == 1 else None
    stats = tracker.get_final_stats(engine.state.step_count, alive_agents)

    if winner_id:
        report.append(f"🏆 **Winner:** **{agent_mapping[winner_id]} ({winner_id})**")
    else:
        report.append(f"🤝 **Match ended in a DRAW (or all dead) after {engine.state.step_count} steps.**")

    report.append("\n### Final Stats Table:\n")
    report.append("| Rank | Agent Name | Agent ID | Survival Steps | Kills | Suicides | Bricks Destroyed | Items Picked | Avg Latency (ms) |")
    report.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

    # Sort stats by rank
    stats_sorted = sorted(stats, key=lambda x: x["rank"])
    for row in stats_sorted:
        name = agent_mapping[row["agent_id"]]
        report.append(
            f"| {row['rank']} | **{name}** | {row['agent_id']} | {row['survival_steps']} | {row['kills']} | {row['suicides']} | {row['bricks_destroyed']} | {row['items_collected']} | {row['avg_latency_ms']} |"
        )

    return "\n".join(report)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bomberman AI Detailed Match Analyser")
    parser.add_argument(
        "--agents",
        nargs=4,
        default=["Minimax", "Expectimax", "A*", "BFS"],
        help="List of 4 agents to play. Choose from: Random, BFS, DFS, Greedy, A*, HillClimbing, SimulatedAnnealing, Backtracking, MinConflicts, OnlineSearch, AndOrSearch, Minimax, Expectimax."
    )
    parser.add_argument("--seed", type=int, default=42, help="Seed for the match layout.")
    parser.add_argument("--output", type=str, default=None, help="Output markdown filepath.")
    parser.add_argument("--fog", action="store_true", help="Enable Fog of War mode.")
    args = parser.parse_args()

    for agent in args.agents:
        if agent not in AGENT_FACTORIES:
            print(f"Error: Agent '{agent}' is invalid. Choose from: {list(AGENT_FACTORIES.keys())}")
            sys.exit(1)

    print(f"Starting analysis for match with agents: {args.agents} under seed {args.seed} (Fog of War: {args.fog})...")
    markdown_log = run_analyzed_match(args.agents, args.seed, fog_of_war=args.fog)

    # Determine output file
    if args.output:
        output_file = Path(args.output)
    else:
        output_dir = Path("benchmark_outputs")
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / f"match_analysis_seed_{args.seed}.md"

    output_file.write_text(markdown_log, encoding="utf-8")
    print(f"Success! Detailed match analysis saved to: [match_analysis_seed_{args.seed}.md](file:///{output_file.resolve().as_posix()})")
