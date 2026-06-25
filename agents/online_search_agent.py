"""Online Search Agent (LRTA* - Learning Real-Time A*) for Bomberman."""
import gc
from collections import deque
from typing import Tuple, Dict, Set, List, Optional
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
        height = len(board); width = len(board[0]) if height > 0 else 0
    walls = set(); bricks = set()
    if board is not None:
        for y in range(height):
            for x in range(width):
                val = board[y][x]
                if val == 1: walls.add((x,y))
                elif val == 2: bricks.add((x,y))
                if player_pos is None and val == 5: player_pos = (x,y)
    else:
        try:
            env = None
            for obj in gc.get_objects():
                if is_env_object(obj): env = obj; break
            if env is not None and env.map is not None:
                walls = set(env.map.walls); bricks = set(env.map.bricks)
                width = env.map.width; height = env.map.height
            else:
                walls = set(map(tuple, state.get("walls",[]))); bricks = set(map(tuple, state.get("bricks",[])))
                width = state.get("width",15); height = state.get("height",13)
        except Exception:
            walls = set(map(tuple, state.get("walls",[]))); bricks = set(map(tuple, state.get("bricks",[])))
            width = state.get("width",15); height = state.get("height",13)
    if player_pos is None: player_pos = (1,1)
    enemies = []
    raw = state.get("enemies") or state.get("enemy_positions")
    if raw:
        for e in raw:
            if isinstance(e, dict): enemies.append((e.get('x'),e.get('y')))
            elif isinstance(e, (list,tuple)): enemies.append((e[0],e[1]))
            else: enemies.append((e.x,e.y))
    bombs = []
    raw = state.get("bombs") or state.get("bomb_positions")
    if raw:
        for b in raw:
            if isinstance(b, dict): bombs.append((b.get('x'),b.get('y'),b.get('timer',4)))
            elif isinstance(b, (list,tuple)): bombs.append((b[0],b[1],b[2] if len(b)>=3 else 4))
            else: bombs.append((b.x,b.y,b.timer))
    explosions = set()
    for exp in state.get("explosions",[]):
        if isinstance(exp,(list,tuple)): explosions.add((exp[0],exp[1]))
        elif isinstance(exp,dict): explosions.add((exp.get('x'),exp.get('y')))
    items = {}
    raw = state.get("items",{})
    if isinstance(raw,dict):
        for k,v in raw.items():
            if isinstance(k,(list,tuple)): items[tuple(k)] = v
    return {
        "player_pos": player_pos, "walls": walls, "bricks": bricks, "enemies": enemies,
        "bombs": bombs, "explosions": explosions, "items": items,
        "ammo": state.get("ammo",1), "blast_radius": state.get("blast_radius",2),
        "width": width, "height": height
    }


def get_hazard_zones(bombs, walls, bricks, blast_radius, width, height) -> Dict:
    hazard = {}
    for bx,by,timer in bombs:
        if (bx,by) not in hazard or timer<hazard[(bx,by)]: hazard[(bx,by)] = timer
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            for dist in range(1,blast_radius+1):
                tx,ty = bx+dx*dist, by+dy*dist
                if not (0<=tx<width and 0<=ty<height): break
                if (tx,ty) in walls: break
                if (tx,ty) not in hazard or timer<hazard[(tx,ty)]: hazard[(tx,ty)] = timer
                if (tx,ty) in bricks: break
    return hazard


def bfs_escape(start, walls, bricks, bombs, explosions, hazard_zones, width, height) -> str:
    bomb_positions = {(bx,by) for bx,by,_ in bombs}
    queue = deque([(start,[])])
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


def initial_heuristic(pos, enemies, items, bricks, ammo, width, height) -> float:
    """Initial heuristic estimate H(s) for LRTA*."""
    px, py = pos
    h = float('inf')

    # h = distance to nearest goal (item > enemy > brick)
    for ix, iy in items.keys():
        d = abs(px-ix)+abs(py-iy)
        if d < h: h = d

    if h == float('inf'):
        for ex, ey in enemies:
            d = abs(px-ex)+abs(py-ey)
            if ammo > 0 and d-1 < h: h = d-1

    if h == float('inf'):
        for bx, by in bricks:
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                ax, ay = bx+dx, by+dy
                d = abs(px-ax)+abs(py-ay)
                if d < h: h = d

    return float(h) if h != float('inf') else 10.0


