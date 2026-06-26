"""Min-Conflicts Agent (CSP Local Search) for Bomberman."""
import random
from typing import List, Tuple, Dict, Any
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def get_valid_actions_for_mc(st: dict) -> List[str]:
    """Get all physically valid actions for the player in the current state."""
    px, py = st["player_pos"]
    walls = st["walls"]
    bricks = st["bricks"]
    bombs = st["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = st["width"], st["height"]

    valid = ["WAIT"]
    moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
    for action, (dx, dy) in moves.items():
        nx, ny = px + dx, py + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid.append(action)

    if st["ammo"] > 0 and (px, py) not in bomb_positions:
        valid.append("BOMB")
    return valid

def get_conflicts_and_state(assignment: List[str], root_state: dict) -> Tuple[float, dict]:
    """
    Simulate the action assignment path and calculate the total number of conflicts.
    Also returns the final simulated state.
    """
    current_state = root_state
    total_conflicts = 0.0

    for idx, action in enumerate(assignment):
        # Resolve to WAIT if the action is physically impossible, counting as a conflict
        valid_actions = get_valid_actions_for_mc(current_state)
        resolved_action = action
        if action not in valid_actions:
            total_conflicts += 10.0
            resolved_action = "WAIT"

        next_state = simulate_state(current_state, resolved_action)
        px, py = next_state["player_pos"]

        # Safety conflicts at the simulated step
        if (px, py) in next_state["explosions"]:
            total_conflicts += 10.0

        hazard_zones = next_state.get("hazard_zones", {})
        if (px, py) in hazard_zones:
            timer = hazard_zones[(px, py)]
            if timer <= 1:
                total_conflicts += 10.0

        # Enemy collision conflict
        for ex, ey in next_state["enemies"]:
            if px == ex and py == ey:
                total_conflicts += 10.0

        current_state = next_state

    return total_conflicts, current_state

class MinConflictsAgent(BaseAgent):
    """
    Min-Conflicts Agent.
    Formulates Bomberman path planning as a CSP with 4 variables (actions for 4 steps).
    Uses Min-Conflicts local search to resolve conflicts, breaking ties with state evaluation.
    """

    def __init__(self, max_depth: int = 4, max_steps: int = 100):
        self.max_depth = max_depth
        self.max_steps = max_steps

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        
        # Domain of actions
        domain = ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]

        # Initial assignment: random physically valid path
        assignment = []
        curr = state_info
        for _ in range(self.max_depth):
            val_acts = get_valid_actions_for_mc(curr)
            act = random.choice(val_acts)
            assignment.append(act)
            curr = simulate_state(curr, act)
        
        best_assignment = list(assignment)
        best_conflicts, final_state = get_conflicts_and_state(assignment, state_info)
        best_score = evaluate_state(final_state)

        for step in range(self.max_steps):
            # Identify conflicted variables (steps where a conflict occurs)
            conflicted_vars = []
            current = state_info
            for i, action in enumerate(assignment):
                # Check physical consistency
                valid_acts = get_valid_actions_for_mc(current)
                resolved_act = action
                if action not in valid_acts:
                    conflicted_vars.append(i)
                    resolved_act = "WAIT"
                
                next_st = simulate_state(current, resolved_act)
                px, py = next_st["player_pos"]
                
                step_conflict = False
                if (px, py) in next_st["explosions"]:
                    step_conflict = True
                elif (px, py) in next_st.get("hazard_zones", {}) and next_st["hazard_zones"][(px, py)] <= 1:
                    step_conflict = True
                
                if step_conflict:
                    conflicted_vars.append(i)
                current = next_st

            if not conflicted_vars:
                # If no steps have conflicts, pick any variable at random to try and find higher score
                conflicted_vars = list(range(self.max_depth))

            # Select a conflicted variable at random
            var_idx = random.choice(conflicted_vars)

            # Find the value (action) that minimizes conflicts (break ties with evaluate_state score)
            best_val = assignment[var_idx]
            min_c = float('inf')
            max_s = -float('inf')

            # Shuffle domain to avoid directional bias
            random_domain = list(domain)
            random.shuffle(random_domain)

            for val in random_domain:
                assignment[var_idx] = val
                c, final_st = get_conflicts_and_state(assignment, state_info)
                s = evaluate_state(final_st)
                
                if c < min_c:
                    min_c = c
                    max_s = s
                    best_val = val
                elif c == min_c and s > max_s:
                    max_s = s
                    best_val = val

            # Reassign
            assignment[var_idx] = best_val

            # Keep track of the globally best assignment seen
            current_conflicts, final_st = get_conflicts_and_state(assignment, state_info)
            current_score = evaluate_state(final_st)

            if current_conflicts < best_conflicts:
                best_conflicts = current_conflicts
                best_score = current_score
                best_assignment = list(assignment)
            elif current_conflicts == best_conflicts and current_score > best_score:
                best_score = current_score
                best_assignment = list(assignment)

        # Make sure we return a physically valid action as fallback
        root_valid = get_valid_actions_for_mc(state_info)
        final_action = best_assignment[0]
        if final_action not in root_valid:
            final_action = "WAIT"
            
        return final_action
