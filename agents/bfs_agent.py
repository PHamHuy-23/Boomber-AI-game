"""
BFS Agent - Agent tìm kiếm theo chiều rộng (Breadth-First Search) trên không gian trạng thái cho game Bomberman.
"""
from typing import Tuple, Set, Dict, Optional, List
from collections import deque
from agents import BaseAgent
from agents.search_utils import (
    parse_state, 
    simulate_state, 
    get_hazard_zones, 
    hierarchical_action
)

def state_signature(state: dict) -> tuple:
    """Tạo signature duy nhất đại diện cho trạng thái game hiện tại phục vụ tránh trùng lặp."""
    player_pos = state["player_pos"]
    bombs = tuple(sorted((b[0], b[1], b[2]) for b in state["bombs"]))
    enemies = tuple(sorted(state["enemies"]))
    explosions = tuple(sorted(state["explosions"]))
    ammo = state.get("ammo", 1)
    blast_radius = state.get("blast_radius", 2)
    return (player_pos, bombs, enemies, explosions, ammo, blast_radius)

def get_valid_actions(state: dict) -> List[str]:
    """Lấy các hành động di chuyển và đứng yên hợp lệ vật lý (không đâm vào tường, gạch, bom)."""
    px, py = state["player_pos"]
    walls = state["walls"]
    bricks = state["bricks"]
    bombs = state["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = state["width"], state["height"]

    valid = []
    
    # WAIT luôn hợp lệ vật lý
    valid.append("WAIT")

    # Các hướng di chuyển
    moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
    for action, (dx, dy) in moves.items():
        nx, ny = px + dx, py + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid.append(action)

    return valid

def bfs(initial_state: dict, goal_test, max_depth: int = 10, danger_mode: bool = False) -> Optional[List[str]]:
    """
    Breadth-First Search (BFS) thuần túy trên không gian trạng thái.
    """
    # Frontier lưu trữ các node dạng tuple: (state, action_path, depth)
    frontier = deque([(initial_state, [], 0)])
    visited = set()

    while frontier:
        state, path, depth = frontier.popleft()

        # Goal Test: dừng ngay khi đạt điều kiện đầu tiên
        if goal_test(state):
            return path

        if depth >= max_depth:
            continue

        sig = state_signature(state)
        if sig in visited:
            continue
        visited.add(sig)

        actions = get_valid_actions(state)
        for action in actions:
            next_state = simulate_state(state, action)
            
            # Loại bỏ trạng thái bị chết do lửa nổ
            if next_state["player_pos"] in next_state["explosions"]:
                continue

            npos = next_state["player_pos"]
            # Đánh giá độ an toàn dựa trên hazard_zones động
            if not danger_mode and npos in next_state["hazard_zones"]:
                continue
            if npos in next_state["hazard_zones"] and next_state["hazard_zones"][npos] <= 1:
                continue

            frontier.append((next_state, path + [action], depth + 1))

    return None

class BFSAgent(BaseAgent):
    """
    BFSAgent sử dụng phân tầng quyết định (hierarchical) dựa trên BFS không gian trạng thái.
    """
    def __init__(self):
        self.search_fn = bfs

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        
        # Đồng bộ và tính toán hazard_zones động cho trạng thái ban đầu
        info["hazard_zones"] = get_hazard_zones(
            info["bombs"], 
            info["walls"], 
            info["bricks"], 
            info["blast_radius"], 
            info["width"], 
            info["height"],
            info.get("bomb_ranges", {})
        )
        return hierarchical_action(self.search_fn, info)
