"""
Min-Conflicts Agent - Agent giải bài toán ràng buộc bằng tìm kiếm cục bộ giảm xung đột (Min-Conflicts).

Triết lý thiết kế:
  Agent xem việc tìm kiếm chuỗi hành động 4 bước như một Bài toán thỏa mãn ràng buộc (CSP).
  Thay vì dùng tìm kiếm quay lui hệ thống (Backtracking), nó sử dụng Thuật toán Tìm kiếm cục bộ Giảm xung đột (Min-Conflicts):
    1. Khởi tạo một lời giải ngẫu nhiên (chuỗi hành động ngẫu nhiên hợp lệ).
    2. Xác định các bước đi xảy ra xung đột (conflited variables - ví dụ: bước đi vào lửa nổ, đi vào bom, đụng địch).
    3. Chọn ngẫu nhiên một bước đi có xung đột.
    4. Thay đổi hành động của bước đi đó bằng cách chọn hành động nào làm giảm tổng số xung đột của toàn chuỗi nhiều nhất
       (nếu số xung đột bằng nhau thì chọn hành động đem lại điểm số heuristic cao nhất để phá vỡ thế bí).
    5. Lặp lại cho đến khi hết xung đột hoặc đạt số bước lặp tối đa (max_steps = 100).
"""
import random
from typing import List, Tuple, Dict, Any
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state


def get_valid_actions_for_mc(st: dict) -> List[str]:
    """Lấy danh sách các hành động hợp lệ vật lý ở trạng thái đang xét."""
    px, py = st["player_pos"]
    walls = st["walls"]
    bricks = st["bricks"]
    bombs = st["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = st["width"], st["height"]

    valid = ["WAIT"]
    moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
    for action, (dx, dy) in moves.items():
        nx, ny = px + dx, py + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid.append(action)

    if st["ammo"] > 0 and (px, py) not in bomb_positions:
        valid.append("BOMB")
    return valid

def get_conflicts_and_state(assignment: List[str], root_state: dict) -> Tuple[float, dict]:
    """
    Mô phỏng chuỗi gán nhãn hành động (assignment) và đếm tổng số xung đột (conflicts) xảy ra.
    Trả về: (tổng_số_xung_đột, trạng_thái_mô_phỏng_cuối_cùng).
    """
    current_state = root_state
    total_conflicts = 0.0

    for idx, action in enumerate(assignment):
        valid_actions = get_valid_actions_for_mc(current_state)
        resolved_action = action
        
        # Nếu hành động không khả thi về mặt vật lý, ép buộc chuyển thành WAIT và cộng xung đột
        if action not in valid_actions:
            total_conflicts += 10.0
            resolved_action = "WAIT"

        next_state = simulate_state(current_state, resolved_action)
        px, py = next_state["player_pos"]

        # Cộng dồn xung đột an toàn tại bước giả lập hiện thời
        if (px, py) in next_state["explosions"]:
            total_conflicts += 10.0 # Bị lửa nổ trúng

        hazard_zones = next_state.get("hazard_zones", {})
        if (px, py) in hazard_zones:
            timer = hazard_zones[(px, py)]
            if timer <= 1:
                total_conflicts += 10.0 # Đứng ở ô bom sắp nổ

        # Đụng độ kẻ địch
        for ex, ey in next_state["enemies"]:
            if px == ex and py == ey:
                total_conflicts += 10.0

        current_state = next_state

    return total_conflicts, current_state

class MinConflictsAgent(BaseAgent):
    """
    MinConflictsAgent giải quyết bài toán quy hoạch 4 bước đi dựa trên thuật toán Min-Conflicts.
    """

    def __init__(self, max_depth: int = 4, max_steps: int = 100):
        self.max_depth = max_depth      # Số bước quy hoạch (số biến CSP)
        self.max_steps = max_steps      # Số bước lặp tối đa của thuật toán tìm kiếm cục bộ

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        
        # Miền giá trị cho các biến hành động
        domain = ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]

        # 1. Khởi tạo phép gán ban đầu: chuỗi hành động ngẫu nhiên hợp lệ vật lý
        assignment = []
        curr = state_info
        for _ in range(self.max_depth):
            val_acts = get_valid_actions_for_mc(curr)
            act = random.choice(val_acts)
            assignment.append(act)
            curr = simulate_state(curr, act)
        
        best_assignment = list(assignment)
        best_conflicts, final_state = get_conflicts_and_state(assignment, state_info)
        best_score = evaluate_state(final_state)

        # 2. Vòng lặp tối ưu hóa giảm thiểu xung đột
        for step in range(self.max_steps):
            # Xác định các bước đi có xung đột
            conflicted_vars = []
            current = state_info
            for i, action in enumerate(assignment):
                valid_acts = get_valid_actions_for_mc(current)
                resolved_act = action
                if action not in valid_acts:
                    conflicted_vars.append(i)
                    resolved_act = "WAIT"
                
                next_st = simulate_state(current, resolved_act)
                px, py = next_st["player_pos"]
                
                step_conflict = False
                if (px, py) in next_st["explosions"]:
                    step_conflict = True
                elif (px, py) in next_st.get("hazard_zones", {}) and next_st["hazard_zones"][(px, py)] <= 1:
                    step_conflict = True
                
                if step_conflict:
                    conflicted_vars.append(i)
                current = next_st

            # Nếu không có bất kỳ xung đột nào, chọn ngẫu nhiên một biến để tìm cách cải thiện điểm số
            if not conflicted_vars:
                conflicted_vars = list(range(self.max_depth))

            # Chọn ngẫu nhiên một biến bị xung đột
            var_idx = random.choice(conflicted_vars)

            # Tìm giá trị (hành động) giảm xung đột tốt nhất cho biến này
            best_val = assignment[var_idx]
            min_c = float('inf')
            max_s = -float('inf')

            # Trộn miền giá trị để tránh thiên hướng hướng đi
            random_domain = list(domain)
            random.shuffle(random_domain)

            for val in random_domain:
                assignment[var_idx] = val
                c, final_st = get_conflicts_and_state(assignment, state_info)
                s = evaluate_state(final_st)
                
                # Ưu tiên giảm thiểu xung đột. Nếu xung đột bằng nhau, ưu tiên điểm số cao hơn.
                if c < min_c:
                    min_c = c
                    max_s = s
                    best_val = val
                elif c == min_c and s > max_s:
                    max_s = s
                    best_val = val

            # Gán giá trị tốt nhất tìm được cho biến
            assignment[var_idx] = best_val

            # Theo dõi và cập nhật cấu hình gán nhãn tốt nhất toàn cục
            current_conflicts, final_st = get_conflicts_and_state(assignment, state_info)
            current_score = evaluate_state(final_st)

            if current_conflicts < best_conflicts:
                best_conflicts = current_conflicts
                best_score = current_score
                best_assignment = list(assignment)
            elif current_conflicts == best_conflicts and current_score > best_score:
                best_score = current_score
                best_assignment = list(assignment)

        # Trả về hành động đầu tiên của cấu hình tốt nhất
        root_valid = get_valid_actions_for_mc(state_info)
        final_action = best_assignment[0]
        # Đảm bảo hành động trả về là hợp lệ tại tick hiện tại, nếu không thì đứng chờ (WAIT)
        if final_action not in root_valid:
            final_action = "WAIT"
            
        return final_action
