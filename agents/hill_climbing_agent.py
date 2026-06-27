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
    HillClimbingAgent sử dụng tìm kiếm leo đồi dốc nhất (Steepest Ascent Hill Climbing)
    để đưa ra quyết định di chuyển tối ưu cục bộ ngay lập tức.
    """

    def __init__(self):
        super().__init__()
        self.sideways_count = 0     # Bộ đếm số lần di chuyển ngang liên tục
        self.sideways_limit = 5     # Giới hạn số lần di chuyển ngang liên tục

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]
        bricks = info["bricks"]
        bombs = info["bombs"]
        explosions = info["explosions"]
        enemies = info["enemies"]
        items = info["items"]
        ammo = info["ammo"]
        blast_radius = info["blast_radius"]
        width = info["width"]
        height = info["height"]

        bomb_positions = {(bx, by) for bx, by, _ in bombs}

        # 1. Đánh giá trạng thái hiện tại (giả lập hành động chờ WAIT)
        current_sim = simulate_state(info, "WAIT")
        current_score = evaluate_state(current_sim)

        # 2. Sinh ra tất cả các trạng thái láng giềng kế tiếp (successors) khả thi
        moves = [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]
        successors = []

        # Láng giềng WAIT
        successors.append(("WAIT", current_sim, current_score))

        # Láng giềng di chuyển (UP, DOWN, LEFT, RIGHT)
        for action, dx, dy in moves:
            nx, ny = px + dx, py + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in walls and (nx, ny) not in bricks:
                    if (nx, ny) not in bomb_positions or (nx, ny) == (px, py):
                        sim = simulate_state(info, action)
                        score = evaluate_state(sim)
                        successors.append((action, sim, score))

        # Láng giềng đặt bom BOMB
        if ammo > 0 and (px, py) not in bomb_positions:
            sim = simulate_state(info, "BOMB")
            score = evaluate_state(sim)
            successors.append(("BOMB", sim, score))

        # 3. Logic quyết định leo đồi dốc nhất (Steepest-Ascent decision logic)
        # Tìm các láng giềng có điểm số heuristic cao nhất
        best_score = -float("inf")
        best_actions = []

        for action, sim, score in successors:
            if score > best_score:
                best_score = score
                best_actions = [action]
            elif score == best_score:
                best_actions.append(action)

        chosen_action = "WAIT"

        # Trường hợp 1: Có láng giềng tốt hơn trạng thái hiện tại (Leo đồi)
        if best_score > current_score:
            self.sideways_count = 0
            chosen_action = random.choice(best_actions)

        # Trường hợp 2: Láng giềng tốt nhất bằng điểm hiện tại (Di chuyển ngang - Sideways move)
        elif best_score == current_score:
            if self.sideways_count < self.sideways_limit:
                self.sideways_count += 1
                chosen_action = random.choice(best_actions) # Chấp nhận đi ngang
            else:
                # Nếu vượt quá giới hạn đi ngang, ép chọn ngẫu nhiên một nước đi khác để phá vỡ bế tắc
                self.sideways_count = 0
                valid_moves = [a for a, _, _ in successors if a != "WAIT"]
                if valid_moves:
                    chosen_action = random.choice(valid_moves)
                else:
                    chosen_action = "WAIT"

        # Trường hợp 3: Đang ở Cực trị cục bộ (Tất cả láng giềng đều tệ hơn hiện tại) -> Khởi động lại ngẫu nhiên
        else:
            self.sideways_count = 0
            # Lọc ra các di chuyển an toàn (không đi vào lửa nổ hoặc bom sắp nổ)
            safe_moves = []
            for action, sim, score in successors:
                sim_pos = sim["player_pos"]
                sim_hazard = sim["hazard_zones"]
                sim_explosions = sim["explosions"]
                if sim_pos not in sim_explosions and (sim_pos not in sim_hazard or sim_hazard[sim_pos] > 1):
                    safe_moves.append(action)

            # Chọn ngẫu nhiên một hành động an toàn làm đột biến
            if safe_moves:
                chosen_action = random.choice(safe_moves)
            else:
                # Nếu không có hành động nào an toàn tuyệt đối, chọn ngẫu nhiên hành động hợp lệ bất kỳ
                valid_moves = [a for a, _, _ in successors]
                if valid_moves:
                    chosen_action = random.choice(valid_moves)
                else:
                    chosen_action = "WAIT"

        return chosen_action
