"""
Backtracking Agent - Agent quay lui (Backtracking Search) tìm kiếm đường đi dưới dạng bài toán CSP.

Triết lý thiết kế:
  Agent coi việc tìm kiếm chuỗi hành động 4 bước tiếp theo như một Bài toán thỏa mãn ràng buộc (CSP - Constraint Satisfaction Problem).
  - Biến số (Variables): Hành động tại mỗi bước (bước 1, 2, 3, 4).
  - Miền giá trị (Domain): ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"].
  - Ràng buộc (Constraints):
    + Vật lý: Không đi vào tường, gạch, bom hiện tại, không đặt bom khi hết đạn.
    + An toàn: Không đi vào ô đang nổ hoặc vùng bom nguy cấp sắp nổ (timer <= 1).
    
  Thuật toán sử dụng phương pháp Quay lui (Backtracking Search) kết hợp với:
    - Kiểm tra tính nhất quán từng bước (Consistency check / Forward checking).
    - Sắp xếp thứ tự giá trị miền (Domain Value Ordering): Ưu tiên thử các hành động có điểm heuristic cao trước để tăng tốc độ tìm kiếm và cắt tỉa nhánh.
"""
from typing import List, Tuple, Dict, Any, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def is_step_consistent(parent_state: dict, next_state: dict, action: str, step_idx: int) -> bool:
    """
    Kiểm tra xem bước chuyển trạng thái (từ parent_state sang next_state thông qua action) có thỏa mãn các ràng buộc CSP hay không.
    Trả về True nếu thỏa mãn mọi ràng buộc vật lý và an toàn.
    """
    px, py = next_state["player_pos"]
    parent_px, parent_py = parent_state["player_pos"]
    walls = parent_state["walls"]
    bricks = parent_state["bricks"]
    bombs = parent_state["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = parent_state["width"], parent_state["height"]

    # 1. Ràng buộc vật lý & biên bản đồ
    if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
        if not (0 <= px < width and 0 <= py < height):
            return False
        # Không được đi xuyên tường cứng, gạch hoặc quả bom khác (trừ khi đứng ngay tại ô bom gốc ở bước đầu)
        if (px, py) in walls or (px, py) in bricks:
            return False
        if (px, py) in bomb_positions and (px, py) != (parent_px, parent_py):
            return False

    if action == "BOMB":
        if parent_state["ammo"] <= 0:
            return False
        if (parent_px, parent_py) in bomb_positions:
            return False # Không đặt bom đè lên quả bom đang có sẵn

    # 2. Ràng buộc an toàn ở trạng thái tiếp theo
    if (px, py) in next_state["explosions"]:
        return False # Tránh lửa nổ trực tiếp

    # Ràng buộc vùng nguy hiểm: bom sẽ nổ tại hoặc trước bước đi này
    hazard_zones = next_state.get("hazard_zones", {})
    if (px, py) in hazard_zones:
        timer = hazard_zones[(px, py)]
        # Nếu bom sắp nổ ngay lập tức (timer <= 1)
        if timer <= 1:
            return False

    return True

class BacktrackingAgent(BaseAgent):
    """
    BacktrackingAgent áp dụng tìm kiếm quay lui thỏa mãn ràng buộc để sinh ra chuỗi hành động 4 bước an toàn và tối ưu nhất.
    """

    def __init__(self, max_depth: int = 4):
        self.max_depth = max_depth
        self.best_score = -float('inf')
        self.best_path: List[str] = []

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        
        # Khởi tạo lại các biến tìm kiếm quay lui
        self.best_score = -float('inf')
        self.best_path = []

        # Thực thi tìm kiếm quay lui CSP
        self.backtrack([], state_info)

        if self.best_path:
            return self.best_path[0] # Trả về hành động đầu tiên trong chuỗi tốt nhất tìm được
        
        # Nếu không tìm được bất kỳ chuỗi hành động nào thỏa mãn ràng buộc, chọn WAIT làm dự phòng
        return "WAIT"

    def backtrack(self, assignment: List[str], current_state: dict):
        """Hàm tìm kiếm quay lui đệ quy trên không gian gán nhãn hành động."""
        # Nếu đã gán đủ số biến (đạt độ sâu tối đa)
        if len(assignment) == self.max_depth:
            # Đánh giá điểm số của trạng thái lá
            score = evaluate_state(current_state)
            if score > self.best_score:
                self.best_score = score
                self.best_path = list(assignment)
            return

        # Miền giá trị của biến
        domain = ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]

        # Sắp xếp thứ tự thử giá trị (Heuristic Domain Value Ordering):
        # Đánh giá nhanh điểm số của trạng thái sau 1 bước đi để ưu tiên duyệt các hành động hứa hẹn trước
        candidates = []
        for action in domain:
            next_state = simulate_state(current_state, action)
            # Chỉ xem xét các hành động nhất quán thỏa mãn ràng buộc
            if is_step_consistent(current_state, next_state, action, len(assignment) + 1):
                h_val = evaluate_state(next_state)
                candidates.append((h_val, action, next_state))

        # Sắp xếp giảm dần theo điểm số heuristic
        candidates.sort(key=lambda x: x[0], reverse=True)

        # Duyệt qua các hành động hợp lệ theo thứ tự ưu tiên
        for _, action, next_state in candidates:
            # 1. Gán giá trị (Assign)
            assignment.append(action)
            
            # 2. Đệ quy đi tiếp (Recurse)
            self.backtrack(assignment, next_state)
            
            # 3. Quay lui gỡ bỏ gán giá trị (Backtrack)
            assignment.pop()
