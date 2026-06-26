"""Benchmarking system to evaluate Bomberman agents."""
from typing import Dict, Any, List
import statistics
import time
from environment.env import Environment
from agents import BaseAgent
from metrics.metrics import MetricsTracker

def run_game(agent: BaseAgent, seed: int = None, render_mode: bool = False, fog_of_war: bool = False, fow_radius: int = 4) -> Dict[str, Any]:
    """
    Run a single game of Bomberman using the provided agent.

    Args:
        agent (BaseAgent): The agent choosing the actions.
        seed (int, optional): Random seed for environment.
        render_mode (bool): Whether to render the game board in ASCII.
        fog_of_war (bool): Whether to enable Fog of War.
        fow_radius (int): Radius of visibility around the agent.

    Returns:
        Dict[str, Any]: Results of the match:
            - score (int): Final player score.
            - steps (int): Steps survived.
            - won (bool): True if victory achieved, False otherwise.
            - decision_times_ms (List[float]): Per-step agent decision latency in ms.
            - avg_decision_time_ms (float): Mean per-step latency in ms.
            - max_decision_time_ms (float): Max per-step latency in ms.
            - p95_decision_time_ms (float): 95th percentile decision latency in ms.
    """
    env = Environment(seed=seed, fog_of_war=fog_of_war, fow_radius=fow_radius)
    state = env.reset()
    done = False
    decision_times_ms: List[float] = []
    
    if render_mode:
        env.render()

    while not done:
        t0 = time.perf_counter()
        action = agent.choose_action(state)
        t1 = time.perf_counter()
        decision_times_ms.append((t1 - t0) * 1000.0)
        state, reward, done, info = env.step(action)
        
        if render_mode:
            env.render()

    avg_decision_time_ms = float(sum(decision_times_ms) / len(decision_times_ms)) if decision_times_ms else 0.0
    max_decision_time_ms = float(max(decision_times_ms)) if decision_times_ms else 0.0
    p95_decision_time_ms = float(statistics.quantiles(decision_times_ms, n=20)[18]) if len(decision_times_ms) >= 2 else max_decision_time_ms

    return {
        "score": info.get("player_score", 0),
        "steps": env.current_step,
        "won": info.get("game_won", False),
        "decision_times_ms": decision_times_ms,
        "avg_decision_time_ms": avg_decision_time_ms,
        "max_decision_time_ms": max_decision_time_ms,
        "p95_decision_time_ms": p95_decision_time_ms,
    }

def benchmark(agent: BaseAgent, num_games: int = 10, start_seed: int = 42, fog_of_war: bool = False, fow_radius: int = 4) -> Dict[str, float]:
    """
    Evaluate an agent over a specified number of games.

    Args:
        agent (BaseAgent): The agent to evaluate.
        num_games (int): The number of matches to run.
        start_seed (int): The starting seed for reproducible games.
        fog_of_war (bool): Whether to enable Fog of War.
        fow_radius (int): Radius of visibility around the agent.

    Returns:
        Dict[str, float]: Aggregated benchmark performance:
            - win_rate (float)
            - average_score (float)
            - average_steps (float)
            - average_survival_time (float)
            - average_decision_time_ms (float)
            - max_decision_time_ms (float)
            - p95_decision_time_ms (float)
            - timeout_rate_100ms (float)
    """
    tracker = MetricsTracker()
    all_decision_times: List[float] = []
    timeout_100ms = 0
    total_decisions = 0

    for game_idx in range(num_games):
        seed = start_seed + game_idx
        # Run match (we don't render to keep benchmark fast)
        result = run_game(agent, seed=seed, render_mode=False, fog_of_war=fog_of_war, fow_radius=fow_radius)
        tracker.record_match(
            score=result["score"],
            steps=result["steps"],
            won=result["won"]
        )
        all_decision_times.extend(result.get("decision_times_ms", []))
        timeout_100ms += sum(1 for t in result.get("decision_times_ms", []) if t > 100.0)
        total_decisions += len(result.get("decision_times_ms", []))

    summary = tracker.get_summary()
    average_decision_time_ms = float(sum(all_decision_times) / len(all_decision_times)) if all_decision_times else 0.0
    max_decision_time_ms = float(max(all_decision_times)) if all_decision_times else 0.0
    p95_decision_time_ms = float(statistics.quantiles(all_decision_times, n=20)[18]) if len(all_decision_times) >= 2 else max_decision_time_ms
    timeout_rate_100ms = float(timeout_100ms / total_decisions) if total_decisions else 0.0

    summary.update({
        "average_decision_time_ms": average_decision_time_ms,
        "max_decision_time_ms": max_decision_time_ms,
        "p95_decision_time_ms": p95_decision_time_ms,
        "timeout_rate_100ms": timeout_rate_100ms,
    })
    print(f"=== BENCHMARK REPORT ({num_games} Games) ===")
    print(f"Win Rate:              {summary['win_rate']:.2%}")
    print(f"Average Score:         {summary['average_score']:.2f}")
    print(f"Average Steps:         {summary['average_steps']:.2f}")
    print(f"Average Survival Time: {summary['average_survival_time']:.2f} ticks")
    print(f"Avg Decision Time:      {summary['average_decision_time_ms']:.2f} ms")
    print(f"P95 Decision Time:      {summary['p95_decision_time_ms']:.2f} ms")
    print(f"Max Decision Time:      {summary['max_decision_time_ms']:.2f} ms")
    print(f"100ms Timeout Rate:     {summary['timeout_rate_100ms']:.2%}")
    print("============================================")

    return summary
