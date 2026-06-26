"""AND-OR Search Agent for Bomberman."""
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

class AndOrSearchAgent(BaseAgent):
    """
    AND-OR Search Agent.
    Models the non-deterministic environment: OR nodes (agent decisions) and
    AND nodes (possible outcomes / enemy moves) where the agent seeks a contingent
    plan that works in the worst-case.
    """

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

        # OR Node at the Root: choose the action that maximizes the AND-node value
        for action in valid_actions:
            next_state = simulate_state(state_info, action)
            score = self.and_node(next_state, self.depth - 1)
            
            if score > best_score:
                best_score = score
                best_action = action
            
        return best_action

    def or_node(self, state: dict, depth: int) -> float:
        """OR node: agent chooses the action with the best AND-node outcome."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return evaluate_state(state)

        valid_actions = get_valid_actions(state)
        if not valid_actions:
            return evaluate_state(state)

        v = -float('inf')
        for action in valid_actions:
            next_state = simulate_state(state, action)
            v = max(v, self.and_node(next_state, depth - 1))
        return v

    def and_node(self, state: dict, depth: int) -> float:
        """AND node: must handle ALL possible outcomes of non-determinism (minimum utility)."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return evaluate_state(state)

        enemies = state["enemies"]
        if not enemies:
            # If no enemies, the AND node has only 1 branch (the next OR node decision)
            return self.or_node(state, depth - 1)

        # Model the closest enemy as the source of environmental non-determinism
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

        # Pessimistic worst-case value over all possible enemy movements
        v = float('inf')
        for next_pos in valid_moves:
            next_state = {**state}
            next_state["enemies"] = list(state["enemies"])
            next_state["enemies"][closest_idx] = next_pos
            
            v = min(v, self.or_node(next_state, depth - 1))

        return v if v != float('inf') else evaluate_state(state)
