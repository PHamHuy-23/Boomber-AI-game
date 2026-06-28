"""
BFS Agent - Agent tìm kiếm theo chiều rộng (Breadth-First Search) cho game Bomberman.
"""
from typing import Tuple, Set, Dict, Optional
from collections import deque
from agents import BaseAgent
from agents.search_utils import parse_state, hierarchical_action

def bfs(start: Tuple[int, int],
        goal_set: Set[Tuple[int, int]],
        walls: set,
        bricks: set,
        bombs: list,
        explosions: set,
        hazard_zones: Dict[Tuple[int, int], int],
        width: int,
        height: int,
        danger_mode: bool = False) -> Optional[list]:
    """BFS trên lưới bản đồ 2D."""
    if not goal_set:
        return None

    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    frontier: deque = deque()
    frontier.append((start, [start]))
    visited: Set[Tuple[int, int]] = {start}

    while frontier:
        node, path = frontier.popleft()
        if node in goal_set:
            return path

        cx, cy = node
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            neighbor = (nx, ny)

            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if neighbor in walls or neighbor in bricks:
                continue
            if neighbor in bomb_positions and neighbor != start:
                continue
            if neighbor in explosions:
                continue
            if neighbor in hazard_zones and hazard_zones[neighbor] <= 1:
                continue
            if not danger_mode and neighbor in hazard_zones:
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append((neighbor, path + [neighbor]))

    return None

class BFSAgent(BaseAgent):
    """BFSAgent sử dụng BFS với logic phân tầng."""

    def __init__(self):
        self.search_fn = bfs

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        return hierarchical_action(self.search_fn, info)
