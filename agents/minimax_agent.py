"""Minimax agent implementation for Bomberman."""
import gc
import inspect
from typing import List, Tuple, Set, Dict, Any
from agents import BaseAgent
from environment.env import Action

def parse_state(state: dict) -> dict:
    """
    Parse the state dict with full compatibility for both local environment keys
    and the standard Kaggle/WandB representation.
    """
    # 1. Player Position
    player_pos = state.get("player_pos") or state.get("self_position")
    
    # 2. Map dimensions (default to standard 15x13)
    width, height = 15, 13
    board = state.get("board") or state.get("grid")
    if board is not None:
        height = len(board)
        width = len(board[0]) if height > 0 else 0
        
    walls = set()
    bricks = set()
    
    # If board or grid is present, parse it directly
    if board is not None:
        # standard: 0: empty, 1: wall, 2: brick, 3: bomb, 4: enemy
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
        # No board key -> we are running locally in pytest / benchmark.py
        # Try to find Environment in the garbage collector (extremely robust)
        try:
            env = None
            for obj in gc.get_objects():
                if obj.__class__.__name__ == 'Environment':
                    env = obj
                    break
            
            if env is None:
                # Fallback to inspect stack
                import inspect
                frame = inspect.currentframe()
                while frame:
                    locals_dict = frame.f_locals
                    if 'env' in locals_dict:
                        env = locals_dict['env']
                        if env.__class__.__name__ == 'Environment':
                            break
                    if 'self' in locals_dict:
                        self_obj = locals_dict['self']
                        if self_obj.__class__.__name__ == 'Environment':
                            env = self_obj
                            break
                    frame = frame.f_back
            
            if env is not None and env.map is not None:
                walls = set(env.map.walls)
                bricks = set(env.map.bricks)
                width = env.map.width
                height = env.map.height
            else:
                walls = set(state.get("walls", []))
        except Exception:
            walls = set(state.get("walls", []))
            
    # Default player position if not found
    if player_pos is None:
        player_pos = (1, 1)
        
    # 3. Enemies
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
                
    # 4. Bombs (list of tuples: (x, y, timer))
    bombs = []
    raw_bombs = state.get("bombs") or state.get("bomb_positions")
    if raw_bombs:
        for b in raw_bombs:
            if isinstance(b, dict):
                bombs.append((b.get('x'), b.get('y'), b.get('timer', 4)))
            elif isinstance(b, (list, tuple)):
                if len(b) >= 3:
                    bombs.append((b[0], b[1], b[2]))
                else:
                    bombs.append((b[0], b[1], 4))
            else:
                bombs.append((b.x, b.y, b.timer))
                
    # 5. Explosions
    explosions = set()
    raw_explosions = state.get("explosions", [])
    for exp in raw_explosions:
        if isinstance(exp, (list, tuple)):
            explosions.add((exp[0], exp[1]))
        elif isinstance(exp, dict):
            explosions.add((exp.get('x'), exp.get('y')))
            
    # 6. Items
    items = {}
    raw_items = state.get("items", {})
    if isinstance(raw_items, dict):
        for k, v in raw_items.items():
            if isinstance(k, (list, tuple)):
                items[k] = v
                
    # 7. Ammo and Blast Radius
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

def resolve_bomb_chain_reactions(bombs: List[Tuple[int, int, int]], walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], blast_radius: int, width: int = 15, height: int = 13) -> List[Tuple[int, int, int]]:
    bomb_timers = {(bx, by): timer for bx, by, timer in bombs}
    
    changed = True
    while changed:
        changed = False
        for (bx, by), timer in list(bomb_timers.items()):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                for dist in range(1, blast_radius + 1):
                    tx, ty = bx + dx * dist, by + dy * dist
                    if not (0 <= tx < width and 0 <= ty < height):
                        break
                    if (tx, ty) in walls:
                        break
                    if (tx, ty) in bomb_timers:
                        other_timer = bomb_timers[(tx, ty)]
                        if timer < other_timer:
                            bomb_timers[(tx, ty)] = timer
                            changed = True
                        break
                    if (tx, ty) in bricks:
                        break
                        
    return [(bx, by, timer) for (bx, by), timer in bomb_timers.items()]

