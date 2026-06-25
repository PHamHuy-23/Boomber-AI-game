"""DFS Agent - Depth-First Search agent for Bomberman."""
import gc
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


def heuristic(pos, enemies, items, bricks, ammo, width, height) -> float:
    """Simple heuristic: prefer positions near items/enemies, away from center of bricks."""
    px, py = pos
    score = 0.0

    # Reward being near items
    for (ix, iy) in items.keys():
        dist = abs(px - ix) + abs(py - iy)
        score += 500.0 / (dist + 1)

    # Reward being near enemies (to attack)
    for ex, ey in enemies:
        dist = abs(px - ex) + abs(py - ey)
        if ammo > 0:
            score += 200.0 / (dist + 1)
        else:
            score -= 100.0 / (dist + 1)

    # Slight reward for being near bricks (to blast them)
    for bx, by in bricks:
        dist = abs(px - bx) + abs(py - by)
        if dist == 1:
            score += 50.0

    return score


def dfs_search(start, walls, bricks, bombs, explosions, hazard_zones,
               enemies, items, ammo, blast_radius, width, height, depth_limit=5):
    """
    DFS with depth limit. Returns (best_score, first_action).
    Explores paths up to depth_limit steps deep, choosing the path with best terminal heuristic.
    """
    bomb_positions = {(bx, by) for bx, by, _ in bombs}

    best_result = [(-float('inf'), "WAIT")]

    def dfs(cx, cy, depth, path, visited):
        # Terminal: evaluate at max depth
        if depth == depth_limit:
            score = heuristic((cx, cy), enemies, items, bricks, ammo, width, height)
            # Penalize if in hazard at terminal
            if (cx, cy) in hazard_zones:
                score -= 5000.0
            if depth > 0 and score > best_result[0][0]:
                first_action = path[0] if path else "WAIT"
                best_result[0] = (score, first_action)
            return

        directions = [(0, -1, "UP"), (0, 1, "DOWN"), (-1, 0, "LEFT"), (1, 0, "RIGHT")]

        for dx, dy, action in directions:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if (nx, ny) in walls or (nx, ny) in bricks:
                continue
            if (nx, ny) in bomb_positions and (nx, ny) != start:
                continue
            if (nx, ny) in explosions:
                continue
            if (nx, ny) in hazard_zones and hazard_zones[(nx, ny)] <= depth + 1:
                continue  # Would be caught in explosion
            if (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            first = path[0] if path else action
            dfs(nx, ny, depth + 1, [first] if not path else path, visited)
            visited.discard((nx, ny))

    dfs(start[0], start[1], 0, [], {start})
    return best_result[0]


def bfs_escape(start, walls, bricks, bombs, explosions, hazard_zones, width, height):
    """Quick BFS escape when in danger."""
    from collections import deque
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        (cx, cy), path = queue.popleft()
        if (cx, cy) not in hazard_zones and (cx, cy) not in explosions:
            return path[0] if path else "WAIT"
        for dx, dy, action in [(0, -1, "UP"), (0, 1, "DOWN"), (-1, 0, "LEFT"), (1, 0, "RIGHT")]:
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
                queue.append(((nx, ny), path + [action]))
    return "WAIT"


class DFSAgent(BaseAgent):
    """
    DFS Agent - Uses Depth-First Search with depth limit to explore future states.
    Explores deeply along one path before backtracking, choosing the path with the
    best terminal heuristic score. Faster than BFS but paths may be suboptimal.
    """

    def __init__(self, depth_limit: int = 5):
        self.depth_limit = depth_limit

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

        # Priority 1: Escape danger immediately using BFS (DFS bad for escape)
        if (px, py) in hazard_zones or (px, py) in explosions:
            return bfs_escape((px, py), walls, bricks, bombs, explosions, hazard_zones, width, height)

        # Priority 2: Place bomb if adjacent to enemy or brick
        if ammo > 0:
            bomb_positions_set = {(bx, by) for bx, by, _ in bombs}
            if (px, py) not in bomb_positions_set:
                near_target = False
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    tx, ty = px + dx, py + dy
                    if any(tx == ex and ty == ey for ex, ey in enemies):
                        near_target = True
                        break
                    if (tx, ty) in bricks:
                        near_target = True
                        break
                if near_target:
                    simulated_bombs = bombs + [(px, py, 4)]
                    sim_hazard = get_hazard_zones(simulated_bombs, walls, bricks, blast_radius, width, height)
                    escape = bfs_escape((px, py), walls, bricks, simulated_bombs, explosions, sim_hazard, width, height)
                    if escape != "WAIT":
                        return "BOMB"

        # Priority 3: DFS exploration
        _score, action = dfs_search(
            (px, py), walls, bricks, bombs, explosions, hazard_zones,
            enemies, items, ammo, blast_radius, width, height, self.depth_limit
        )
        return action
