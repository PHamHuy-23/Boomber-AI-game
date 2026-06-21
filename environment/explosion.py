"""Explosion definition and propagation for Bomberman."""
from typing import Set, Tuple, List
from configs.default_config import GameConfig

class Explosion:
    """Represents a set of grid tiles covered by a bomb's explosion."""

    def __init__(self, x: int, y: int, blast_radius: int, owner_id: str, duration: int = GameConfig.EXPLOSION_LIFETIME):
        """
        Initialize an explosion.

        Args:
            x (int): x-coordinate of the explosion center.
            y (int): y-coordinate of the explosion center.
            blast_radius (int): Maximum range of the explosion in each direction.
            owner_id (str): ID of the player/agent who placed the bomb.
            duration (int): Remaining steps before the explosion clears.
        """
        self.center_x = x
        self.center_y = y
        self.blast_radius = blast_radius
        self.owner_id = owner_id
        self.duration = duration
        # Set of (x, y) coordinates covered by this explosion
        self.tiles: Set[Tuple[int, int]] = set()

    def propagate(self, walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], 
                  bombs_dict: dict, items_dict: dict) -> Tuple[Set[Tuple[int, int]], Set[Tuple[int, int]], List[Tuple[int, int]]]:
        """
        Calculate explosion tiles propagating from center and trigger items/bricks/other bombs.

        Args:
            walls (Set[Tuple[int, int]]): Set of indestructible wall coordinates.
            bricks (Set[Tuple[int, int]]): Set of destructible brick coordinates.
            bombs_dict (dict): Dictionary mapping (x, y) to Bomb objects.
            items_dict (dict): Dictionary mapping (x, y) to Item objects.

        Returns:
            Tuple[Set[Tuple[int, int]], Set[Tuple[int, int]], List[Tuple[int, int]]]:
                - Set of brick coordinates destroyed by this explosion.
                - Set of item coordinates destroyed by this explosion.
                - List of bomb coordinates chain-triggered by this explosion.
        """
        destroyed_bricks: Set[Tuple[int, int]] = set()
        destroyed_items: Set[Tuple[int, int]] = set()
        triggered_bombs: List[Tuple[int, int]] = []

        # Center is always affected
        self.tiles.add((self.center_x, self.center_y))

        # Check if there is a bomb at the center (it will chain react)
        if (self.center_x, self.center_y) in bombs_dict:
            triggered_bombs.append((self.center_x, self.center_y))

        directions = [
            (1, 0),   # Right
            (-1, 0),  # Left
            (0, 1),   # Down
            (0, -1)   # Up
        ]

        for dx, dy in directions:
            for dist in range(1, self.blast_radius + 1):
                tx = self.center_x + dx * dist
                ty = self.center_y + dy * dist

                # Hit permanent wall: stops propagation immediately, wall is NOT affected
                if (tx, ty) in walls:
                    break

                # Add to explosion tiles
                self.tiles.add((tx, ty))

                # Hit another bomb: chain trigger it, propagation stops/continues (usually chain-reacts and propagates)
                if (tx, ty) in bombs_dict:
                    bomb = bombs_dict[(tx, ty)]
                    if not bomb.is_exploded:
                        triggered_bombs.append((tx, ty))
                    # Do not propagate past another bomb (it will explode anyway)
                    break

                # Hit brick: destroy it and stop propagating in this direction
                if (tx, ty) in bricks:
                    destroyed_bricks.add((tx, ty))
                    break

                # Hit item: destroy the item, keep propagating
                if (tx, ty) in items_dict:
                    destroyed_items.add((tx, ty))

        return destroyed_bricks, destroyed_items, triggered_bombs

    def tick(self) -> bool:
        """
        Decrements the duration timer.

        Returns:
            bool: True if the explosion is finished and should be cleared, False otherwise.
        """
        self.duration -= 1
        return self.duration <= 0