def get_bomb_hazard_zones(bombs: List[Tuple[int, int, int]], walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], blast_radius: int, width: int = 15, height: int = 13) -> Dict[Tuple[int, int], int]:
    hazard_zones = {}
    for bx, by, timer in bombs:
        if (bx, by) not in hazard_zones or timer < hazard_zones[(bx, by)]:
            hazard_zones[(bx, by)] = timer
            
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            for dist in range(1, blast_radius + 1):
                tx, ty = bx + dx * dist, by + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls:
                    break
                if (tx, ty) not in hazard_zones or timer < hazard_zones[(tx, ty)]:
                    hazard_zones[(tx, ty)] = timer
                if (tx, ty) in bricks:
                    break
    return hazard_zones

def check_escape_path(start_pos: Tuple[int, int], walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], bombs: List[Tuple[int, int, int]], blast_radius: int, current_explosions: Set[Tuple[int, int]], width: int = 15, height: int = 13) -> bool:
    resolved_bombs = resolve_bomb_chain_reactions(bombs, walls, bricks, blast_radius, width, height)
    hazard_zones = get_bomb_hazard_zones(resolved_bombs, walls, bricks, blast_radius, width, height)
    
    if start_pos not in hazard_zones and start_pos not in current_explosions:
        return True
        
    queue = [(start_pos[0], start_pos[1], 0)]
    visited = {(start_pos[0], start_pos[1], 0)}
    bomb_positions = {(bx, by) for bx, by, _ in resolved_bombs}
    
    max_bfs_steps = 15
    while queue:
        cx, cy, t = queue.pop(0)
        
        if t > max_bfs_steps:
            continue
            
        if (cx, cy) not in hazard_zones and (cx, cy) not in current_explosions:
            return True
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if (nx, ny) in walls or (nx, ny) in bricks:
                continue
            if (nx, ny) in bomb_positions and (nx, ny) != start_pos:
                continue
            if (nx, ny) in current_explosions:
                continue
                
            if (nx, ny) in hazard_zones and hazard_zones[(nx, ny)] <= t + 1:
                continue
                
            if (nx, ny, t + 1) not in visited:
                visited.add((nx, ny, t + 1))
                queue.append((nx, ny, t + 1))
                
    return False

def bfs_shortest_path_distance(start: Tuple[int, int], targets: Set[Tuple[int, int]], walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], bombs: List[Tuple[int, int, int]] = None, width: int = 15, height: int = 13) -> float:
    if not targets:
        return float('inf')
    if start in targets:
        return 0.0
        
    queue = [(start[0], start[1], 0)]
    visited = {start}
    bomb_positions = {(bx, by) for bx, by, _ in bombs} if bombs else set()
    
    while queue:
        cx, cy, dist = queue.pop(0)
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) in targets:
                    return float(dist + 1)
                if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))
    return float('inf')

