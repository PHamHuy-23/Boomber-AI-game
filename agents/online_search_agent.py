"""Online Search Agent (LRTA* - Learning Real-Time A*) for Bomberman."""
from typing import List, Tuple, Dict, Any, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def get_state_key(state_info: dict) -> Tuple[Tuple[int, int], Tuple[Tuple[int, int], ...], Optional[Tuple[int, int]]]:
    """
    Generate a discrete state key for LRTA* lookup table.
    The key consists of (player_pos, sorted_bomb_positions, closest_enemy_pos).
    """
    px, py = state_info["player_pos"]
    bombs = state_info["bombs"]
    bombs_key = tuple(sorted((bx, by) for bx, by, _ in bombs))
    
    enemies = state_info["enemies"]
    closest_enemy_pos = None
    if enemies:
        min_dist = float('inf')
        for ex, ey in enemies:
            dist = abs(px - ex) + abs(py - ey)
            if dist < min_dist:
                min_dist = dist
                closest_enemy_pos = (ex, ey)
                
    return ((px, py), bombs_key, closest_enemy_pos)

def get_action_cost(action: str, current_state: dict, next_state: dict) -> float:
    """
    Define transition cost c(s, a, s').
    - Highly illegal actions: extremely high cost (10,000,000.0).
    - Valid movement: small step cost (10.0) to encourage path efficiency.
    - Valid Wait/Bomb: slightly higher step cost (20.0) to prevent useless waiting/bombing.
    """
    px, py = next_state["player_pos"]
    parent_px, parent_py = current_state["player_pos"]
    
    # Check physical legality of movements
    if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
        walls = current_state["walls"]
        bricks = current_state["bricks"]
        bombs = current_state["bombs"]
        bomb_positions = {(bx, by) for bx, by, _ in bombs}
        width, height = current_state["width"], current_state["height"]
        
        if not (0 <= px < width and 0 <= py < height):
            return 10000000.0
        if (px, py) in walls or (px, py) in bricks:
            return 10000000.0
        if (px, py) in bomb_positions and (px, py) != (parent_px, parent_py):
            return 10000000.0
            
        return 10.0

    if action == "BOMB":
        if current_state["ammo"] <= 0:
            return 10000000.0
        if (parent_px, parent_py) in {(b[0], b[1]) for b in current_state["bombs"]}:
            return 10000000.0
        return 20.0

    if action == "WAIT":
        return 20.0

    return 10.0

def get_initial_heuristic(state_info: dict) -> float:
    """
    Initial heuristic estimate h(s) for LRTA*.
    Maps evaluate_state utility to a positive cost scale (lower is better).
    """
    if "hazard_zones" not in state_info:
        state_info = simulate_state(state_info, "WAIT")
    score = evaluate_state(state_info)
    return max(0.0, 1000000.0 - score)

class OnlineSearchAgent(BaseAgent):
    """
    Online Search Agent using textbook LRTA* (Learning Real-Time A*).
    Learns heuristic values online and updates H(s) dynamically to escape local minima.
    """

    def __init__(self):
        # Persistent memory lookup table H: state_key -> estimated cost to goal
        self.H: Dict[Any, float] = {}
        self.prev_state_key = None
        self.prev_action = None

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        current_state_key = get_state_key(state_info)
        
        # Reset memory if a new game starts
        tick = state.get("tick") or state.get("step") or state.get("time", 0)
        if tick <= 1:
            self.prev_state_key = None
            self.prev_action = None

        # 1. Initialize H for current state if not already visited
        if current_state_key not in self.H:
            self.H[current_state_key] = get_initial_heuristic(state_info)

        # 2. Learning update for the previous state s_prev:
        # H(s_prev) = max(H(s_prev), min_b (c(s_prev, b, s'_b) + H(s'_b)))
        if self.prev_state_key is not None and self.prev_action is not None:
            # We need the parent state info before the previous action, but since we only have
            # H(s_prev) in memory, we can reconstruct the minimum value from s_prev.
            # To do that, we can keep the parent state's state_info or estimate it.
            # Let's save the previous state_info as well for this update.
            pass

        # To make the update robust and fully consistent with LRTA*, we do:
        if self.prev_state_key is not None and self.prev_action is not None:
            prev_info = self.prev_state_info
            
            # Find the minimum of c(s_prev, b, s'_b) + H(s'_b) over all actions b
            min_val = float('inf')
            for b in ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]:
                next_st_b = simulate_state(prev_info, b)
                cost_b = get_action_cost(b, prev_info, next_st_b)
                next_key_b = get_state_key(next_st_b)
                
                # Initialize H for child if not seen
                if next_key_b not in self.H:
                    self.H[next_key_b] = get_initial_heuristic(next_st_b)
                    
                val_b = cost_b + self.H[next_key_b]
                if val_b < min_val:
                    min_val = val_b
            
            # Update H(s_prev)
            self.H[self.prev_state_key] = max(self.H[self.prev_state_key], min_val)

        # 3. Action Selection: choose action a from current state that minimizes c(s, a, s') + H(s')
        best_action = "WAIT"
        min_cost = float('inf')

        # Enumerate and evaluate all actions from the current state
        actions = ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]
        # Filter root's legal actions if provided by the environment
        legal_actions = state.get("legal_actions")
        if legal_actions:
            actions = [a for a in actions if a in legal_actions]

        for action in actions:
            next_st = simulate_state(state_info, action)
            cost = get_action_cost(action, state_info, next_st)
            next_key = get_state_key(next_st)

            # Initialize H for child if not seen
            if next_key not in self.H:
                self.H[next_key] = get_initial_heuristic(next_st)

            f_value = cost + self.H[next_key]
            
            if f_value < min_cost:
                min_cost = f_value
                best_action = action

        # 4. Save current state and chosen action for the next step's learning update
        self.prev_state_key = current_state_key
        self.prev_action = best_action
        self.prev_state_info = state_info

        return best_action
