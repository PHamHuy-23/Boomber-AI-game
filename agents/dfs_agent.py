"""
DFS Agent - Agent tìm kiếm theo chiều sâu (Depth-First Search) trên không gian trạng thái cho game Bomberman.
"""
from typing import Tuple, Set, Dict, Optional, List
from agents import BaseAgent
from agents.search_utils import (
    parse_state, 
    simulate_state, 
    get_valid_actions, 
    state_signature, 
    get_hazard_zones, 
    hierarchical_action
)

def dfs(initial_state: dict, goal_test, max_depth: int = 10, danger_mode: bool = False) -> Optional[List[str]]:
    """DFS trên không gian trạng thái."""
    # Frontier lưu trữ các node dạng tuple: (state, action_path, depth)
    frontier = [(initial_state, [], 0)]
    visited = set()

    while frontier:
        state, path, depth = frontier.pop()

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

class DFSAgent(BaseAgent):
    """DFSAgent sử dụng DFS trên không gian trạng thái với logic phân tầng."""

    def __init__(self):
        self.search_fn = dfs

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
