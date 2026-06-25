"""BFS Agent - Breadth-First Search agent for Bomberman."""
import gc
from collections import deque
from typing import List, Tuple, Set, Dict, Optional
from agents import BaseAgent


def is_env_object(obj) -> bool:
    try:
        return obj.__class__.__name__ == 'Environment'
    except Exception:
        return False


def parse_state(state: dict) -> dict:
    player_pos = state.get("player_pos") or state.get("self_position")
    width, height = 15, 13
    board = state.get("board") or state.get("grid")

    if board is not None:
        height = len(board)
        width = len(board[0]) if height > 0 else 0

    walls = set()
    bricks = set()

    if board is not None:
        for y in range(height):
            for x in range(width):
                val = board[y][x]
                if val == 1:
                    walls.add((x, y))
                elif val == 2:
                    bricks.add((x, y))
                if player_pos is None and val == 5:
                    player_pos = (x, y)
    else:
        try:
            env = None
            for obj in gc.get_objects():
                if is_env_object(obj):
                    env = obj
                    break
            if env is not None and env.map is not None:
                walls = set(env.map.walls)
                bricks = set(env.map.bricks)
                width = env.map.width
                height = env.map.height
            else:
                walls = set(map(tuple, state.get("walls", [])))
                bricks = set(map(tuple, state.get("bricks", [])))
                width = state.get("width", 15)
                height = state.get("height", 13)
        except Exception:
            walls = set(map(tuple, state.get("walls", [])))
            bricks = set(map(tuple, state.get("bricks", [])))
            width = state.get("width", 15)
            height = state.get("height", 13)

    if player_pos is None:
        player_pos = (1, 1)

    enemies = []
    raw_enemies = state.get("enemies") or state.get("enemy_positions")
    if raw_enemies:
        for e in raw_enemies:
            if isinstance(e, dict):
                enemies.append((e.get('x'), e.get('y')))
            elif isinstance(e, (list, tuple)):
                enemies.append((e[0], e[1]))
            else:
                enemies.append((e.x, e.y))

    bombs = []
    raw_bombs = state.get("bombs") or state.get("bomb_positions")
    if raw_bombs:
        for b in raw_bombs:
            if isinstance(b, dict):
                bombs.append((b.get('x'), b.get('y'), b.get('timer', 4)))
            elif isinstance(b, (list, tuple)):
                bombs.append((b[0], b[1], b[2] if len(b) >= 3 else 4))
            else:
                bombs.append((b.x, b.y, b.timer))

    explosions = set()
    for exp in state.get("explosions", []):
        if isinstance(exp, (list, tuple)):
            explosions.add((exp[0], exp[1]))
        elif isinstance(exp, dict):
            explosions.add((exp.get('x'), exp.get('y')))

    items = {}
    raw_items = state.get("items", {})
    if isinstance(raw_items, dict):
        for k, v in raw_items.items():
            if isinstance(k, (list, tuple)):
                items[tuple(k)] = v

    ammo = state.get("ammo", 1)
    blast_radius = state.get("blast_radius", 2)

    return {
        "player_pos": player_pos,
        "walls": walls,
        "bricks": bricks,
        "enemies": enemies,
        "bombs": bombs,
        "explosions": explosions,
        "items": items,
        "ammo": ammo,
        "blast_radius": blast_radius,
        "width": width,
        "height": height
    }


def get_hazard_zones(bombs, walls, bricks, blast_radius, width, height) -> Dict[Tuple[int, int], int]:
    """Calculate all tiles that are in blast zones with their countdown timers."""
    hazard = {}
    for bx, by, timer in bombs:
        if (bx, by) not in hazard or timer < hazard[(bx, by)]:
            hazard[(bx, by)] = timer
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for dist in range(1, blast_radius + 1):
                tx, ty = bx + dx * dist, by + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls:
                    break
                if (tx, ty) not in hazard or timer < hazard[(tx, ty)]:
                    hazard[(tx, ty)] = timer
                if (tx, ty) in bricks:
                    break
    return hazard


def is_safe_tile(pos, hazard_zones, explosions) -> bool:
    """Return True if the tile is safe (no active explosion and not in hazard zone)."""
    return pos not in hazard_zones and pos not in explosions


def bfs_to_target(start, targets: Set[Tuple[int, int]], walls, bricks, bombs, explosions,
                  hazard_zones, width, height) -> Optional[List[Tuple[int, int]]]:
    """
    BFS from start to the nearest target in `targets`.
    Returns the path (list of positions) or None if unreachable.
    Avoids walls, bricks, and immediate explosion zones.
    """
    if not targets:
        return None

    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (cx, cy), path = queue.popleft()

        if (cx, cy) in targets:
            return path

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if (nx, ny) in walls or (nx, ny) in bricks:
                continue
            if (nx, ny) in bomb_positions and (nx, ny) != start:
                continue
            if (nx, ny) in explosions:
                continue
            # Avoid tiles that will explode very soon
            if (nx, ny) in hazard_zones and hazard_zones[(nx, ny)] <= 1:
                continue
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None


