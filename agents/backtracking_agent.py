"""Backtracking Agent for Bomberman using CSP path planning."""
from typing import List, Tuple, Dict, Any, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def is_step_consistent(parent_state: dict, next_state: dict, action: str, step_idx: int) -> bool:
    """
    Check if the transition from parent_state to next_state via action satisfies CSP constraints.
    - Physical constraint: cannot walk into walls/bricks/bombs, cannot place bomb without ammo.
    - Safety constraint: player cannot land in active explosions or urgent hazard zones.
    """
    px, py = next_state["player_pos"]
    parent_px, parent_py = parent_state["player_pos"]
    walls = parent_state["walls"]
    bricks = parent_state["bricks"]
    bombs = parent_state["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = parent_state["width"], parent_state["height"]

    # 1. Physical boundaries & obstacles constraint
    if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
        if not (0 <= px < width and 0 <= py < height):
            return False
        # Cannot walk into walls, bricks or existing bombs (except the starting position at root step)
        if (px, py) in walls or (px, py) in bricks:
            return False
        if (px, py) in bomb_positions and (px, py) != (parent_px, parent_py):
            return False

    if action == "BOMB":
        if parent_state["ammo"] <= 0:
            return False
        if (parent_px, parent_py) in bomb_positions:
            return False

    # 2. Safety constraints at the new state
    if (px, py) in next_state["explosions"]:
        return False

    # Hazard zones: bombs that will detonate at or before this step
    hazard_zones = next_state.get("hazard_zones", {})
    if (px, py) in hazard_zones:
        timer = hazard_zones[(px, py)]
        # If the bomb detonates immediately (timer <= 0) or is about to detonate
        if timer <= 1:
            return False

    return True

class BacktrackingAgent(BaseAgent):
    """
    Backtracking Agent.
    Formulates a 4-step action path as a Constraint Satisfaction Problem (CSP).
    Uses recursive backtracking search with forward checking/consistency checks to find the
    optimal consistent path.
    """

    def __init__(self, max_depth: int = 4):
        self.max_depth = max_depth
        self.best_score = -float('inf')
        self.best_path: List[str] = []

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        
        # Reset backtracking variables
        self.best_score = -float('inf')
        self.best_path = []

        # Run Backtracking CSP Search
        self.backtrack([], state_info)

        if self.best_path:
            return self.best_path[0]
        
        # Fallback to WAIT if no path is consistent
        return "WAIT"

    def backtrack(self, assignment: List[str], current_state: dict):
        """Textbook recursive Backtracking Search over action variables."""
        if len(assignment) == self.max_depth:
            # Complete assignment: evaluate the utility of the terminal state
            score = evaluate_state(current_state)
            if score > self.best_score:
                self.best_score = score
                self.best_path = list(assignment)
            return

        # Domain for variables: possible actions
        domain = ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]

        # Order domain value heuristic: evaluate_state on 1-step lookahead to speed up pruning
        # (This is analogous to Least-Constraining-Value or heuristic ordering)
        candidates = []
        for action in domain:
            next_state = simulate_state(current_state, action)
            if is_step_consistent(current_state, next_state, action, len(assignment) + 1):
                h_val = evaluate_state(next_state)
                candidates.append((h_val, action, next_state))

        # Sort candidates descending by heuristic value
        candidates.sort(key=lambda x: x[0], reverse=True)

        # Try assigning each consistent value to the variable
        for _, action, next_state in candidates:
            # Assign
            assignment.append(action)
            
            # Recurse
            self.backtrack(assignment, next_state)
            
            # Backtrack
            assignment.pop()
