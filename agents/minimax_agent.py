"""Minimax agent implementation for Bomberman using Alpha-Beta Pruning."""
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

class MinimaxAgent(BaseAgent):
    """An agent that uses depth-limited Minimax search with Alpha-Beta pruning."""

    def __init__(self, depth: int = 5):
        self.depth = depth

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        
        # Determine the root's legal actions (using legal_actions from state if available, but validated)
        legal_actions = state.get("legal_actions")
        valid_actions = get_valid_actions(state_info)
        if legal_actions:
            valid_actions = [a for a in valid_actions if a in legal_actions]
        if not valid_actions:
            valid_actions = ["WAIT"]

        best_action = "WAIT"
        best_score = -float('inf')
        alpha = -float('inf')
        beta = float('inf')

        # Alpha-Beta Search Root (MAX node)
        for action in valid_actions:
            next_state = simulate_state(state_info, action)
            score = self.min_value(next_state, alpha, beta, self.depth - 1)
            
            if score > best_score:
                best_score = score
                best_action = action
            
            alpha = max(alpha, best_score)
            
        return best_action

    def max_value(self, state: dict, alpha: float, beta: float, depth: int) -> float:
        """MAX node: maximizes player's utility."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return evaluate_state(state)

        valid_actions = get_valid_actions(state)
        if not valid_actions:
            return evaluate_state(state)

        v = -float('inf')
        for action in valid_actions:
            next_state = simulate_state(state, action)
            v = max(v, self.min_value(next_state, alpha, beta, depth - 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state: dict, alpha: float, beta: float, depth: int) -> float:
        """MIN node: minimizes player's utility using adversarial enemy decisions."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return evaluate_state(state)

        enemies = state["enemies"]
        if not enemies:
            # If no enemies are present, run a MAX node at the next level
            return self.max_value(state, alpha, beta, depth - 1)

        # Adversary: model the enemy closest to the player
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

        v = float('inf')
        for next_pos in valid_moves:
            # Simulate the enemy's move in the state dictionary
            next_state = {**state}
            next_state["enemies"] = list(state["enemies"])
            next_state["enemies"][closest_idx] = next_pos
            
            v = min(v, self.max_value(next_state, alpha, beta, depth - 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v