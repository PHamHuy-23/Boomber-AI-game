"""
A* Agent - Agent tìm kiếm A* (A-Star Search) cho game Bomberman.
"""
import heapq
from typing import Tuple, Set, Dict, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, hierarchical_action

def astar(start: Tuple[int, int],
          goal_set: Set[Tuple[int, int]],
          walls: set,
          bricks: set,
          bombs: list,
          explosions: set,
          hazard_zones: Dict[Tuple[int, int], int],
          width: int,
          height: int,
          danger_mode: bool = False) -> Optional[list]:
    """A* trên lưới bản đồ 2D."""
    if not goal_set:
        return None

    bomb_positions = {(bx, by) for bx, by, _ in bombs}

    def heuristic(pos: Tuple[int, int]) -> int:
        return min(abs(pos[0] - g[0]) + abs(pos[1] - g[1]) for g in goal_set)

    start_h = heuristic(start)
    open_heap = []
    heapq.heappush(open_heap, (start_h, 0, start[0], start[1]))

    g_score = {start: 0}
    came_from = {}
    closed_set = set()

    while open_heap:
        f, g_heap, cx, cy = heapq.heappop(open_heap)
        current = (cx, cy)

        if current in closed_set:
            continue
        closed_set.add(current)

        if current in goal_set:
            path = []
            node = current
            while node != start:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return list(reversed(path))

        g = g_score.get(current, float('inf'))

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

            if neighbor in closed_set:
                continue

            tentative_g = g + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                h_val = heuristic(neighbor)
                heapq.heappush(open_heap, (tentative_g + h_val, tentative_g, nx, ny))

    return None

class AStarAgent(BaseAgent):
    """AStarAgent sử dụng A* với logic phân tầng."""

    def __init__(self):
        self.search_fn = astar

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        return hierarchical_action(self.search_fn, info)
