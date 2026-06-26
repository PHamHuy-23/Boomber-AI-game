"""Expectimax agent implementation for Bomberman."""
from typing import List, Tuple, Dict, Any
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def get_valid_actions(state_info: dict) -> List[str]:
    """Get all physically valid actions for the player in the current state."""
    px, py = state_info["player_pos"]
    walls = state_info["walls"]
    bricks = state_info["bricks"]
    bombs = state_info["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = state_info["width"], state_info["height"]

    valid = ["WAIT"]

    # Movement actions
    moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
    for action, (dx, dy) in moves.items():
        nx, ny = px + dx, py + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid.append(action)

    # Bomb placement action
    if state_info["ammo"] > 0 and (px, py) not in bomb_positions:
        valid.append("BOMB")

    return valid

def get_enemy_valid_moves(enemy_pos: Tuple[int, int], state_info: dict) -> List[Tuple[int, int]]:
    """Get all valid next positions for an enemy (adjacent cells and waiting)."""
    ex, ey = enemy_pos
    walls = state_info["walls"]
    bricks = state_info["bricks"]
    bombs = state_info["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = state_info["width"], state_info["height"]

    valid_positions = [(ex, ey)] # Waiting is always possible

    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = ex + dx, ey + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid_positions.append((nx, ny))

    return valid_positions

class ExpectimaxAgent(BaseAgent):
    """An agent that uses depth-limited Expectimax search to choose actions."""

    def __init__(self, depth: int = 5):
        self.depth = depth

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        
        # Determine root's legal actions
        legal_actions = state.get("legal_actions")
        valid_actions = get_valid_actions(state_info)
        if legal_actions:
            valid_actions = [a for a in valid_actions if a in legal_actions]
        if not valid_actions:
            valid_actions = ["WAIT"]

        best_action = "WAIT"
        best_score = -float('inf')

        # Expectimax Root (MAX node)
        for action in valid_actions:
            next_state = simulate_state(state_info, action)
            score = self.chance_value(next_state, self.depth - 1)
            
            if score > best_score:
                best_score = score
                best_action = action
            
        return best_action

    def max_value(self, state: dict, depth: int) -> float:
        """MAX node: maximizes expected utility."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return evaluate_state(state)

        valid_actions = get_valid_actions(state)
        if not valid_actions:
            return evaluate_state(state)

        v = -float('inf')
        for action in valid_actions:
            next_state = simulate_state(state, action)
            v = max(v, self.chance_value(next_state, depth - 1))
        return v

    def chance_value(self, state: dict, depth: int) -> float:
        """CHANCE node: returns average utility over possible enemy movements (uniform probability)."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return evaluate_state(state)

        enemies = state["enemies"]
        if not enemies:
            # If no enemies are present, run a MAX node at the next level
            return self.max_value(state, depth - 1)

        # Stochastic Adversary: model the enemy closest to the player
        px, py = state["player_pos"]
        closest_idx = 0
        min_dist = float('inf')
        for idx, (ex, ey) in enumerate(enemies):
            dist = abs(px - ex) + abs(py - ey)
            if dist < min_dist:
                min_dist = dist
                closest_idx = idx

        enemy_pos = enemies[closest_idx]
        valid_moves = get_enemy_valid_moves(enemy_pos, state)

        # Average the values of all successor states (uniform distribution)
        total_value = 0.0
        for next_pos in valid_moves:
            next_state = {**state}
            next_state["enemies"] = list(state["enemies"])
            next_state["enemies"][closest_idx] = next_pos
            
            total_value += self.max_value(next_state, depth - 1)

        return total_value / len(valid_moves)
