"""Min-Conflicts Agent (CSP) for Bomberman."""
import gc
import random
from collections import deque
from typing import Tuple, Dict, Set, List
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


def count_conflicts(pos, hazard_zones, explosions, enemies, walls, bricks,
                    bomb_positions, width, height) -> int:
    """
    Count the number of CONSTRAINTS violated by placing the agent at `pos`.
    
    CSP Constraints:
    1. Must not be in active explosion (hard)
    2. Must not be on a wall or brick (hard)
    3. Must not be at enemy position (hard)
    4. Should not be in bomb hazard zone (soft - weighted by urgency)
    5. Must not be on bomb (hard)
    6. Should be reachable (soft)
    """
    conflicts = 0
    px, py = pos

    # Hard constraints
    if pos in explosions: conflicts += 1000
    if pos in walls or pos in bricks: conflicts += 1000
    if any(px==ex and py==ey for ex,ey in enemies): conflicts += 1000
    if pos in bomb_positions: conflicts += 500

    # Soft constraint: hazard zone
    if pos in hazard_zones:
        timer = hazard_zones[pos]
        conflicts += max(0, (4 - timer)) * 50  # More urgent = more conflicts

    # Boundary check
    if not (0 <= px < width and 0 <= py < height):
        conflicts += 1000

    return conflicts


def strategic_value(pos, enemies, items, bricks, ammo, width, height) -> float:
    """How strategically valuable is this position (negative = we want to minimize conflicts)."""
    px, py = pos
    value = 0.0

    for ix, iy in items.keys():
        dist = abs(px-ix)+abs(py-iy)
        value += 500.0/(dist+1)

    for ex, ey in enemies:
        dist = abs(px-ex)+abs(py-ey)
        if ammo > 0: value += 300.0/(dist+1)
        else: value -= 200.0/(dist+1)

    for bx, by in bricks:
        if abs(px-bx)+abs(py-by) == 1:
            value += 80.0

    return value


class MinConflictsAgent(BaseAgent):
    """
    Min-Conflicts Agent (CSP approach).
    
    Models the Bomberman navigation as a Constraint Satisfaction Problem:
    - Variable: player's next position
    - Domain: all reachable adjacent positions
    - Constraints: avoid explosions, hazard zones, walls, enemies
    
    At each step, selects the action (position) that MINIMIZES violated constraints.
    When conflicts are equal, uses strategic value as tiebreaker.
    Naturally handles multiple competing objectives as constraint weights.
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
        bomb_positions = {(bx,by) for bx,by,_ in bombs}

        # Hard override: escape
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

        # Generate candidate positions (domain of the variable)
        # Domain includes: current position (WAIT) + 4 neighbors
        candidates = []
        moves = [("WAIT",0,0),("UP",0,-1),("DOWN",0,1),("LEFT",-1,0),("RIGHT",1,0)]

        for action, dx, dy in moves:
            nx, ny = px+dx, py+dy
            if action == "WAIT": nx, ny = px, py
            if not (0<=nx<width and 0<=ny<height): continue
            if (nx,ny) in walls or (nx,ny) in bricks: continue
            if (nx,ny) in bomb_positions and (nx,ny) != (px,py): continue

            # Count constraint violations for this position
            conflicts = count_conflicts(
                (nx,ny), hazard_zones, explosions, enemies,
                walls, bricks, bomb_positions, width, height
            )

            # Strategic value as tiebreaker (higher is better)
            value = strategic_value((nx,ny), enemies, items, bricks, ammo, width, height)

            candidates.append((conflicts, -value, action))  # minimize conflicts, maximize value

        if not candidates:
            return "WAIT"

        # Sort: first by conflicts (ascending), then by -value (descending strategic value)
        candidates.sort(key=lambda x: (x[0], x[1]))

        # Min-conflicts: pick the candidate with fewest violations
        best_conflicts = candidates[0][0]
        tied = [c for c in candidates if c[0] == best_conflicts]

        # Among ties, pick highest strategic value
        _, _, best_action = min(tied, key=lambda x: x[1])

        return best_action
