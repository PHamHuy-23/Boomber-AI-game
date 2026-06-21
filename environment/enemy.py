"""Enemy definition and behavior for Bomberman."""
import random
from typing import List, Tuple, Set

class Enemy:
    """Represents an NPC enemy on the grid."""

    def __init__(self, enemy_id: str, x: int, y: int):
        """
        Initialize the enemy.

        Args:
            enemy_id (str): Unique identifier.
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
        """
        self.id = enemy_id
        self.x = x
        self.y = y
        self.is_alive = True

    def move_to(self, x: int, y: int) -> None:
        """Update enemy position."""
        self.x = x
        self.y = y

    def lose_life(self) -> None:
        """Kills the enemy."""
        self.is_alive = False

    def choose_move(self, walkable_cells: Set[Tuple[int, int]]) -> Tuple[int, int]:
        """
        Choose a valid next position from adjacent walkable cells.

        Args:
            walkable_cells (Set[Tuple[int, int]]): Set of all coordinate tuples that are currently empty of walls/bricks.

        Returns:
            Tuple[int, int]: Next position (x, y).
        """
        if not self.is_alive:
            return (self.x, self.y)

        candidates = [
            (self.x, self.y),  # Can wait
            (self.x + 1, self.y),
            (self.x - 1, self.y),
            (self.x, self.y + 1),
            (self.x, self.y - 1)
        ]
        
        # Filter moves that are in walkable_cells
        valid_moves = [move for move in candidates if move in walkable_cells or move == (self.x, self.y)]
        
        if not valid_moves:
            return (self.x, self.y)
            
        # 80% chance to move to a new square if available, otherwise stay
        if len(valid_moves) > 1 and random.random() < 0.8:
            new_moves = [m for m in valid_moves if m != (self.x, self.y)]
            return random.choice(new_moves)
        return (self.x, self.y)

    def to_dict(self) -> dict:
        """Serialize enemy details to a dictionary."""
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "is_alive": self.is_alive
        }