class OnlineSearchAgent(BaseAgent):
    """
    Online Search Agent using LRTA* (Learning Real-Time A*).
    
    LRTA* is an online search algorithm that:
    1. Moves to the neighbor minimizing c(s,a,s') + H(s') 
       where c = step cost, H = learned heuristic
    2. After moving, updates H(s) = max(H(s), min_neighbor(c + H(neighbor)))
       This is the "learning" step - H values improve over time.
    
    Unlike BFS/A*, LRTA* does NOT require a complete map - it explores online
    and learns from experience. Heuristic values are stored across steps.
    """

    def __init__(self):
        # Learned heuristic table H: position -> estimated cost to goal
        self.H: Dict[Tuple[int, int], float] = {}
        self.prev_pos = None

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]; bricks = info["bricks"]
        bombs = info["bombs"]; explosions = info["explosions"]
        enemies = info["enemies"]; items = info["items"]
        ammo = info["ammo"]; blast_radius = info["blast_radius"]
        width = info["width"]; height = info["height"]

        hazard_zones = get_hazard_zones(bombs, walls, bricks, blast_radius, width, height)
        bomb_positions = {(bx,by) for bx,by,_ in bombs}

        # Safety override
        if (px,py) in hazard_zones or (px,py) in explosions:
            return bfs_escape((px,py), walls, bricks, bombs, explosions, hazard_zones, width, height)

        # Bomb placement
        if ammo > 0 and (px,py) not in bomb_positions:
            near_target = any(
                (px+dx,py+dy) in bricks or any((px+dx)==ex and (py+dy)==ey for ex,ey in enemies)
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]
            )
            if near_target:
                sim_bombs = bombs + [(px,py,4)]
                sim_hazard = get_hazard_zones(sim_bombs, walls, bricks, blast_radius, width, height)
                if bfs_escape((px,py), walls, bricks, sim_bombs, explosions, sim_hazard, width, height) != "WAIT":
                    return "BOMB"

        # Initialize H for current position if not seen
        cur = (px, py)
        if cur not in self.H:
            self.H[cur] = initial_heuristic(cur, enemies, items, bricks, ammo, width, height)

        # LRTA* step: enumerate neighbors
        neighbors = []
        moves_map = [("UP",0,-1),("DOWN",0,1),("LEFT",-1,0),("RIGHT",1,0)]
        for action, dx, dy in moves_map:
            nx, ny = px+dx, py+dy
            if not (0<=nx<width and 0<=ny<height): continue
            if (nx,ny) in walls or (nx,ny) in bricks: continue
            if (nx,ny) in bomb_positions: continue
            if (nx,ny) in explosions: continue
            if (nx,ny) in hazard_zones and hazard_zones[(nx,ny)] <= 1: continue

            npos = (nx,ny)
            if npos not in self.H:
                self.H[npos] = initial_heuristic(npos, enemies, items, bricks, ammo, width, height)

            # Danger cost adjustment
            danger_cost = 0
            if npos in hazard_zones:
                danger_cost = (4 - hazard_zones[npos]) * 2

            cost = 1 + danger_cost + self.H[npos]  # c(s,a,s') + H(s')
            neighbors.append((cost, action, npos))

        if not neighbors:
            return "WAIT"

        # LRTA* learning update: H(s) = max(H(s), min c+H over neighbors)
        min_cost = min(c for c, _, _ in neighbors)
        self.H[cur] = max(self.H[cur], min_cost)

        # Move to neighbor with minimum c + H
        neighbors.sort(key=lambda x: x[0])
        _, best_action, _ = neighbors[0]

        self.prev_pos = cur
        return best_action
