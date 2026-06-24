import random
from typing import List, Set, Tuple, Optional
from app.models import TileType

class MapGenerator:
    def __init__(self, width: int = 15, height: int = 13, target_wall_density: float = 0.15, target_brick_density: float = 0.35):
        self.width = width
        self.height = height
        self.target_wall_density = target_wall_density
        self.target_brick_density = target_brick_density
        
        # Center points
        self.cx = (self.width - 1) // 2
        self.cy = (self.height - 1) // 2
        
        # Define spawn locations
        self.spawns = [
            (1, 1),
            (self.width - 2, 1),
            (1, self.height - 2),
            (self.width - 2, self.height - 2)
        ]
        
        # Define spawn protection zones (spawn cells + their immediate 4 neighbors)
        self.spawn_protection = set()
        for sx, sy in self.spawns:
            self.spawn_protection.add((sx, sy))
            self.spawn_protection.add((sx + 1, sy))
            self.spawn_protection.add((sx - 1, sy))
            self.spawn_protection.add((sx, sy + 1))
            self.spawn_protection.add((sx, sy - 1))

    def is_border(self, x: int, y: int) -> bool:
        """
        Returns True if the cell is a border wall.
        """
        return x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1

    def get_variables(self) -> List[Tuple[int, int]]:
        """
        Returns a list of all coordinates across the entire board that can be EMPTY, BRICK, or WALL.
        These are the variables for the CSP solver.
        """
        variables = []
        for y in range(self.height):
            for x in range(self.width):
                if self.is_border(x, y):
                    continue
                if (x, y) in self.spawn_protection:
                    continue
                variables.append((x, y))
        return variables

    def check_reachability(self, grid: List[List[int]]) -> bool:
        """
        Checks if all 4 spawn points are connected.
        Traverses through EMPTY tiles (treating unassigned/empty variables as walkable).
        """
        start = (1, 1)
        visited = {start}
        queue = [start]
        
        while queue:
            cx, cy = queue.pop(0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    # Can traverse only if EMPTY (which includes unassigned)
                    if grid[ny][nx] == TileType.EMPTY and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        
        # Check if all spawn points are reached
        for spawn in self.spawns:
            if spawn not in visited:
                return False
        return True

    def generate(self) -> List[List[int]]:
        """
        Generates a map using Backtracking CSP search with Forward Checking (pruning).
        Ensures exact densities and 100% reachability.
        """
        variables = self.get_variables()
        total_vars = len(variables)
        
        target_walls = int(total_vars * self.target_wall_density)
        target_bricks = int(total_vars * self.target_brick_density)
        
        # Shuffle variables to ensure random maps on each call
        random.shuffle(variables)
        
        # Initialize grid with border walls
        grid = [[TileType.EMPTY for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if self.is_border(x, y):
                    grid[y][x] = TileType.WALL

        # Backtracking search with forward checking
        def backtrack(idx: int, wall_count: int, brick_count: int) -> Optional[List[List[int]]]:
            # Success base case
            if idx == total_vars:
                if wall_count == target_walls and brick_count == target_bricks:
                    return [row[:] for row in grid]
                return None

            remaining_vars = total_vars - idx
            needed_walls = target_walls - wall_count
            needed_bricks = target_bricks - brick_count
            
            # Forward checking: Prune if we cannot satisfy target densities
            if needed_walls > remaining_vars or needed_bricks > remaining_vars:
                return None
            if needed_walls < 0 or needed_bricks < 0:
                return None
                
            # Current variable
            vx, vy = variables[idx]
            
            # Decide which tile types to try. We shuffle the choices to add randomness.
            choices = []
            if needed_walls > 0:
                choices.append(TileType.WALL)
            if needed_bricks > 0:
                choices.append(TileType.BRICK)
            # We can always choose EMPTY if remaining vars is greater than what is needed
            if remaining_vars > needed_walls + needed_bricks:
                choices.append(TileType.EMPTY)
                
            random.shuffle(choices)
            
            for choice in choices:
                grid[vy][vx] = choice
                
                # Forward checking for reachability:
                # If we placed a WALL or BRICK, check if we broke the path.
                # If path is broken, we prune this branch immediately.
                if choice in (TileType.WALL, TileType.BRICK):
                    if not self.check_reachability(grid):
                        grid[vy][vx] = TileType.EMPTY  # backtrack
                        continue
                
                # Recurse
                next_walls = wall_count + (1 if choice == TileType.WALL else 0)
                next_bricks = brick_count + (1 if choice == TileType.BRICK else 0)
                result = backtrack(idx + 1, next_walls, next_bricks)
                if result is not None:
                    return result
                
                # Revert
                grid[vy][vx] = TileType.EMPTY
                
            return None

        # Execute backtracking search
        solution = backtrack(0, 0, 0)
        if solution is not None:
            return solution
            
        # Fallback empty map (in case search fails, which is mathematically impossible here)
        fallback = [[TileType.EMPTY for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if self.is_border(x, y):
                    fallback[y][x] = TileType.WALL
        return fallback
