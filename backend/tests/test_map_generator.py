import pytest
from app.models import TileType
from app.map_generator import MapGenerator

def test_map_properties():
    # Set target_wall_density=0.15, target_brick_density=0.35
    generator = MapGenerator(width=15, height=13, target_wall_density=0.15, target_brick_density=0.35)
    grid = generator.generate()
    
    # Check dimensions
    assert len(grid) == 13
    assert len(grid[0]) == 15
    
    # 1. Check Borders are WALLs
    for y in range(13):
        for x in range(15):
            if x == 0 or x == 14 or y == 0 or y == 12:
                assert grid[y][x] == TileType.WALL
                
    # 2. Check Spawn Protection (Should be EMPTY)
    spawns = [(1, 1), (13, 1), (1, 11), (13, 11)]
    for sx, sy in spawns:
        assert grid[sy][sx] == TileType.EMPTY
        # Neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = sx + dx, sy + dy
            # Spawn protections should be empty, unless they are borders
            if not generator.is_border(nx, ny):
                assert grid[ny][nx] == TileType.EMPTY

    # 3. Check Reachability (Connectivity)
    # BFS from spawn (1, 1) to other spawns traversing only EMPTY
    start = (1, 1)
    visited = {start}
    queue = [start]
    
    while queue:
        cx, cy = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 15 and 0 <= ny < 13:
                if grid[ny][nx] == TileType.EMPTY and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    
    for spawn in spawns:
        assert spawn in visited, f"Spawn {spawn} is not reachable from (1, 1)"

    # 4. Check Brick and Wall Densities
    total_vars = 0
    wall_count = 0
    brick_count = 0
    for y in range(13):
        for x in range(15):
            if not generator.is_border(x, y) and (x, y) not in generator.spawn_protection:
                total_vars += 1
                if grid[y][x] == TileType.WALL:
                    wall_count += 1
                elif grid[y][x] == TileType.BRICK:
                    brick_count += 1
                    
    wall_density = wall_count / total_vars
    brick_density = brick_count / total_vars
    
    # Assert densities are within a reasonable range of targets (0.15 and 0.35)
    assert 0.10 <= wall_density <= 0.20, f"Wall density was {wall_density}, expected near 0.15"
    assert 0.30 <= brick_density <= 0.40, f"Brick density was {brick_density}, expected near 0.35"
