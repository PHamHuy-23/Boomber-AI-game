"""Random agent implementation for Bomberman."""
import random
from agents import BaseAgent
from environment.env import Action

class RandomAgent(BaseAgent):
    """An agent that chooses actions completely at random."""

    def __init__(self, seed: int = None):
        """
        Initialize RandomAgent.

        Args:
            seed (int, optional): Random seed.
        """
        if seed is not None:
            random.seed(seed)

    def choose_action(self, state: dict) -> str:
        """
        Choose a random action from the action space.

        Args:
            state (dict): The current game state.

        Returns:
            str: Action string.
        """
        action = random.choice(list(Action))
        return action.value
