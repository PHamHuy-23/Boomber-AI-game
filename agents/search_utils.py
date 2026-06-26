"""Shared search utilities for Bomberman agents.

This file contains the common state parser, simulator, and evaluator used by
all state-space search agents (Hill Climbing, Simulated Annealing, BFS, DFS, Greedy, A*).
"""
import gc
import random
from typing import Tuple, Dict, Set, List

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
    raw = state.get("enemies") or state.get("enemy_positions")
    if raw:
        for e in raw:
            if isinstance(e, dict):
                enemies.append((e.get('x'), e.get('y')))
            elif isinstance(e, (list, tuple)):
                enemies.append((e[0], e[1]))
            else:
                enemies.append((e.x, e.y))
    bombs = []
    raw = state.get("bombs") or state.get("bomb_positions")
    if raw:
        for b in raw:
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
    raw = state.get("items", {})
    if isinstance(raw, dict):
        for k, v in raw.items():
            if isinstance(k, (list, tuple)):
                items[tuple(k)] = v
    return {
        "player_pos": player_pos,
        "walls": walls,
        "bricks": bricks,
        "enemies": enemies,
        "bombs": bombs,
        "explosions": explosions,
        "items": items,
        "ammo": state.get("ammo", 1),
        "blast_radius": state.get("blast_radius", 2),
        "width": width,
        "height": height
    }

def get_hazard_zones(bombs, walls, bricks, blast_radius, width, height) -> Dict:
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

def simulate_state(info: dict, action: str) -> dict:
    px, py = info["player_pos"]
    walls = info["walls"]
    bricks = set(info["bricks"])
    enemies = list(info["enemies"])
    items = dict(info["items"])
    bombs = list(info["bombs"])
    explosions = set(info["explosions"])
    ammo = info["ammo"]
    blast_radius = info["blast_radius"]
    width = info["width"]
    height = info["height"]

    sim_player_pos = (px, py)
    sim_bombs = list(bombs)
    sim_ammo = ammo
    sim_bricks = set(bricks)
    sim_enemies = list(enemies)
    sim_items = dict(items)
    sim_explosions = set(explosions)

    # 1. Simulate Player action
    if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
        dx, dy = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}[action]
        sim_player_pos = (px + dx, py + dy)
        if sim_player_pos in sim_items:
            del sim_items[sim_player_pos]
    elif action == "BOMB":
        sim_bombs.append((px, py, 4))
        sim_ammo = ammo - 1

    # 2. Simulate countdown and explosion updates
    next_bombs = []
    bombed_this_turn = []
    for bx, by, timer in sim_bombs:
        if timer <= 1:
            bombed_this_turn.append((bx, by, blast_radius))
        else:
            next_bombs.append((bx, by, timer))

    sim_bombs = next_bombs

    bombs_dict = {(b[0], b[1]): b for b in sim_bombs}
    for bx, by, br in bombed_this_turn:
        bombs_dict[(bx, by)] = (bx, by, 0)

    while bombed_this_turn:
        bx, by, br = bombed_this_turn.pop(0)
        sim_explosions.add((bx, by))
        sim_enemies = [e for e in sim_enemies if not (e[0] == bx and e[1] == by)]

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for dist in range(1, br + 1):
                tx, ty = bx + dx * dist, by + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls:
                    break

                sim_explosions.add((tx, ty))

                if (tx, ty) in sim_bricks:
                    sim_bricks.discard((tx, ty))
                    if (tx, ty) in sim_items:
                        del sim_items[(tx, ty)]
                    break

                sim_enemies = [e for e in sim_enemies if not (e[0] == tx and e[1] == ty)]

                if (tx, ty) in bombs_dict:
                    match_bombs = [b for b in sim_bombs if b[0] == tx and b[1] == ty]
                    if match_bombs:
                        sim_bombs = [b for b in sim_bombs if not (b[0] == tx and b[1] == ty)]
                        bombed_this_turn.append((tx, ty, br))

    sim_hazard_zones = get_hazard_zones(sim_bombs, walls, sim_bricks, blast_radius, width, height)

    # 3. Calculate projections when action == "BOMB"
    projected_destroyed_bricks = set(info.get("projected_destroyed_bricks", []))
    projected_hit_enemies = set(info.get("projected_hit_enemies", []))
    bomb_efficiency_reward = info.get("bomb_efficiency_reward", 0.0)

    if action == "BOMB":
        other_bomb_positions = {(bx, by) for bx, by, _ in bombs}
        chained_bombs_count = 0
        new_projected_destroyed_bricks = set()
        new_projected_hit_enemies = set()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for dist in range(1, blast_radius + 1):
                tx, ty = px + dx * dist, py + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls:
                    break
                if (tx, ty) in sim_bricks:
                    new_projected_destroyed_bricks.add((tx, ty))
                    break
                if (tx, ty) in other_bomb_positions:
                    chained_bombs_count += 1
                for ex, ey in sim_enemies:
                    if ex == tx and ey == ty:
                        new_projected_hit_enemies.add((ex, ey))

        projected_destroyed_bricks.update(new_projected_destroyed_bricks)
        projected_hit_enemies.update(new_projected_hit_enemies)
        bomb_efficiency_reward += (
            len(new_projected_destroyed_bricks) * 200.0 +
            len(new_projected_hit_enemies) * 400.0 +
            chained_bombs_count * 150.0
        )

    return {
        "player_pos": sim_player_pos,
        "walls": walls,
        "bricks": sim_bricks,
        "enemies": sim_enemies,
        "bombs": sim_bombs,
        "explosions": sim_explosions,
        "items": sim_items,
        "ammo": sim_ammo,
        "blast_radius": blast_radius,
        "width": width,
        "height": height,
        "hazard_zones": sim_hazard_zones,
        "projected_destroyed_bricks": projected_destroyed_bricks,
        "projected_hit_enemies": projected_hit_enemies,
        "bomb_efficiency_reward": bomb_efficiency_reward
    }

