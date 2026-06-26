"""Hill Climbing Agent for Bomberman."""
import gc
import random
from typing import Tuple, Dict, Set, List
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state


class HillClimbingAgent(BaseAgent):
    """
    Hill Climbing Agent - Local search that always moves to the neighbor
    with the highest heuristic score (steepest ascent hill climbing).
    Makes greedy local decisions - no lookahead beyond immediate neighbors.
    Uses Sideways Moves with limit, falling back to Random Restart (random valid action).

    Note: Since Bomberman is an online game where arbitrary state reinitialization
    is impossible, Random-Restart is approximated by selecting a random valid action.
    """

    def __init__(self):
        super().__init__()
        self.sideways_count = 0
        self.sideways_limit = 5

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]
        bricks = info["bricks"]
        bombs = info["bombs"]
        explosions = info["explosions"]
        enemies = info["enemies"]
        items = info["items"]
        ammo = info["ammo"]
        blast_radius = info["blast_radius"]
        width = info["width"]
        height = info["height"]

        bomb_positions = {(bx, by) for bx, by, _ in bombs}

        # 1. Evaluate current state (simulating WAIT action)
        current_sim = simulate_state(info, "WAIT")
        current_score = evaluate_state(current_sim)

        # 2. Generate valid actions and their simulated states
        moves = [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]
        successors = []

        # WAIT successor
        successors.append(("WAIT", current_sim, current_score))

        # Movement successors
        for action, dx, dy in moves:
            nx, ny = px + dx, py + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in walls and (nx, ny) not in bricks:
                    if (nx, ny) not in bomb_positions or (nx, ny) == (px, py):
                        sim = simulate_state(info, action)
                        score = evaluate_state(sim)
                        successors.append((action, sim, score))

        # BOMB successor
        if ammo > 0 and (px, py) not in bomb_positions:
            sim = simulate_state(info, "BOMB")
            score = evaluate_state(sim)
            successors.append(("BOMB", sim, score))

        # 3. Steepest-Ascent decision logic
        # Find successor with highest score
        best_score = -float("inf")
        best_actions = []

        for action, sim, score in successors:
            if score > best_score:
                best_score = score
                best_actions = [action]
            elif score == best_score:
                best_actions.append(action)

        chosen_action = "WAIT"
        # Separate actions into strictly better, equal, and worse
        if best_score > current_score:
            self.sideways_count = 0
            chosen_action = random.choice(best_actions)

        # If best_score == current_score: Sideways move
        elif best_score == current_score:
            if self.sideways_count < self.sideways_limit:
                self.sideways_count += 1
                chosen_action = random.choice(best_actions)
            else:
                self.sideways_count = 0
                valid_moves = [a for a, _, _ in successors if a != "WAIT"]
                if valid_moves:
                    chosen_action = random.choice(valid_moves)
                else:
                    chosen_action = "WAIT"

        # If best_score < current_score: Local Maximum -> Random Restart
        else:
            self.sideways_count = 0
            safe_moves = []
            for action, sim, score in successors:
                sim_pos = sim["player_pos"]
                sim_hazard = sim["hazard_zones"]
                sim_explosions = sim["explosions"]
                if sim_pos not in sim_explosions and (sim_pos not in sim_hazard or sim_hazard[sim_pos] > 1):
                    safe_moves.append(action)

            if safe_moves:
                chosen_action = random.choice(safe_moves)
            else:
                valid_moves = [a for a, _, _ in successors]
                if valid_moves:
                    chosen_action = random.choice(valid_moves)
                else:
                    chosen_action = "WAIT"

        return chosen_action
