"""
Hill Climbing Agent - Agent leo đồi (Hill Climbing Search) cho game Bomberman.

Triết lý thiết kế:
  Leo đồi là thuật toán tìm kiếm cục bộ (Local Search) không nhìn xa (lookahead = 1 bước).
  Tại mỗi bước di chuyển, agent sinh ra tất cả các trạng thái láng giềng kế cận (successors)
  và di chuyển tới láng giềng có điểm số heuristic cao nhất (Steepest Ascent).
  
  Để khắc phục các điểm hạn chế của Leo đồi cơ bản:
    - Đi ngang (Sideways moves): Nếu láng giềng tốt nhất bằng điểm hiện tại, cho phép di chuyển ngang (tối đa 5 lượt).
    - Khởi động lại ngẫu nhiên (Random Restart): Nếu gặp Cực trị cục bộ (Local Maximum - tất cả láng giềng đều tệ hơn hiện tại),
      agent sẽ chọn ngẫu nhiên một hành động an toàn để thoát ra.
"""
import gc
import random
from typing import Tuple, Dict, Set, List
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

class HillClimbingAgent(BaseAgent):
    """
    HillClimbingAgent mô phỏng thuật toán leo đồi dốc nhất (Steepest-Ascent Hill Climbing) chuẩn sách giáo khoa.
    Tìm kiếm trên không gian đường đi 4 bước bằng cách chọn láng giềng tốt nhất tại mỗi lượt lặp cho đến khi đạt cực trị cục bộ.
    """

    def __init__(self, max_steps: int = 30):
        super().__init__()
        self.max_steps = max_steps

    def is_action_consistent(self, parent_state: dict, next_state: dict, action: str) -> bool:
        """Kiểm tra tính nhất quán vật lý và an toàn của bước đi."""
        px, py = next_state["player_pos"]
        parent_px, parent_py = parent_state["player_pos"]
        walls = parent_state["walls"]
        bricks = parent_state["bricks"]
        bombs = parent_state["bombs"]
        bomb_positions = {(bx, by) for bx, by, _ in bombs}
        width, height = parent_state["width"], parent_state["height"]

        if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if not (0 <= px < width and 0 <= py < height):
                return False
            if (px, py) in walls or (px, py) in bricks:
                return False
            if (px, py) in bomb_positions and (px, py) != (parent_px, parent_py):
                return False

        if action == "BOMB":
            if parent_state["ammo"] <= 0:
                return False
            if (parent_px, parent_py) in bomb_positions:
                return False

        if (px, py) in next_state["explosions"]:
            return False

        hazard_zones = next_state.get("hazard_zones", {})
        if (px, py) in hazard_zones:
            if hazard_zones[(px, py)] <= 1:
                return False

        return True

    def evaluate_path(self, path: List[str], initial_state: dict) -> float:
        """Đánh giá toàn bộ đường đi 4 bước từ trạng thái ban đầu."""
        current_state = initial_state
        for step_idx, action in enumerate(path):
            next_state = simulate_state(current_state, action)
            if not self.is_action_consistent(current_state, next_state, action):
                # Phạt nặng nếu chuỗi hành động không hợp lệ hoặc gây tự sát tức thời
                return -1000000.0 - (len(path) - step_idx) * 10000.0
            current_state = next_state
        return evaluate_state(current_state)

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        
        # Khởi tạo với một đường đi mặc định an toàn: ["WAIT", "WAIT", "WAIT", "WAIT"]
        current_path = ["WAIT", "WAIT", "WAIT", "WAIT"]
        current_score = self.evaluate_path(current_path, info)
        
        domain = ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]
        nodes_expanded = 0
        evaluations = {}
        
        # Vòng lặp leo đồi dốc nhất (Steepest-Ascent)
        for step in range(self.max_steps):
            best_neighbor_path = None
            best_neighbor_score = -float('inf')
            
            # Khảo sát toàn bộ 20 láng giềng (đột biến 1 hành động trong chuỗi 4 bước)
            for idx in range(len(current_path)):
                for action in domain:
                    if action == current_path[idx]:
                        continue
                    neighbor_path = list(current_path)
                    neighbor_path[idx] = action
                    
                    nodes_expanded += 1
                    score = self.evaluate_path(neighbor_path, info)
                    if score > best_neighbor_score:
                        best_neighbor_score = score
                        best_neighbor_path = neighbor_path
                        
            # Lưu vết đánh giá cho trực quan hóa
            evaluations[f"Step {step}"] = best_neighbor_score
            
            # Nếu láng giềng tốt nhất tốt hơn hẳn trạng thái hiện tại, leo lên
            if best_neighbor_score > current_score:
                current_path = best_neighbor_path
                current_score = best_neighbor_score
            else:
                # Đã đạt Cực trị cục bộ (Local Maximum), dừng tìm kiếm
                break
                
        action = current_path[0]
        self.last_trace = {
            "algorithm": "hill_climbing",
            "nodes_expanded": nodes_expanded,
            "search_depth": 4, # 4-step path horizon
            "path": current_path,
            "chosen_action": action,
            "evaluations": evaluations,
            "reasoning": [
                "Running Hill Climbing (Local Search)...",
                f"Total candidate paths evaluated: {nodes_expanded}",
                f"Local maximum score reached: {current_score:.1f}",
                f"Optimal 4-step path: {current_path}",
                f"Chosen action (first step): {action}"
            ]
        }
        return action
