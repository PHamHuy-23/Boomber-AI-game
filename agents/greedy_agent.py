"""Greedy Best-First Search Agent for Bomberman."""
import gc
import heapq
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
                if val == 1: walls.add((x, y))
                elif val == 2: bricks.add((x, y))
                if player_pos is None and val == 5: player_pos = (x, y)
    else:
        try:
            env = None
            for obj in gc.get_objects():
                if is_env_object(obj):
                    env = obj; break
            if env is not None and env.map is not None:
                walls = set(env.map.walls); bricks = set(env.map.bricks)
                width = env.map.width; height = env.map.height
            else:
                walls = set(map(tuple, state.get("walls", []))); bricks = set(map(tuple, state.get("bricks", [])))
                width = state.get("width", 15); height = state.get("height", 13)
        except Exception:
            walls = set(map(tuple, state.get("walls", []))); bricks = set(map(tuple, state.get("bricks", [])))
            width = state.get("width", 15); height = state.get("height", 13)
    if player_pos is None: player_pos = (1, 1)
    enemies = []
    raw_enemies = state.get("enemies") or state.get("enemy_positions")
    if raw_enemies:
        for e in raw_enemies:
            if isinstance(e, dict): enemies.append((e.get('x'), e.get('y')))
            elif isinstance(e, (list, tuple)): enemies.append((e[0], e[1]))
            else: enemies.append((e.x, e.y))
    bombs = []
    raw_bombs = state.get("bombs") or state.get("bomb_positions")
    if raw_bombs:
        for b in raw_bombs:
            if isinstance(b, dict): bombs.append((b.get('x'), b.get('y'), b.get('timer', 4)))
            elif isinstance(b, (list, tuple)): bombs.append((b[0], b[1], b[2] if len(b) >= 3 else 4))
            else: bombs.append((b.x, b.y, b.timer))
    explosions = set()
    for exp in state.get("explosions", []):
        if isinstance(exp, (list, tuple)): explosions.add((exp[0], exp[1]))
        elif isinstance(exp, dict): explosions.add((exp.get('x'), exp.get('y')))
    items = {}
    raw_items = state.get("items", {})
    if isinstance(raw_items, dict):
        for k, v in raw_items.items():
            if isinstance(k, (list, tuple)): items[tuple(k)] = v
    return {
        "player_pos": player_pos, "walls": walls, "bricks": bricks, "enemies": enemies,
        "bombs": bombs, "explosions": explosions, "items": items,
        "ammo": state.get("ammo", 1), "blast_radius": state.get("blast_radius", 2),
        "width": width, "height": height
    }


def get_hazard_zones(bombs, walls, bricks, blast_radius, width, height) -> Dict:
    hazard = {}
    for bx, by, timer in bombs:
        if (bx, by) not in hazard or timer < hazard[(bx, by)]: hazard[(bx, by)] = timer
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            for dist in range(1, blast_radius+1):
                tx, ty = bx+dx*dist, by+dy*dist
                if not (0<=tx<width and 0<=ty<height): break
                if (tx,ty) in walls: break
                if (tx,ty) not in hazard or timer < hazard[(tx,ty)]: hazard[(tx,ty)] = timer
                if (tx,ty) in bricks: break
    return hazard


def manhattan(a, b) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def greedy_search(start, targets: Set[Tuple[int, int]], walls, bricks, bombs,
                  explosions, hazard_zones, width, height) -> Optional[List]:
    """
    Greedy Best-First Search: always expand the node with the smallest h(n).
    h(n) = min Manhattan distance to any target.
    Does NOT consider g(n), so it's faster than A* but not optimal.
    """
    if not targets: return None
    bomb_positions = {(bx, by) for bx, by, _ in bombs}

    def h(pos):
        return min(manhattan(pos, t) for t in targets)

    # (h_val, pos, path)
    open_heap = [(h(start), start, [start])]
    visited = {start}

    while open_heap:
        _, (cx, cy), path = heapq.heappop(open_heap)

        if (cx, cy) in targets:
            return path

        for dx, dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            nx, ny = cx+dx, cy+dy
            if not (0<=nx<width and 0<=ny<height): continue
            if (nx,ny) in walls or (nx,ny) in bricks: continue
            if (nx,ny) in bomb_positions and (nx,ny) != start: continue
            if (nx,ny) in explosions: continue
            if (nx,ny) in hazard_zones and hazard_zones[(nx,ny)] <= 1: continue
            if (nx,ny) not in visited:
                visited.add((nx,ny))
                heapq.heappush(open_heap, (h((nx,ny)), (nx,ny), path+[(nx,ny)]))

    return None


