"""Map definition and generation for Bomberman."""
import random
from typing import Set, Tuple, List, Optional
from configs.default_config import GameConfig

class Map:
    """Manages the grid layout, walls, and destructible bricks."""

    def __init__(self, width: int = GameConfig.MAP_WIDTH, height: int = GameConfig.MAP_HEIGHT, 
                 wall_density: float = GameConfig.WALL_DENSITY, brick_density: float = GameConfig.BRICK_DENSITY,
                 seed: Optional[int] = None):
        """
        Initialize the map.

        Args:
            width (int): Grid width.
            height (int): Grid height.
            wall_density (float): Density of pillars.
            brick_density (float): Density of destructible bricks.
            seed (int, optional): Random seed.
        """
        self.width = width
        self.height = height
        self.wall_density = wall_density
        self.brick_density = brick_density
        self.seed = seed

        self.walls: Set[Tuple[int, int]] = set()
        self.bricks: Set[Tuple[int, int]] = set()
        self.spawns: List[Tuple[int, int]] = []
        self.spawn_protection: Set[Tuple[int, int]] = set()

        self.generate()

    def generate(self) -> None:
        """Generate border walls, pillars, protected spawn zones, and bricks."""
        if self.seed is not None:
            random.seed(self.seed)

        attempts = 0
        max_attempts = 1000
        while attempts < max_attempts:
            self.walls.clear()
            self.bricks.clear()
            self.spawn_protection.clear()

            # 1. Place border walls
            for y in range(self.height):
                for x in range(self.width):
                    if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                        self.walls.add((x, y))

            # 2. Define spawn points (corners)
            self.spawns = [
                (1, 1),
                (self.width - 2, 1),
                (1, self.height - 2),
                (self.width - 2, self.height - 2)
            ]

            # Define protection zone around spawn points
            for sx, sy in self.spawns:
                self.spawn_protection.add((sx, sy))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    self.spawn_protection.add((sx + dx, sy + dy))

            # 3. Place inner permanent wall pillars (every odd row/col index in grid coordinates)
            # Traditionally in Bomberman, pillars are at (even x, even y) if outer border is index 0.
            for y in range(2, self.height - 2, 2):
                for x in range(2, self.width - 2, 2):
                    self.walls.add((x, y))

            # 4. Gather remaining available cells for bricks
            eligible_cells = []
            for y in range(1, self.height - 1):
                for x in range(1, self.width - 1):
                    if (x, y) not in self.walls and (x, y) not in self.spawn_protection:
                        eligible_cells.append((x, y))

            # 5. Place bricks randomly based on brick density
            random.shuffle(eligible_cells)
            target_bricks = int(len(eligible_cells) * self.brick_density)
            for i in range(min(target_bricks, len(eligible_cells))):
                self.bricks.add(eligible_cells[i])

            # Ensure reachability: if all spawn points can connect, we are done
            if self._check_reachability():
                break

            attempts += 1
            if self.seed is not None:
                random.seed(self.seed + attempts)

    def _check_reachability(self) -> bool:
        """
        Check if all spawn points are connected to each other.
        We traverse through empty/walkable spaces to see if all spawn points can connect.
        """
        start = self.spawns[0]
        visited = {start}
        queue = [start]

        while queue:
            cx, cy = queue.pop(0)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    # Can walk if not a permanent wall and not a brick
                    if (nx, ny) not in self.walls and (nx, ny) not in self.bricks and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        # All spawns must be reachable
        return all(spawn in visited for spawn in self.spawns)

    def is_in_bounds(self, x: int, y: int) -> bool:
        """Check if coordinates are inside the board boundary."""
        return 0 <= x < self.width and 0 <= y < self.height

    def is_walkable(self, x: int, y: int) -> bool:
        """Check if a tile is walkable (no wall, no brick)."""
        return self.is_in_bounds(x, y) and (x, y) not in self.walls and (x, y) not in self.bricks

    def remove_brick(self, x: int, y: int) -> bool:
        """
        Remove a brick at coordinates.

        Returns:
            bool: True if brick was successfully removed, False otherwise.
        """
        if (x, y) in self.bricks:
            self.bricks.remove((x, y))
            return True
        return False

    def get_walkable_cells(self) -> Set[Tuple[int, int]]:
        """Get all empty cells that are not walls or bricks."""
        walkable = set()
        for y in range(self.height):
            for x in range(self.width):
                if self.is_walkable(x, y):
                    walkable.add((x, y))
        return walkable
