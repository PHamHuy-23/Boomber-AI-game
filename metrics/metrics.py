"""Metrics collection and aggregation for Bomberman matches."""
import numpy as np
import pandas as pd
from typing import List, Dict, Any

class MetricsTracker:
    """Tracks and aggregates statistics over multiple game runs."""

    def __init__(self):
        """Initialize the metrics lists."""
        self.scores: List[int] = []
        self.steps: List[int] = []
        self.wins: List[bool] = []
        self.survival_times: List[float] = []  # In discrete step terms

    def record_match(self, score: int, steps: int, won: bool) -> None:
        """
        Record the outcomes of a single game.

        Args:
            score (int): Score achieved in the match.
            steps (int): Number of steps taken.
            won (bool): True if the player won (eliminated all enemies), False otherwise.
        """
        self.scores.append(score)
        self.steps.append(steps)
        self.wins.append(won)
        self.survival_times.append(float(steps))

    def get_summary(self) -> Dict[str, float]:
        """
        Compute aggregate statistics across all recorded matches.

        Returns:
            Dict[str, float]: Aggregated statistics:
                - win_rate: Ratio of wins to total games.
                - average_score: Mean score achieved.
                - average_steps: Mean steps taken.
                - average_survival_time: Mean survival steps.
        """
        if not self.scores:
            return {
                "win_rate": 0.0,
                "average_score": 0.0,
                "average_steps": 0.0,
                "average_survival_time": 0.0
            }

        # Calculate using numpy for convenience
        return {
            "win_rate": float(np.mean(self.wins)),
            "average_score": float(np.mean(self.scores)),
            "average_steps": float(np.mean(self.steps)),
            "average_survival_time": float(np.mean(self.survival_times))
        }

    def to_dataframe(self) -> pd.DataFrame:
        """Export matches data to a Pandas DataFrame."""
        return pd.DataFrame({
            "score": self.scores,
            "steps": self.steps,
            "won": self.wins,
            "survival_time": self.survival_times
        })
