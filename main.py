"""Entry point for running BombermanAI agent benchmarks."""
import sys
from agents.random_agent import RandomAgent
from benchmark.benchmark import benchmark, run_game

def main():
    """Main execution flow."""
    print("Initializing RandomAgent...")
    agent = RandomAgent(seed=42)

    # Display a sample game rendering so the user can see the environment physics in action
    print("\nRunning a sample game with ASCII rendering...")
    # Run 1 game and render it
    run_game(agent, seed=100, render_mode=True)

    print("\nStarting benchmark of 10 matches...")
    # Evaluate over 10 games
    benchmark(agent, num_games=10, start_seed=42)

if __name__ == "__main__":
    main()
