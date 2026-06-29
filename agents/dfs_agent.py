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
        
        import agents.search_utils as search_utils
        if isinstance(search_utils.CURRENT_SEARCH_TRACE, dict):
            search_utils.CURRENT_SEARCH_TRACE["nodes_expanded"] += 1
            search_utils.CURRENT_SEARCH_TRACE["frontier_size"] = len(frontier)

        # Goal Test: dừng ngay khi đạt điều kiện đầu tiên
        if goal_test(state):
            if isinstance(search_utils.CURRENT_SEARCH_TRACE, dict):
                search_utils.CURRENT_SEARCH_TRACE["path"] = path
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

    def __init__(self, depth_limit: int = 10):
        self.depth_limit = depth_limit
        self.search_fn = lambda state, goal_test, **kwargs: dfs(state, goal_test, max_depth=self.depth_limit, danger_mode=kwargs.get("danger_mode", False))

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
        action = hierarchical_action(self.search_fn, info)
        
        import agents.search_utils as search_utils
        self.last_trace = {
            "algorithm": "dfs",
            "nodes_expanded": search_utils.CURRENT_SEARCH_TRACE.get("nodes_expanded", 0),
            "search_depth": len(search_utils.CURRENT_SEARCH_TRACE.get("path", [])),
            "frontier_size": search_utils.CURRENT_SEARCH_TRACE.get("frontier_size", 0),
            "path": search_utils.CURRENT_SEARCH_TRACE.get("path", []),
            "chosen_action": action,
            "reasoning": [
                "Running Depth-First Search (DFS)...",
                f"Nodes expanded: {search_utils.CURRENT_SEARCH_TRACE.get('nodes_expanded', 0)}",
                f"Frontier size: {search_utils.CURRENT_SEARCH_TRACE.get('frontier_size', 0)}",
                f"Path found: {search_utils.CURRENT_SEARCH_TRACE.get('path', [])}",
                f"Chosen move: {action}"
            ]
        }
        return action
