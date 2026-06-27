"""
AND-OR Search Agent - Agent tìm kiếm AND-OR cho game Bomberman.

Triết lý thiết kế:
  Tìm kiếm AND-OR được áp dụng trong môi trường không xác định (non-deterministic).
  - Nút OR (OR nodes): Đại diện cho quyết định của Agent. Agent muốn chọn hành động tốt nhất để tối đa hóa điểm số.
  - Nút AND (AND nodes): Đại diện cho các khả năng xảy ra của môi trường (ở đây là hành động của kẻ địch gần nhất).
    Agent phải chuẩn bị cho kịch bản xấu nhất (lấy giá trị tối thiểu - worst-case).
  
  Mục tiêu của Tìm kiếm AND-OR là tìm ra một kế hoạch dự phòng (contingent plan) đảm bảo an toàn và hiệu quả
  bất kể kẻ địch di chuyển như thế nào trong tình huống xấu nhất.
"""
from typing import List, Tuple, Dict, Any
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def get_valid_actions(state_info: dict) -> List[str]:
    """Lấy tất cả các hành động hợp lý về mặt vật lý của người chơi."""
    px, py = state_info["player_pos"]
    walls = state_info["walls"]
    bricks = state_info["bricks"]
    bombs = state_info["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = state_info["width"], state_info["height"]

    valid = ["WAIT"]

    # Di chuyển
    moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
    for action, (dx, dy) in moves.items():
        nx, ny = px + dx, py + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid.append(action)

    # Đặt bom
    if state_info["ammo"] > 0 and (px, py) not in bomb_positions:
        valid.append("BOMB")

    return valid

def get_enemy_valid_moves(enemy_pos: Tuple[int, int], state_info: dict) -> List[Tuple[int, int]]:
    """Lấy tất cả vị trí tiếp theo kẻ địch có thể đi tới."""
    ex, ey = enemy_pos
    walls = state_info["walls"]
    bricks = state_info["bricks"]
    bombs = state_info["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = state_info["width"], state_info["height"]

    valid_positions = [(ex, ey)]

    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = ex + dx, ey + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid_positions.append((nx, ny))

    return valid_positions

class AndOrSearchAgent(BaseAgent):
    """
    AndOrSearchAgent thực hiện tìm kiếm AND-OR lên tới độ sâu quy định (mặc định depth = 5).
    """

    def __init__(self, depth: int = 5):
        self.depth = depth

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        
        # Xác định các hành động hợp lệ
        legal_actions = state.get("legal_actions")
        valid_actions = get_valid_actions(state_info)
        if legal_actions:
            valid_actions = [a for a in valid_actions if a in legal_actions]
        if not valid_actions:
            valid_actions = ["WAIT"]

        best_action = "WAIT"
        best_score = -float('inf')

        # Nút OR đầu tiên (tại gốc): chọn hành động dẫn tới giá trị nút AND tốt nhất
        for action in valid_actions:
            next_state = simulate_state(state_info, action)
            score = self.and_node(next_state, self.depth - 1)
            
            if score > best_score:
                best_score = score
                best_action = action
            
        return best_action

    def or_node(self, state: dict, depth: int) -> float:
        """Nút OR: Người chơi chọn hành động tốt nhất để tối đa hóa điểm số."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return evaluate_state(state)

        valid_actions = get_valid_actions(state)
        if not valid_actions:
            return evaluate_state(state)

        v = -float('inf')
        for action in valid_actions:
            next_state = simulate_state(state, action)
            # Nút OR gọi nút AND kế tiếp
            v = max(v, self.and_node(next_state, depth - 1))
        return v

    def and_node(self, state: dict, depth: int) -> float:
        """Nút AND: Môi trường (kẻ địch) phản ứng. Ta tính toán dựa trên kịch bản xấu nhất (tối thiểu hóa)."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return evaluate_state(state)

        enemies = state["enemies"]
        if not enemies:
            # Nếu không có kẻ địch, chỉ có 1 nhánh phản ứng duy nhất từ môi trường (chuyển tiếp tới nút OR)
            return self.or_node(state, depth - 1)

        # Mô hình hóa kẻ địch gần nhất là nguồn gốc gây ra sự bất định của môi trường
        px, py = state["player_pos"]
        closest_idx = 0
        min_dist = float('inf')
        for idx, (ex, ey) in enumerate(enemies):
            dist = abs(px - ex) + abs(py - ey)
            if dist < min_dist:
                min_dist = dist
                closest_idx = idx

        enemy_pos = enemies[closest_idx]
        valid_moves = get_enemy_valid_moves(enemy_pos, state)

        # Trả về giá trị tệ nhất (min) trong tất cả các phản ứng có thể của kẻ địch
        v = float('inf')
        for next_pos in valid_moves:
            next_state = {**state}
            next_state["enemies"] = list(state["enemies"])
            next_state["enemies"][closest_idx] = next_pos
            
            v = min(v, self.or_node(next_state, depth - 1))

        return v if v != float('inf') else evaluate_state(state)
