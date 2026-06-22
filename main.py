"""Entry point for running BombermanAI agent benchmarks."""
import sys
from agents.minimax_agent import MinimaxAgent
from benchmarks.benchmark import benchmark, run_game

def main():
    """Main execution flow."""
    print("Initializing MinimaxAgent...")
    agent = MinimaxAgent(depth=2)

    # Display a sample game rendering so the user can see the environment physics in action
    print("\nRunning a sample game with ASCII rendering...")
    # Run 1 game and render it
    run_game(agent, seed=100, render_mode=True)

    print("\nStarting benchmark of 10 matches...")
    # Evaluate over 10 games
    benchmark(agent, num_games=10, start_seed=42)

if __name__ == "__main__":
    main()
