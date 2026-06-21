"""Benchmarking system to evaluate Bomberman agents."""
from typing import Dict, Any
from environment.env import Environment
from agents import BaseAgent
from metrics.metrics import MetricsTracker

def run_game(agent: BaseAgent, seed: int = None, render_mode: bool = False) -> Dict[str, Any]:
    """
    Run a single game of Bomberman using the provided agent.

    Args:
        agent (BaseAgent): The agent choosing the actions.
        seed (int, optional): Random seed for environment.
        render_mode (bool): Whether to render the game board in ASCII.

    Returns:
        Dict[str, Any]: Results of the match:
            - score (int): Final player score.
            - steps (int): Steps survived.
            - won (bool): True if victory achieved, False otherwise.
    """
    env = Environment(seed=seed)
    state = env.reset()
    done = False
    
    if render_mode:
        env.render()

    while not done:
        action = agent.choose_action(state)
        state, reward, done, info = env.step(action)
        
        if render_mode:
            env.render()

    return {
        "score": info.get("player_score", 0),
        "steps": env.current_step,
        "won": info.get("game_won", False)
    }

def benchmark(agent: BaseAgent, num_games: int = 10, start_seed: int = 42) -> Dict[str, float]:
    """
    Evaluate an agent over a specified number of games.

    Args:
        agent (BaseAgent): The agent to evaluate.
        num_games (int): The number of matches to run.
        start_seed (int): The starting seed for reproducible games.

    Returns:
        Dict[str, float]: Aggregated benchmark performance:
            - win_rate (float)
            - average_score (float)
            - average_steps (float)
            - average_survival_time (float)
    """
    tracker = MetricsTracker()

    for game_idx in range(num_games):
        seed = start_seed + game_idx
        # Run match (we don't render to keep benchmark fast)
        result = run_game(agent, seed=seed, render_mode=False)
        tracker.record_match(
            score=result["score"],
            steps=result["steps"],
            won=result["won"]
        )

    summary = tracker.get_summary()
    print(f"=== BENCHMARK REPORT ({num_games} Games) ===")
    print(f"Win Rate:              {summary['win_rate']:.2%}")
    print(f"Average Score:         {summary['average_score']:.2f}")
    print(f"Average Steps:         {summary['average_steps']:.2f}")
    print(f"Average Survival Time: {summary['average_survival_time']:.2f} ticks")
    print("============================================")

    return summary