def evaluate_state(sim_state: dict) -> float:
    pos = sim_state["player_pos"]
    hazard_zones = sim_state["hazard_zones"]
    explosions = sim_state["explosions"]
    walls = sim_state["walls"]
    bricks = sim_state["bricks"]
    bombs = sim_state["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width = sim_state["width"]
    height = sim_state["height"]
    enemies = sim_state["enemies"]
    items = sim_state["items"]
    ammo = sim_state["ammo"]
    blast_radius = sim_state["blast_radius"]

    projected_destroyed_bricks = sim_state.get("projected_destroyed_bricks", set())
    projected_hit_enemies = sim_state.get("projected_hit_enemies", set())
    bomb_efficiency_reward = sim_state.get("bomb_efficiency_reward", 0.0)

    score = 0.0

    # 1. Survival & Safety Heuristic
    if pos in explosions:
        return -1000000.0

    in_hazard = pos in hazard_zones
    if in_hazard:
        timer = hazard_zones[pos]
        if timer <= 1:
            return -500000.0
        score -= (5 - timer) * 150.0

    bomb_timers = {(bx, by): t for bx, by, t in bombs}
    if pos in bomb_positions:
        b_timer = bomb_timers.get(pos, 4)
        score -= (5 - b_timer) * 300.0

    safe_neighbors = 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions and (nx, ny) not in explosions:
                if (nx, ny) not in hazard_zones:
                    safe_neighbors += 1
    score += safe_neighbors * 200.0

    # 2. Escape Freedom (Degree / Mobility)
    reachable_neighbors = 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions and (nx, ny) not in explosions:
                reachable_neighbors += 1
    score += reachable_neighbors * 50.0

    escape_routes = 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions and (nx, ny) not in explosions:
                for ddx, ddy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nnx, nny = nx + ddx, ny + ddy
                    if (nnx, nny) == pos:
                        continue
                    if 0 <= nnx < width and 0 <= nny < height:
                        if (nnx, nny) not in walls and (nnx, nny) not in bricks and (nnx, nny) not in bomb_positions and (nnx, nny) not in explosions:
                            if (nnx, nny) not in hazard_zones:
                                escape_routes += 1
    score += escape_routes * 150.0

    # 3. Dead-end Penalty
    if reachable_neighbors == 0:
        score -= 400000.0

    # 4. Item Penalty & Proximity
    score -= len(items) * 1000.0
    if items:
        min_dist_item = min(abs(pos[0] - ix) + abs(pos[1] - iy) for ix, iy in items.keys())
        score += 600.0 / (min_dist_item + 1)

    # 5. Enemy Penalty & Proximity
    effective_enemies_count = len(enemies) - len(projected_hit_enemies)
    score -= effective_enemies_count * 3000.0
    if enemies:
        min_dist_enemy = min(abs(pos[0] - ex) + abs(pos[1] - ey) for ex, ey in enemies)
        if ammo > 0:
            score += 300.0 / (min_dist_enemy + 1)
            if min_dist_enemy <= 1:
                score += 100.0
        else:
            score -= 200.0 / (min_dist_enemy + 1)

    # 6. Brick Penalty & Proximity
    effective_bricks = set(bricks) - projected_destroyed_bricks
    score -= len(effective_bricks) * 500.0
    if bricks:
        min_dist_brick = min(abs(pos[0] - bx) + abs(pos[1] - by) for bx, by in bricks)
        score += 100.0 / (min_dist_brick + 1)
        if min_dist_brick == 1:
            score += 50.0

    # 7. Bomb Placement & Efficiency Reward
    score += bomb_efficiency_reward

    # 8. Center of Map Preference
    cx, cy = width / 2.0, height / 2.0
    dist_to_center = abs(pos[0] - cx) + abs(pos[1] - cy)
    score += 10.0 / (dist_to_center + 1)

    return score