def heuristic_evaluate(pos: Tuple[int, int], state_info: dict, placed_bomb: Tuple[int, int, int] = None) -> float:
    px, py = pos
    width, height = state_info["width"], state_info["height"]
    
    # 1. Base check: is it in active explosion or touching enemy?
    if pos in state_info["explosions"]:
        return -100000.0
        
    for ex, ey in state_info["enemies"]:
        if px == ex and py == ey:
            return -100000.0
            
    # 2. Check escape path
    bombs_to_check = list(state_info["bombs"])
    if placed_bomb:
        bombs_to_check.append(placed_bomb)
        
    if not check_escape_path(pos, state_info["walls"], state_info["bricks"], bombs_to_check, state_info["blast_radius"], state_info["explosions"], width, height):
        return -80000.0
        
    # 3. Penalty for being in hazard zone (even if there is an escape path)
    resolved_bombs = resolve_bomb_chain_reactions(bombs_to_check, state_info["walls"], state_info["bricks"], state_info["blast_radius"], width, height)
    hazard_zones = get_bomb_hazard_zones(resolved_bombs, state_info["walls"], state_info["bricks"], state_info["blast_radius"], width, height)
    
    score = 0.0
    
    if pos in hazard_zones:
        timer = hazard_zones[pos]
        score -= (5.0 - timer) * 150.0
        
    # 4. Enemy proximity penalty
    min_enemy_dist = float('inf')
    for ex, ey in state_info["enemies"]:
        dist = abs(px - ex) + abs(py - ey)
        if dist < min_enemy_dist:
            min_enemy_dist = dist
            
    if min_enemy_dist == 1:
        score -= 3000.0
    elif min_enemy_dist == 2:
        score -= 300.0
    elif min_enemy_dist == 3:
        score -= 30.0
        
    # 5. Item proximity bonus
    if state_info["items"]:
        item_targets = set(state_info["items"].keys())
        dist = bfs_shortest_path_distance(pos, item_targets, state_info["walls"], state_info["bricks"], bombs_to_check, width, height)
        if dist != float('inf'):
            score += 1500.0 / (dist + 1)
            
    # 6. Brick proximity bonus
    if state_info["bricks"]:
        brick_targets = set()
        for bx, by in state_info["bricks"]:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tx, ty = bx + dx, by + dy
                if 0 <= tx < width and 0 <= ty < height and (tx, ty) not in state_info["walls"] and (tx, ty) not in state_info["bricks"]:
                    brick_targets.add((tx, ty))
                    
        dist = bfs_shortest_path_distance(pos, brick_targets, state_info["walls"], state_info["bricks"], bombs_to_check, width, height)
        if dist != float('inf'):
            score += 300.0 / (dist + 1)
            
    # 7. Enemy proximity / hunt bonus if no bricks are left
    if state_info["enemies"]:
        enemy_targets = set()
        for ex, ey in state_info["enemies"]:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tx, ty = ex + dx, ey + dy
                if 0 <= tx < width and 0 <= ty < height and (tx, ty) not in state_info["walls"] and (tx, ty) not in state_info["bricks"]:
                    enemy_targets.add((tx, ty))
                    
        dist = bfs_shortest_path_distance(pos, enemy_targets, state_info["walls"], state_info["bricks"], bombs_to_check, width, height)
        if dist != float('inf'):
            if not state_info["bricks"]:
                score += 800.0 / (dist + 1)
            else:
                if state_info["ammo"] > 0:
                    score += 100.0 / (dist + 1)
                else:
                    score -= 50.0 / (dist + 1)
                    
    return score

def simulate_state_forward(state_info: dict, player_action: str, step: int = 1) -> dict:
    next_state = {
        "player_pos": state_info["player_pos"],
        "walls": state_info["walls"],
        "bricks": state_info["bricks"],
        "enemies": list(state_info["enemies"]),
        "bombs": list(state_info["bombs"]),
        "explosions": set(state_info["explosions"]),
        "items": dict(state_info["items"]),
        "ammo": state_info["ammo"],
        "blast_radius": state_info["blast_radius"],
        "width": state_info["width"],
        "height": state_info["height"]
    }
    
    px, py = next_state["player_pos"]
    
    # 1. Player move
    if player_action == "UP":
        ny = py - 1
        if (px, ny) not in next_state["walls"] and (px, ny) not in next_state["bricks"] and (px, ny) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["player_pos"] = (px, ny)
    elif player_action == "DOWN":
        ny = py + 1
        if (px, ny) not in next_state["walls"] and (px, ny) not in next_state["bricks"] and (px, ny) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["player_pos"] = (px, ny)
    elif player_action == "LEFT":
        nx = px - 1
        if (nx, py) not in next_state["walls"] and (nx, py) not in next_state["bricks"] and (nx, py) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["player_pos"] = (nx, py)
    elif player_action == "RIGHT":
        nx = px + 1
        if (nx, py) not in next_state["walls"] and (nx, py) not in next_state["bricks"] and (nx, py) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["player_pos"] = (nx, py)
    elif player_action == "BOMB":
        if next_state["ammo"] > 0 and (px, py) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["bombs"].append((px, py, 4))
            next_state["ammo"] -= 1
            
    # 2. Tick bombs
    new_bombs = []
    exploded_bombs = []
    for bx, by, timer in next_state["bombs"]:
        if timer <= 1:
            exploded_bombs.append((bx, by))
        else:
            new_bombs.append((bx, by, timer - 1))
            
    next_state["bombs"] = new_bombs
    
    # Detonate exploded bombs
    if exploded_bombs:
        resolved_exploded = resolve_bomb_chain_reactions(
            [(bx, by, 0) for bx, by in exploded_bombs],
            next_state["walls"],
            next_state["bricks"],
            next_state["blast_radius"],
            next_state["width"],
            next_state["height"]
        )
        hazard = get_bomb_hazard_zones(resolved_exploded, next_state["walls"], next_state["bricks"], next_state["blast_radius"], next_state["width"], next_state["height"])
        next_state["explosions"] = set(hazard.keys())
        next_state["bricks"] = next_state["bricks"] - next_state["explosions"]
    else:
        if step == 1:
            # Keep original active explosions for step 1 as they take 2 ticks to clear
            next_state["explosions"] = set(state_info["explosions"])
        else:
            next_state["explosions"] = set()
        
    return next_state

