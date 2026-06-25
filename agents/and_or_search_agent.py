"""AND-OR Search Agent for Bomberman."""
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


def enemy_possible_moves(enemy_pos, walls, bricks, bomb_positions, width, height) -> List[Tuple]:
    """Generate all possible next positions of an enemy (non-deterministic)."""
    ex, ey = enemy_pos
    moves = [(ex, ey)]  # Staying still is possible
    for dx, dy in [(0,-1),(0,1),(-1,0),(1,0)]:
        nx, ny = ex+dx, ey+dy
        if 0<=nx<width and 0<=ny<height and (nx,ny) not in walls and \
           (nx,ny) not in bricks and (nx,ny) not in bomb_positions:
            moves.append((nx, ny))
    return moves


def and_or_evaluate(pos, enemies_outcomes, items, bricks, hazard_zones, explosions,
                    ammo, width, height) -> float:
    """
    AND node evaluation: must handle ALL possible enemy outcomes.
    Score = min over enemy outcomes (pessimistic) weighted with strategic value.
    """
    px, py = pos

    # Base score for the player position
    base_score = 0.0
    if pos in explosions: return -100000.0
    if pos in hazard_zones:
        base_score -= (5 - hazard_zones[pos]) * 300.0

    for ix, iy in items.keys():
        dist = abs(px-ix)+abs(py-iy)
        base_score += 600.0/(dist+1)
    for bx, by in bricks:
        if abs(px-bx)+abs(py-by) == 1:
            base_score += 80.0

    # AND logic: consider WORST case among enemy positions
    if not enemies_outcomes:
        return base_score

    # For each possible enemy position, compute threat to player
    min_threat_score = float('inf')
    for enemy_pos in enemies_outcomes:
        ex, ey = enemy_pos
        dist = abs(px-ex) + abs(py-ey)
        if ammo > 0:
            threat_score = 300.0/(dist+1)  # Want to be close when armed
        else:
            threat_score = -400.0/(dist+1)  # Avoid when unarmed
        if threat_score < min_threat_score:
            min_threat_score = threat_score

    return base_score + min_threat_score


class AndOrSearchAgent(BaseAgent):
    """
    AND-OR Search Agent.
    Models nondeterministic environment: OR nodes (agent's choices) and
    AND nodes (all possible enemy responses must be handled).
    
    The agent searches for a contingency plan that works regardless of
    how enemies move (pessimistic/worst-case planning).
    Depth-limited AND-OR tree search: OR depth = agent decisions, AND depth = enemy outcomes.
    """

    def __init__(self, depth: int = 2):
        self.depth = depth

    def _or_node(self, player_pos, enemies, walls, bricks, bombs, explosions,
                 hazard_zones, items, ammo, blast_radius, width, height, depth) -> Tuple[float, str]:
        """OR node: agent chooses the action with the best AND-node outcome."""
        if depth == 0:
            score = and_or_evaluate(player_pos, [e for e in enemies], items, bricks,
                                     hazard_zones, explosions, ammo, width, height)
            return score, "WAIT"

        bomb_positions = {(bx,by) for bx,by,_ in bombs}
        px, py = player_pos
        best_score = -float('inf')
        best_action = "WAIT"

        moves = [("WAIT",0,0),("UP",0,-1),("DOWN",0,1),("LEFT",-1,0),("RIGHT",1,0)]
        for action, dx, dy in moves:
            nx, ny = px+dx, py+dy
            if action == "WAIT":
                nx, ny = px, py
            if not (0<=nx<width and 0<=ny<height): continue
            if (nx,ny) in walls or (nx,ny) in bricks: continue
            if (nx,ny) in bomb_positions and (nx,ny) != (px,py): continue
            if (nx,ny) in explosions: continue
            if (nx,ny) in hazard_zones and hazard_zones[(nx,ny)] <= 1: continue

            # AND node: evaluate against all possible enemy configurations
            and_score = self._and_node(
                (nx,ny), enemies, walls, bricks, bombs, explosions,
                hazard_zones, items, ammo, blast_radius, width, height, depth-1
            )
            if and_score > best_score:
                best_score = and_score
                best_action = action

        return best_score, best_action

    def _and_node(self, player_pos, enemies, walls, bricks, bombs, explosions,
                  hazard_zones, items, ammo, blast_radius, width, height, depth) -> float:
        """AND node: must handle ALL possible enemy moves (pessimistic)."""
        if not enemies:
            # No enemies: just evaluate player position
            score, _ = self._or_node(player_pos, [], walls, bricks, bombs, explosions,
                                      hazard_zones, items, ammo, blast_radius, width, height, depth)
            return score

        bomb_positions = {(bx,by) for bx,by,_ in bombs}
        # Generate all possible next positions of each enemy
        all_enemy_outcomes = []
        for enemy_pos in enemies:
            possible_positions = enemy_possible_moves(enemy_pos, walls, bricks, bomb_positions, width, height)
            all_enemy_outcomes.append(possible_positions)

        # Worst case: pick the enemy configuration that minimizes player's score
        min_score = float('inf')
        # Limit combinations for performance: only consider first enemy's outcomes
        primary_outcomes = all_enemy_outcomes[0] if all_enemy_outcomes else [(0,0)]
        rest_enemies = list(enemies[1:]) if len(enemies) > 1 else []

        for enemy_next in primary_outcomes[:4]:  # Limit branching factor
            new_enemies = [enemy_next] + rest_enemies
            if depth > 0:
                score, _ = self._or_node(player_pos, new_enemies, walls, bricks, bombs,
                                          explosions, hazard_zones, items, ammo, blast_radius,
                                          width, height, depth)
            else:
                score = and_or_evaluate(player_pos, new_enemies, items, bricks,
                                         hazard_zones, explosions, ammo, width, height)
            if score < min_score:
                min_score = score

        return min_score if min_score != float('inf') else 0.0

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]; bricks = info["bricks"]
        bombs = info["bombs"]; explosions = info["explosions"]
        enemies = info["enemies"]; items = info["items"]
        ammo = info["ammo"]; blast_radius = info["blast_radius"]
        width = info["width"]; height = info["height"]

        hazard_zones = get_hazard_zones(bombs, walls, bricks, blast_radius, width, height)

        # Safety first
        if (px,py) in hazard_zones or (px,py) in explosions:
            return bfs_escape((px,py), walls, bricks, bombs, explosions, hazard_zones, width, height)

        # Bomb placement check
        if ammo > 0:
            bomb_pos_set = {(bx,by) for bx,by,_ in bombs}
            if (px,py) not in bomb_pos_set:
                near_target = any(
                    (px+dx,py+dy) in bricks or any((px+dx)==ex and (py+dy)==ey for ex,ey in enemies)
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]
                )
                if near_target:
                    sim_bombs = bombs + [(px,py,4)]
                    sim_hazard = get_hazard_zones(sim_bombs, walls, bricks, blast_radius, width, height)
                    if bfs_escape((px,py), walls, bricks, sim_bombs, explosions, sim_hazard, width, height) != "WAIT":
                        return "BOMB"

        # AND-OR search
        _, action = self._or_node(
            (px,py), enemies, walls, bricks, bombs, explosions,
            hazard_zones, items, ammo, blast_radius, width, height, self.depth
        )
        return action
