"""Simulated Annealing Agent for Bomberman."""
import gc
import math
import random
from collections import deque
from typing import Tuple, Dict, Set, List
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state


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


def bfs_escape(start, walls, bricks, bombs, explosions, hazard_zones, width, height) -> str:
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


def should_place_bomb(pos, enemies, bricks, walls, blast_radius, width, height) -> bool:
    px, py = pos
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for dist in range(1, blast_radius + 1):
            tx, ty = px + dx * dist, py + dy * dist
            if not (0 <= tx < width and 0 <= ty < height):
                break
            if (tx, ty) in walls:
                break
            if any(tx == ex and ty == ey for ex, ey in enemies):
                return True
            if (tx, ty) in bricks:
                return True
    return False


class SimulatedAnnealingAgent(BaseAgent):
    """
    Simulated Annealing Agent.
    Like Hill Climbing but can accept WORSE moves with probability exp(-ΔE/T).
    Temperature T decreases each step (cooling schedule).
    This allows escaping local optima that Hill Climbing gets stuck in.
    
    Temperature starts high (lots of exploration) and decreases (more exploitation).
    """

    def __init__(self, initial_temp: float = 50.0, cooling_rate: float = 0.97, min_temp: float = 1.0):
        super().__init__()
        self.temperature = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]
        bricks = info["bricks"]
        bombs = info["bombs"]
        ammo = info["ammo"]
        width = info["width"]
        height = info["height"]

        bomb_positions = {(bx, by) for bx, by, _ in bombs}

        # --- Textbook SA: Search on state-space tree up to depth 4 ---
        root_sim = simulate_state(info, "WAIT")
        root_score = evaluate_state(root_sim)
        
        c_sim_state = info
        current_score = root_score
        current_path = []
        
        best_action = "WAIT"
        best_score = root_score
        
        temp = self.temperature
        num_iterations = 20
        depth_limit = 4
        
        for _ in range(num_iterations):
            # Reset to root if depth limit reached
            if len(current_path) >= depth_limit:
                c_sim_state = info
                current_score = root_score
                current_path = []
                
            # Generate valid actions from c_sim_state
            c_px, c_py = c_sim_state["player_pos"]
            c_walls = c_sim_state["walls"]
            c_bricks = c_sim_state["bricks"]
            c_bombs = c_sim_state["bombs"]
            c_ammo = c_sim_state["ammo"]
            c_width = c_sim_state["width"]
            c_height = c_sim_state["height"]
            
            c_bomb_positions = {(bx, by) for bx, by, _ in c_bombs}
            
            valid_actions = ["WAIT"]
            for action, dx, dy in [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]:
                nx, ny = c_px + dx, c_py + dy
                if 0 <= nx < c_width and 0 <= ny < c_height:
                    if (nx, ny) not in c_walls and (nx, ny) not in c_bricks:
                        if (nx, ny) not in c_bomb_positions or (nx, ny) == (c_px, c_py):
                            valid_actions.append(action)
            if c_ammo > 0 and (c_px, c_py) not in c_bomb_positions:
                valid_actions.append("BOMB")
                
            if not valid_actions:
                c_sim_state = info
                current_score = root_score
                current_path = []
                continue
                
            chosen_action = random.choice(valid_actions)
            neighbor_sim = simulate_state(c_sim_state, chosen_action)
            neighbor_score = evaluate_state(neighbor_sim)
            
            delta_e = neighbor_score - current_score
            accept = False
            if delta_e > 0:
                accept = True
            else:
                prob = math.exp(delta_e / max(temp, 0.001))
                accept = random.random() < prob
                
            if accept:
                c_sim_state = neighbor_sim
                current_score = neighbor_score
                current_path.append(chosen_action)
                if current_score > best_score:
                    best_score = current_score
                    best_action = current_path[0]
                    
            # Cool down
            temp = max(self.min_temp, temp * self.cooling_rate)
            
        return best_action
