"""
Expectimax Agent - Agent Expectimax cho game Bomberman.

Triết lý thiết kế:
  Expectimax khác biệt so với Minimax ở chỗ: Nó không giả định đối thủ luôn đưa ra lựa chọn tối ưu nhất để hãm hại mình.
  Thay vào đó, nó giả định môi trường hoặc kẻ địch hành động mang tính ngẫu nhiên (stochastic).
  - Lượt của Agent (MAX node): Chọn hành động tối đa hóa điểm số dự kiến.
  - Lượt của Kẻ địch (CHANCE node): Tính giá trị trung bình (kỳ vọng toán học) của điểm số trên tất cả các hành động khả thi
    của kẻ địch (với phân phối xác suất đều - Uniform Distribution).
    
  Điều này rất phù hợp khi kẻ địch di chuyển ngẫu nhiên hoặc không hoàn hảo, giúp agent đưa ra các quyết định thực tế hơn.
"""
from typing import List, Tuple, Dict, Any
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state, get_hazard_zones

def get_valid_actions(state_info: dict) -> List[str]:
    """Lấy tất cả hành động hợp lệ về vật lý của người chơi."""
    px, py = state_info["player_pos"]
    walls = state_info["walls"]
    bricks = state_info["bricks"]
    bombs = state_info["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = state_info["width"], state_info["height"]

    valid = ["WAIT"]

    # Các hướng di chuyển
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
    """Lấy tất cả vị trí tiếp theo khả thi của kẻ địch."""
    ex, ey = enemy_pos
    walls = state_info["walls"]
    bricks = state_info["bricks"]
    bombs = state_info["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = state_info["width"], state_info["height"]

    valid_positions = [(ex, ey)] # Đứng yên luôn hợp lệ

    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = ex + dx, ey + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid_positions.append((nx, ny))

    return valid_positions

class ExpectimaxAgent(BaseAgent):
    """
    ExpectimaxAgent sử dụng thuật toán Expectimax giới hạn độ sâu (depth = 5).
    """

    def __init__(self, depth: int = 5):
        self.depth = depth

    def evaluate_state_adversarial(self, sim_state: dict) -> float:
        """Hàm lượng giá mở rộng cho đối kháng, phạt theo khoảng cách đến quái nếu xa."""
        base_score = evaluate_state(sim_state)
        enemies = sim_state.get("enemies")
        if enemies:
            px, py = sim_state["player_pos"]
            min_dist_enemy = min(abs(px - ex) + abs(py - ey) for ex, ey in enemies)
            if min_dist_enemy > 4:
                base_score -= (min_dist_enemy ** 2) * 20.0
        return base_score

    def choose_action(self, state: dict) -> str:
        state_info = parse_state(state)
        
        # Xác định các hành động hợp lệ tại gốc
        legal_actions = state.get("legal_actions")
        valid_actions = get_valid_actions(state_info)
        if legal_actions:
            valid_actions = [a for a in valid_actions if a in legal_actions]
        if not valid_actions:
            valid_actions = ["WAIT"]

        best_action = "WAIT"
        best_score = -float('inf')

        # Nút gốc Expectimax (MAX node)
        for action in valid_actions:
            next_state = simulate_state(state_info, action)
            # Gọi nút cơ hội (CHANCE node) cho đối thủ ở tầng tiếp theo
            score = self.chance_value(next_state, self.depth - 1)
            
            if score > best_score:
                best_score = score
                best_action = action
            
        return best_action

    def max_value(self, state: dict, depth: int) -> float:
        """MAX node: Chọn hành động tối đa hóa giá trị kỳ vọng nhận được."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return self.evaluate_state_adversarial(state)

        valid_actions = get_valid_actions(state)
        if not valid_actions:
            return self.evaluate_state_adversarial(state)

        v = -float('inf')
        for action in valid_actions:
            next_state = simulate_state(state, action)
            v = max(v, self.chance_value(next_state, depth - 1))
        return v

    def chance_value(self, state: dict, depth: int) -> float:
        """CHANCE node: Tính giá trị kỳ vọng trung bình dựa trên mọi hành động khả thi của kẻ địch."""
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return self.evaluate_state_adversarial(state)

        enemies = state["enemies"]
        if not enemies:
            # Nếu không có kẻ địch, chuyển tiếp thành MAX node bình thường
            return self.max_value(state, depth - 1)

        # Mô hình hóa kẻ địch ngẫu nhiên: Tìm kẻ địch gần người chơi nhất
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

        # Tính trung bình cộng của tất cả các kết quả láng giềng (xác suất đồng đều)
        total_value = 0.0
        for next_pos in valid_moves:
            next_state = {**state}
            next_state["enemies"] = list(state["enemies"])
            next_state["enemies"][closest_idx] = next_pos
            
            # CẬP NHẬT ĐỒNG BỘ HAZARD ZONES TẠI ĐÂY
            next_state["hazard_zones"] = get_hazard_zones(
                next_state["bombs"], 
                next_state["walls"], 
                next_state["bricks"], 
                next_state["blast_radius"], 
                next_state["width"], 
                next_state["height"],
                next_state.get("bomb_ranges", {})
            )
            
            total_value += self.max_value(next_state, depth - 1)

        return total_value / len(valid_moves)