class MinimaxAgent(BaseAgent):
    """An agent that uses Minimax search with heuristic lookahead to choose actions."""

    def __init__(self, depth: int = 2):
        """
        Initialize MinimaxAgent.

        Args:
            depth (int): Depth of search tree.
        """
        self.depth = depth

    def choose_action(self, state: dict) -> str:
        """
        Choose the best action using depth-2 lookahead heuristic search.
        """
        state_info = parse_state(state)
        
        legal_actions = state.get("legal_actions")
        if not legal_actions:
            legal_actions = ["UP", "DOWN", "LEFT", "RIGHT", "BOMB", "WAIT"]
            
        best_action = "WAIT"
        best_score = -float('inf')
        
        fallback_action = "WAIT"
        fallback_score = -float('inf')
        
        for action1 in legal_actions:
            px, py = state_info["player_pos"]
            
            # Prune impossible moves
            if action1 == "UP" and (px, py - 1) in state_info["walls"] | state_info["bricks"]:
                continue
            if action1 == "DOWN" and (px, py + 1) in state_info["walls"] | state_info["bricks"]:
                continue
            if action1 == "LEFT" and (px - 1, py) in state_info["walls"] | state_info["bricks"]:
                continue
            if action1 == "RIGHT" and (px + 1, py) in state_info["walls"] | state_info["bricks"]:
                continue
            if action1 == "BOMB":
                if state_info["ammo"] <= 0:
                    continue
                if (px, py) in {(b[0], b[1]) for b in state_info["bombs"]}:
                    continue
                    
            state_info_1 = simulate_state_forward(state_info, action1, step=1)
            score_1 = heuristic_evaluate(state_info_1["player_pos"], state_info_1)
            
            # Update fallback safest action
            if score_1 > fallback_score:
                fallback_score = score_1
                fallback_action = action1
                
            # If step-1 is already deadly/trapped, prune search tree
            if score_1 <= -50000.0:
                continue
                
            # Lookahead step 2
            max_score_2 = -float('inf')
            
            for action2 in ["UP", "DOWN", "LEFT", "RIGHT", "BOMB", "WAIT"]:
                px1, py1 = state_info_1["player_pos"]
                if action2 == "UP" and (px1, py1 - 1) in state_info_1["walls"] | state_info_1["bricks"]:
                    continue
                if action2 == "DOWN" and (px1, py1 + 1) in state_info_1["walls"] | state_info_1["bricks"]:
                    continue
                if action2 == "LEFT" and (px1 - 1, py1) in state_info_1["walls"] | state_info_1["bricks"]:
                    continue
                if action2 == "RIGHT" and (px1 + 1, py1) in state_info_1["walls"] | state_info_1["bricks"]:
                    continue
                if action2 == "BOMB":
                    if state_info_1["ammo"] <= 0:
                        continue
                    if (px1, py1) in {(b[0], b[1]) for b in state_info_1["bombs"]}:
                        continue
                        
                state_info_2 = simulate_state_forward(state_info_1, action2, step=2)
                score = heuristic_evaluate(state_info_2["player_pos"], state_info_2)
                
                # Reward useful bomb placement at step 1
                if action1 == "BOMB":
                    is_next_to_brick = any((px + dx, py + dy) in state_info["bricks"] for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)])
                    is_next_to_enemy = any(abs(px - ex) + abs(py - ey) <= 2 for ex, ey in state_info["enemies"])
                    if is_next_to_brick or is_next_to_enemy:
                        score += 3500.0
                    else:
                        score -= 800.0
                        
                if score > max_score_2:
                    max_score_2 = score
                    
            if max_score_2 == -float('inf'):
                max_score_2 = score_1
                
            if max_score_2 > best_score:
                best_score = max_score_2
                best_action = action1
                
        # Fallback to the safest action if everything at step 2 is deadly/trapped
        if best_score <= -50000.0:
            return fallback_action
            
        return best_action