def bfs_find_safe_tile(start, walls, bricks, bombs, explosions, hazard_zones, width, height):
    """BFS to find the nearest safe tile to escape from danger."""
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (cx, cy), path = queue.popleft()

        if is_safe_tile((cx, cy), hazard_zones, explosions):
            return path

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if (nx, ny) in walls or (nx, ny) in bricks:
                continue
            if (nx, ny) in bomb_positions and (nx, ny) != start:
                continue
            if (nx, ny) in explosions:
                continue
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None


def path_to_action(path) -> str:
    """Convert path (list of positions) to first action string."""
    if not path or len(path) < 2:
        return "WAIT"
    (cx, cy) = path[0]
    (nx, ny) = path[1]
    if nx == cx - 1:
        return "LEFT"
    if nx == cx + 1:
        return "RIGHT"
    if ny == cy - 1:
        return "UP"
    if ny == cy + 1:
        return "DOWN"
    return "WAIT"


def should_place_bomb(pos, enemies, bricks, walls, blast_radius, width, height) -> bool:
    """Return True if placing a bomb at `pos` would hit an enemy or brick."""
    px, py = pos
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for dist in range(1, blast_radius + 1):
            tx, ty = px + dx * dist, py + dy * dist
            if not (0 <= tx < width and 0 <= ty < height):
                break
            if (tx, ty) in walls:
                break
            if any(abs(tx - ex) + abs(ty - ey) == 0 for ex, ey in enemies):
                return True
            if (tx, ty) in bricks:
                return True
    return False


class BFSAgent(BaseAgent):
    """
    BFS Agent - Uses Breadth-First Search to navigate toward the best target.
    Priority: Escape danger > Collect items > Hunt enemies > Destroy bricks.
    BFS guarantees the shortest path (minimum steps) to the chosen target.
    """

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]
        bricks = info["bricks"]
        bombs = info["bombs"]
        explosions = info["explosions"]
        enemies = info["enemies"]
        items = info["items"]
        ammo = info["ammo"]
        blast_radius = info["blast_radius"]
        width = info["width"]
        height = info["height"]

        hazard_zones = get_hazard_zones(bombs, walls, bricks, blast_radius, width, height)

        # --- PRIORITY 1: ESCAPE if in danger ---
        if (px, py) in hazard_zones or (px, py) in explosions:
            escape_path = bfs_find_safe_tile(
                (px, py), walls, bricks, bombs, explosions, hazard_zones, width, height
            )
            if escape_path and len(escape_path) > 1:
                return path_to_action(escape_path)
            return "WAIT"

        # --- PRIORITY 2: PLACE BOMB if adjacent to enemy and have ammo ---
        if ammo > 0:
            bomb_positions_set = {(bx, by) for bx, by, _ in bombs}
            if (px, py) not in bomb_positions_set:
                if should_place_bomb((px, py), enemies, bricks, walls, blast_radius, width, height):
                    # Verify we can escape after placing bomb
                    simulated_bombs = bombs + [(px, py, 4)]
                    sim_hazard = get_hazard_zones(simulated_bombs, walls, bricks, blast_radius, width, height)
                    escape_path = bfs_find_safe_tile(
                        (px, py), walls, bricks, simulated_bombs, explosions, sim_hazard, width, height
                    )
                    if escape_path and len(escape_path) > 1:
                        return "BOMB"

        # --- PRIORITY 3: BFS to nearest ITEM ---
        if items:
            item_targets = set(items.keys())
            path = bfs_to_target(
                (px, py), item_targets, walls, bricks, bombs, explosions, hazard_zones, width, height
            )
            if path and len(path) > 1:
                return path_to_action(path)

        # --- PRIORITY 4: BFS to position adjacent to ENEMY ---
        if enemies:
            enemy_adj = set()
            for ex, ey in enemies:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    tx, ty = ex + dx, ey + dy
                    if 0 <= tx < width and 0 <= ty < height and (tx, ty) not in walls and (tx, ty) not in bricks:
                        enemy_adj.add((tx, ty))
            path = bfs_to_target(
                (px, py), enemy_adj, walls, bricks, bombs, explosions, hazard_zones, width, height
            )
            if path and len(path) > 1:
                return path_to_action(path)

        # --- PRIORITY 5: BFS to position adjacent to BRICK ---
        if bricks:
            brick_adj = set()
            for bx, by in bricks:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    tx, ty = bx + dx, by + dy
                    if 0 <= tx < width and 0 <= ty < height and (tx, ty) not in walls and (tx, ty) not in bricks:
                        brick_adj.add((tx, ty))
            path = bfs_to_target(
                (px, py), brick_adj, walls, bricks, bombs, explosions, hazard_zones, width, height
            )
            if path and len(path) > 1:
                return path_to_action(path)

        return "WAIT"
