"""
Online Search Agent - Agent Tìm kiếm trực tuyến LRTA* (Learning Real-Time A*) cho game Bomberman.

Triết lý thiết kế:
  Khác với các phương pháp lập kế hoạch offline (BFS, A*, Minimax...) mô phỏng toàn bộ hành trình trước khi di chuyển,
  Online Search Agent sử dụng thuật toán LRTA* (Learning Real-Time A*):
    1. Quyết định hành động di chuyển ngay lập tức dựa trên chi phí cục bộ cộng với ước lượng heuristic từ các ô láng giềng.
    2. Lưu trữ các giá trị ước lượng này vào bảng tra cứu H (State-Space Memory).
    3. Cập nhật động giá trị H(s_prev) của trạng thái trước đó dựa trên trải nghiệm thực tế để "học hỏi" và tránh
       bị mắc kẹt vào các giếng tối ưu cục bộ (local minima / loops).
       Công thức cập nhật: H(s_prev) = max(H(s_prev), min_b (c(s_prev, b, s') + H(s')))
"""
from typing import List, Tuple, Dict, Any, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def get_state_key(state_info: dict) -> Tuple[Tuple[int, int], Tuple[Tuple[int, int], ...], Optional[Tuple[int, int]]]:
    """
    Tạo một khóa (key) định danh duy nhất cho mỗi trạng thái rời rạc để lưu trữ vào bảng LRTA*.
    Khóa gồm: (tọa độ_player, danh_sách_tọa_độ_bom_đã_sắp_xếp, tọa độ_kẻ_địch_gần_nhất).
    """
    px, py = state_info["player_pos"]
    bombs = state_info["bombs"]
    bombs_key = tuple(sorted((bx, by) for bx, by, _ in bombs))
    
    enemies = state_info["enemies"]
    closest_enemy_pos = None
    if enemies:
        min_dist = float('inf')
        for ex, ey in enemies:
            dist = abs(px - ex) + abs(py - ey)
            if dist < min_dist:
                min_dist = dist
                closest_enemy_pos = (ex, ey)
                
    return ((px, py), bombs_key, closest_enemy_pos)

def get_action_cost(action: str, current_state: dict, next_state: dict) -> float:
    """
    Định nghĩa chi phí bước chuyển c(s, a, s').
    Vì LRTA* là thuật toán tìm đường tối thiểu hóa chi phí (cost minimizer):
      - Hành động bất hợp lệ vật lý: chi phí cực lớn (10M) để chặn.
      - Di chuyển hợp lệ: chi phí nhỏ (10.0) nhằm khuyến khích đi đường ngắn.
      - Chờ hoặc đặt bom hợp lệ: chi phí nhỉnh hơn một chút (20.0) nhằm hạn chế đặt bom bừa bãi hay chờ vô ích.
    """
    px, py = next_state["player_pos"]
    parent_px, parent_py = current_state["player_pos"]
    
    # Kiểm tra tính hợp lệ vật lý của di chuyển
    if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
        walls = current_state["walls"]
        bricks = current_state["bricks"]
        bombs = current_state["bombs"]
        bomb_positions = {(bx, by) for bx, by, _ in bombs}
        width, height = current_state["width"], current_state["height"]
        
        if not (0 <= px < width and 0 <= py < height):
            return 10000000.0
        if (px, py) in walls or (px, py) in bricks:
            return 10000000.0
        if (px, py) in bomb_positions and (px, py) != (parent_px, parent_py):
            return 10000000.0
            
        return 10.0

    if action == "BOMB":
        if current_state["ammo"] <= 0:
            return 10000000.0
        if (parent_px, parent_py) in {(b[0], b[1]) for b in current_state["bombs"]}:
            return 10000000.0
        return 20.0

    if action == "WAIT":
        return 20.0

    return 10.0

def get_initial_heuristic(state_info: dict) -> float:
    """
    Ước lượng heuristic ban đầu h(s) cho LRTA*.
    Chuyển đổi điểm số heuristic (càng cao càng tốt) sang thang đo chi phí dương (càng thấp càng tốt).
    """
    if "hazard_zones" not in state_info:
        state_info = simulate_state(state_info, "WAIT")
    score = evaluate_state(state_info)
    # Trả về giá trị chi phí (cost)
    return max(0.0, 1000000.0 - score)

class OnlineSearchAgent(BaseAgent):
    """
    OnlineSearchAgent áp dụng thuật toán LRTA* sách giáo khoa để học Heuristic trực tuyến trong khi chơi.
    """

    def __init__(self):
        # Bảng tra cứu bộ nhớ H: state_key -> chi phí ước lượng tới đích
        self.H: Dict[Any, float] = {}
        self.prev_state_key = None
        self.prev_action = None
        self.steps_run = 0

    def choose_action(self, state: dict) -> str:
        self.steps_run += 1
        state_info = parse_state(state)
        current_state_key = get_state_key(state_info)
        
        # Reset bộ nhớ nếu game mới bắt đầu (bước chạy đầu tiên)
        if self.steps_run <= 1:
            self.prev_state_key = None
            self.prev_action = None

        # 1. Khởi tạo giá trị H cho trạng thái hiện tại nếu chưa từng gặp
        if current_state_key not in self.H:
            self.H[current_state_key] = get_initial_heuristic(state_info)

        # 2. Cập nhật học hỏi (Learning update) cho trạng thái trước đó s_prev:
        # H(s_prev) = max(H(s_prev), min_b (c(s_prev, b, s') + H(s')))
        if self.prev_state_key is not None and self.prev_action is not None:
            prev_info = self.prev_state_info
            
            # Tìm giá trị tối thiểu của c(s_prev, b, s') + H(s') trên mọi hành động b
            min_val = float('inf')
            for b in ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]:
                next_st_b = simulate_state(prev_info, b)
                cost_b = get_action_cost(b, prev_info, next_st_b)
                next_key_b = get_state_key(next_st_b)
                
                # Khởi tạo H cho trạng thái con nếu chưa có
                if next_key_b not in self.H:
                    self.H[next_key_b] = get_initial_heuristic(next_st_b)
                    
                val_b = cost_b + self.H[next_key_b]
                if val_b < min_val:
                    min_val = val_b
            
            # Cập nhật giá trị bộ nhớ H của trạng thái trước đó
            self.H[self.prev_state_key] = max(self.H[self.prev_state_key], min_val)

        # 3. Lựa chọn hành động: chọn hành động a từ trạng thái hiện tại làm tối thiểu hóa f = c(s, a, s') + H(s')
        best_action = "WAIT"
        min_cost = float('inf')

        # Liệt kê các hành động khả thi tại nút gốc hiện tại
        actions = ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]
        legal_actions = state.get("legal_actions")
        if legal_actions:
            actions = [a for a in actions if a in legal_actions]

        for action in actions:
            next_st = simulate_state(state_info, action)
            cost = get_action_cost(action, state_info, next_st)
            next_key = get_state_key(next_st)

            # Khởi tạo H cho trạng thái con nếu chưa có
            if next_key not in self.H:
                self.H[next_key] = get_initial_heuristic(next_st)

            f_value = cost + self.H[next_key]
            
            if f_value < min_cost:
                min_cost = f_value
                best_action = action

        # 4. Lưu lại trạng thái và hành động hiện tại để làm tài liệu học cho bước kế tiếp
        self.prev_state_key = current_state_key
        self.prev_action = best_action
        self.prev_state_info = state_info

        return best_action
