"""Agents package containing BaseAgent and its implementations."""
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract base class for all Bomberman agents."""

    @abstractmethod
    def choose_action(self, state: dict) -> str:
        """
        Choose an action from the action space based on the current game state.

        Args:
            state (dict): Dictionary representing the current environment state.

        Returns:
            str: The chosen action string ('UP', 'DOWN', 'LEFT', 'RIGHT', 'BOMB', 'WAIT').
        """
        pass
