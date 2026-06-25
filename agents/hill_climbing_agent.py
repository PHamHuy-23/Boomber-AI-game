"""Hill Climbing Agent for Bomberman."""
import gc
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


def evaluate_position(pos, enemies, items, bricks, hazard_zones, explosions,
                      ammo, blast_radius, width, height) -> float:
    """
    Heuristic score for a position.
    Hill Climbing picks the neighbor with the highest score.
    """
    px, py = pos
    score = 0.0

    # Hard penalty for dangerous tiles
    if pos in explosions:
        return -100000.0
    if pos in hazard_zones:
        timer = hazard_zones[pos]
        score -= (5 - timer) * 300.0

    # Reward for being near items
    for ix, iy in items.keys():
        dist = abs(px-ix) + abs(py-iy)
        score += 800.0 / (dist + 1)

    # Reward for being near enemies
    for ex, ey in enemies:
        dist = abs(px-ex) + abs(py-ey)
        if ammo > 0:
            score += 400.0 / (dist + 1)
        else:
            score -= 200.0 / (dist + 1)

    # Reward for being adjacent to bricks
    for bx, by in bricks:
        dist = abs(px-bx) + abs(py-by)
        if dist == 1:
            score += 100.0

    return score


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


class HillClimbingAgent(BaseAgent):
    """
    Hill Climbing Agent - Local search that always moves to the neighbor
    with the highest heuristic score (steepest ascent hill climbing).
    Makes greedy local decisions - no lookahead beyond immediate neighbors.
    Can get stuck at local maxima (plateau handling: falls back to random restart).
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

        # PRIORITY 1: Escape danger
        if (px,py) in hazard_zones or (px,py) in explosions:
            return bfs_escape((px,py), walls, bricks, bombs, explosions, hazard_zones, width, height)

        # PRIORITY 2: Place bomb if strategically good
        if ammo > 0 and (px,py) not in bomb_positions:
            if should_place_bomb((px,py), enemies, bricks, walls, blast_radius, width, height):
                sim_bombs = bombs + [(px,py,4)]
                sim_hazard = get_hazard_zones(sim_bombs, walls, bricks, blast_radius, width, height)
                if bfs_escape((px,py), walls, bricks, sim_bombs, explosions, sim_hazard, width, height) != "WAIT":
                    return "BOMB"

        # PRIORITY 3: Hill Climbing - find best immediate neighbor
        current_score = evaluate_position(
            (px,py), enemies, items, bricks, hazard_zones, explosions,
            ammo, blast_radius, width, height
        )

        best_score = current_score
        best_action = "WAIT"

        moves = [("UP", 0,-1), ("DOWN", 0,1), ("LEFT",-1,0), ("RIGHT",1,0)]
        for action, dx, dy in moves:
            nx, ny = px+dx, py+dy
            if not (0<=nx<width and 0<=ny<height): continue
            if (nx,ny) in walls or (nx,ny) in bricks: continue
            if (nx,ny) in bomb_positions: continue
            if (nx,ny) in explosions: continue

            score = evaluate_position(
                (nx,ny), enemies, items, bricks, hazard_zones, explosions,
                ammo, blast_radius, width, height
            )
            if score > best_score:
                best_score = score
                best_action = action

        # If no improvement (local maximum or plateau), try to explore
        # Simple random restart: pick any valid non-dangerous neighbor
        if best_action == "WAIT" and best_score == current_score:
            import random
            valid = []
            for action, dx, dy in moves:
                nx, ny = px+dx, py+dy
                if 0<=nx<width and 0<=ny<height and (nx,ny) not in walls and \
                   (nx,ny) not in bricks and (nx,ny) not in bomb_positions and \
                   (nx,ny) not in explosions and \
                   ((nx,ny) not in hazard_zones or hazard_zones[(nx,ny)] > 2):
                    valid.append(action)
            if valid:
                best_action = random.choice(valid)

        return best_action