def bfs_escape(start, walls, bricks, bombs, explosions, hazard_zones, width, height) -> str:
    bomb_positions = {(bx,by) for bx,by,_ in bombs}
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        (cx,cy), path = queue.popleft()
        if (cx,cy) not in hazard_zones and (cx,cy) not in explosions:
            return path[0] if path else "WAIT"
        for dx,dy,action in [(0,-1,"UP"),(0,1,"DOWN"),(-1,0,"LEFT"),(1,0,"RIGHT")]:
            nx,ny = cx+dx,cy+dy
            if not (0<=nx<width and 0<=ny<height): continue
            if (nx,ny) in walls or (nx,ny) in bricks: continue
            if (nx,ny) in bomb_positions and (nx,ny) != start: continue
            if (nx,ny) in explosions: continue
            if (nx,ny) not in visited:
                visited.add((nx,ny)); queue.append(((nx,ny), path+[action]))
    return "WAIT"


def path_to_action(path) -> str:
    if not path or len(path)<2: return "WAIT"
    cx,cy = path[0]; nx,ny = path[1]
    if nx==cx-1: return "LEFT"
    if nx==cx+1: return "RIGHT"
    if ny==cy-1: return "UP"
    if ny==cy+1: return "DOWN"
    return "WAIT"


def should_place_bomb(pos, enemies, bricks, walls, blast_radius, width, height) -> bool:
    px,py = pos
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        for dist in range(1, blast_radius+1):
            tx,ty = px+dx*dist, py+dy*dist
            if not (0<=tx<width and 0<=ty<height): break
            if (tx,ty) in walls: break
            if any(tx==ex and ty==ey for ex,ey in enemies): return True
            if (tx,ty) in bricks: return True
    return False


class GreedyAgent(BaseAgent):
    """
    Greedy Best-First Search Agent.
    Expands nodes by h(n) only (minimum estimated distance to goal).
    No cost tracking (no g(n)), making it faster than A* but potentially suboptimal.
    Good for quick decisions in open spaces; can get trapped in local optima.
    """

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]; bricks = info["bricks"]
        bombs = info["bombs"]; explosions = info["explosions"]
        enemies = info["enemies"]; items = info["items"]
        ammo = info["ammo"]; blast_radius = info["blast_radius"]
        width = info["width"]; height = info["height"]

        hazard_zones = get_hazard_zones(bombs, walls, bricks, blast_radius, width, height)

        # PRIORITY 1: Escape
        if (px,py) in hazard_zones or (px,py) in explosions:
            safe_targets = {(x,y) for y in range(height) for x in range(width)
                           if (x,y) not in walls and (x,y) not in bricks
                           and (x,y) not in hazard_zones and (x,y) not in explosions}
            path = greedy_search((px,py), safe_targets, walls, bricks, bombs, explosions, hazard_zones, width, height)
            if path and len(path) > 1: return path_to_action(path)
            return bfs_escape((px,py), walls, bricks, bombs, explosions, hazard_zones, width, height)

        # PRIORITY 2: Place bomb
        if ammo > 0:
            bomb_pos_set = {(bx,by) for bx,by,_ in bombs}
            if (px,py) not in bomb_pos_set and should_place_bomb((px,py), enemies, bricks, walls, blast_radius, width, height):
                sim_bombs = bombs + [(px,py,4)]
                sim_hazard = get_hazard_zones(sim_bombs, walls, bricks, blast_radius, width, height)
                if bfs_escape((px,py), walls, bricks, sim_bombs, explosions, sim_hazard, width, height) != "WAIT":
                    return "BOMB"

        # PRIORITY 3: Greedy to nearest item
        if items:
            path = greedy_search((px,py), set(items.keys()), walls, bricks, bombs, explosions, hazard_zones, width, height)
            if path and len(path) > 1: return path_to_action(path)

        # PRIORITY 4: Greedy to adjacent enemy
        if enemies:
            enemy_adj = {(ex+dx, ey+dy) for ex,ey in enemies for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]
                         if 0<=ex+dx<width and 0<=ey+dy<height and (ex+dx,ey+dy) not in walls and (ex+dx,ey+dy) not in bricks}
            path = greedy_search((px,py), enemy_adj, walls, bricks, bombs, explosions, hazard_zones, width, height)
            if path and len(path) > 1: return path_to_action(path)

        # PRIORITY 5: Greedy to adjacent brick
        if bricks:
            brick_adj = {(bx+dx,by+dy) for bx,by in bricks for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]
                         if 0<=bx+dx<width and 0<=by+dy<height and (bx+dx,by+dy) not in walls and (bx+dx,by+dy) not in bricks}
            path = greedy_search((px,py), brick_adj, walls, bricks, bombs, explosions, hazard_zones, width, height)
            if path and len(path) > 1: return path_to_action(path)

        return "WAIT"
