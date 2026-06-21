"""Bomb definition for Bomberman."""
from configs.default_config import GameConfig

class Bomb:
    """Represents a bomb placed by a player/agent."""

    def __init__(self, x: int, y: int, blast_radius: int, timer: int = GameConfig.BOMB_LIFETIME, owner_id: str = "player"):
        """
        Initialize a bomb.

        Args:
            x (int): x-coordinate of the bomb.
            y (int): y-coordinate of the bomb.
            blast_radius (int): Explosion blast radius.
            timer (int): Countdown steps before explosion.
            owner_id (str): Identifier of the agent who placed the bomb.
        """
        self.x = x
        self.y = y
        self.blast_radius = blast_radius
        self.timer = timer
        self.owner_id = owner_id
        self.is_exploded = False

    def tick(self) -> bool:
        """
        Decrement bomb timer.

        Returns:
            bool: True if the bomb is ready to explode (timer <= 0), False otherwise.
        """
        if not self.is_exploded:
            self.timer -= 1
            if self.timer <= 0:
                self.is_exploded = True
                return True
        return False

    def trigger_explosion(self) -> None:
        """Force the bomb to explode immediately (e.g. chain reaction)."""
        self.timer = 0
        self.is_exploded = True

    def to_dict(self) -> dict:
        """Serialize bomb details to a dictionary."""
        return {
            "x": self.x,
            "y": self.y,
            "timer": self.timer,
            "blast_radius": self.blast_radius,
            "owner_id": self.owner_id
        }
