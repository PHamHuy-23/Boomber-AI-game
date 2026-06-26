"""Utilities for running the same benchmark across multiple Bomberman agents.

The goal is to keep the benchmark fair:
- same number of games
- same seed range
- same environment settings
- same reporting format for every agent

This does not change the agent logic itself. It only standardizes how results
are collected so the comparison is reportable and reproducible.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Type

from agents import BaseAgent
from agents.and_or_search_agent import AndOrSearchAgent
from agents.astar_agent import AStarAgent
from agents.backtracking_agent import BacktrackingAgent
from agents.bfs_agent import BFSAgent
from agents.dfs_agent import DFSAgent
from agents.expectimax_agent import ExpectimaxAgent
from agents.greedy_agent import GreedyAgent
from agents.hill_climbing_agent import HillClimbingAgent
from agents.min_conflicts_agent import MinConflictsAgent
from agents.minimax_agent import MinimaxAgent
from agents.online_search_agent import OnlineSearchAgent
from agents.random_agent import RandomAgent
from agents.simulated_annealing_agent import SimulatedAnnealingAgent
from benchmarks.benchmark import benchmark


@dataclass(frozen=True)
class AgentSpec:
    """Declarative definition of one benchmarked agent."""

    name: str
    factory: Callable[[], BaseAgent]


def default_agent_suite() -> List[AgentSpec]:
    """Return the default set of agents to compare in reports."""
    return [
        AgentSpec("Random", lambda: RandomAgent(seed=42)),
        AgentSpec("BFS", lambda: BFSAgent()),
        AgentSpec("DFS", lambda: DFSAgent()),
        AgentSpec("Greedy", lambda: GreedyAgent()),
        AgentSpec("A*", lambda: AStarAgent()),
        AgentSpec("HillClimbing", lambda: HillClimbingAgent()),
        AgentSpec("SimulatedAnnealing", lambda: SimulatedAnnealingAgent()),
        AgentSpec("Backtracking", lambda: BacktrackingAgent()),
        AgentSpec("MinConflicts", lambda: MinConflictsAgent()),
        AgentSpec("OnlineSearch", lambda: OnlineSearchAgent()),
        AgentSpec("AndOrSearch", lambda: AndOrSearchAgent()),
        AgentSpec("Minimax", lambda: MinimaxAgent(depth=2)),
        AgentSpec("Expectimax", lambda: ExpectimaxAgent(depth=2)),
    ]


def run_agent_suite(
    num_games: int = 10,
    start_seed: int = 42,
    fog_of_war: bool = False,
    fow_radius: int = 4,
    agents: Optional[List[AgentSpec]] = None,
) -> List[Dict[str, float]]:
    """Run the benchmark for each agent and return comparable summaries."""
    suite = agents or default_agent_suite()
    results: List[Dict[str, float]] = []

    for spec in suite:
        print(f"\n=== Running {spec.name} ===")
        try:
            summary = benchmark(
                spec.factory(),
                num_games=num_games,
                start_seed=start_seed,
                fog_of_war=fog_of_war,
                fow_radius=fow_radius,
            )
            summary["agent_name"] = spec.name
            results.append(summary)
        except Exception as exc:
            print(f"[ERROR] {spec.name} failed: {exc}")
            results.append(
                {
                    "agent_name": spec.name,
                    "win_rate": 0.0,
                    "average_score": 0.0,
                    "average_steps": 0.0,
                    "average_survival_time": 0.0,
                    "average_decision_time_ms": 0.0,
                    "max_decision_time_ms": 0.0,
                    "p95_decision_time_ms": 0.0,
                    "timeout_rate_100ms": 0.0,
                    "error": str(exc),
                }
            )

    print("\n=== COMPARISON SUMMARY ===")
    for item in results:
        print(
            f"{item['agent_name']:<18} "
            f"win={item['win_rate']:.2%} "
            f"score={item['average_score']:.2f} "
            f"steps={item['average_steps']:.2f} "
            f"avg_ms={item.get('average_decision_time_ms', 0.0):.2f} "
            f"p95_ms={item.get('p95_decision_time_ms', 0.0):.2f}"
        )

    return results
