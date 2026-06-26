"""Entry point for running BombermanAI agent benchmarks."""
from benchmarks.compare_agents import run_agent_suite
from benchmarks.benchmark import benchmark, run_game
from agents.minimax_agent import MinimaxAgent

def main():
    """Main execution flow."""
    print("Running a side-by-side benchmark suite...")
    run_agent_suite(num_games=10, start_seed=42)

    print("\nRunning a sample Minimax game with ASCII rendering...")
    agent = MinimaxAgent(depth=2)
    run_game(agent, seed=100, render_mode=True)

    print("\nRunning a focused Minimax benchmark...")
    benchmark(agent, num_games=10, start_seed=42)

if __name__ == "__main__":
    main()
