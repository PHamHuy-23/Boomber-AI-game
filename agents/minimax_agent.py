"""
Minimax Agent - Agent đối kháng Minimax với Cắt tỉa Alpha-Beta (Alpha-Beta Pruning) cho game Bomberman.

Triết lý thiết kế:
  Bomberman là một trò chơi mang tính đối kháng. Agent coi kẻ địch gần nhất là đối thủ (Adversary).
  - Lượt của Agent (MAX node): Chọn hành động tối đa hóa điểm số trạng thái của mình.
  - Lượt của Kẻ địch (MIN node): Giả định kẻ địch sẽ chọn hành động tồi tệ nhất đối với Agent (tối thiểu hóa điểm số của Agent).
  
  Cắt tỉa Alpha-Beta (Alpha-Beta Pruning) được tích hợp để bỏ qua các nhánh trạng thái không tối ưu,
  giúp tăng tốc độ tìm kiếm và cho phép duyệt sâu hơn (depth = 5).
"""
from typing import List, Tuple, Dict, Any
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state, get_hazard_zones

def get_valid_actions(state_info: dict) -> List[str]:
    """Lấy tất cả hành động hợp lệ về mặt vật lý của người chơi ở trạng thái hiện tại."""
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

    # Hành động đặt bom
    if state_info["ammo"] > 0 and (px, py) not in bomb_positions:
        valid.append("BOMB")

    return valid

def get_enemy_valid_moves(enemy_pos: Tuple[int, int], state_info: dict) -> List[Tuple[int, int]]:
    """Lấy tất cả vị trí tiếp theo khả thi của kẻ địch (gồm đứng yên và di chuyển sang 4 ô kề cạnh)."""
    ex, ey = enemy_pos
    walls = state_info["walls"]
    bricks = state_info["bricks"]
    bombs = state_info["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width, height = state_info["width"], state_info["height"]

    valid_positions = [(ex, ey)] # Đứng yên luôn khả thi

    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = ex + dx, ey + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                valid_positions.append((nx, ny))

    return valid_positions

class MinimaxAgent(BaseAgent):
    """
    MinimaxAgent sử dụng thuật toán Minimax giới hạn độ sâu kết hợp Cắt tỉa Alpha-Beta.
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

    def order_actions(self, valid_actions: List[str], state_info: dict) -> List[str]:
        """Sắp xếp các hành động để tối ưu hóa cắt tỉa Alpha-Beta."""
        px, py = state_info["player_pos"]
        hazard_zones = state_info.get("hazard_zones", {})
        in_hazard = (px, py) in hazard_zones
        
        escape_moves = []
        bomb_move = []
        normal_moves = []
        wait_move = []
        
        moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
        for action in valid_actions:
            if action == "WAIT":
                wait_move.append(action)
            elif action == "BOMB":
                bomb_move.append(action)
            elif action in moves:
                dx, dy = moves[action]
                nx, ny = px + dx, py + dy
                if in_hazard and (nx, ny) not in hazard_zones:
                    escape_moves.append(action)
                else:
                    normal_moves.append(action)
            else:
                normal_moves.append(action)
                
        return escape_moves + bomb_move + normal_moves + wait_move

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
        alpha = -float('inf') # Giá trị tốt nhất mà MAX node có thể đảm bảo
        beta = float('inf')   # Giá trị tốt nhất mà MIN node có thể đảm bảo

        self.nodes_expanded = 0
        action_scores = {}

        # Nút gốc của cây Minimax (MAX node)
        valid_actions = self.order_actions(valid_actions, state_info)
        for action in valid_actions:
            next_state = simulate_state(state_info, action)
            # Tính điểm số dự báo từ nút MIN phía dưới
            self.nodes_expanded += 1
            score = self.min_value(next_state, alpha, beta, self.depth - 1)
            action_scores[action] = score
            
            if score > best_score:
                best_score = score
                best_action = action
            
            # Cập nhật alpha
            alpha = max(alpha, best_score)
            
        self.last_trace = {
            "algorithm": "minimax",
            "nodes_expanded": self.nodes_expanded,
            "search_depth": self.depth,
            "evaluations": action_scores,
            "chosen_action": best_action,
            "reasoning": [
                f"Running Minimax Search (depth={self.depth})...",
                f"Total nodes evaluated: {self.nodes_expanded}",
                f"Candidate actions evaluated: " + ", ".join(f"{act}: {val:.1f}" for act, val in action_scores.items()),
                f"Chosen move: {best_action} (Utility: {best_score:.1f})"
            ]
        }
        return best_action

    def max_value(self, state: dict, alpha: float, beta: float, depth: int) -> float:
        """MAX node: Đại diện cho lựa chọn tối ưu của người chơi để tối đa hóa điểm số."""
        self.nodes_expanded += 1
        # Điều kiện dừng: đạt giới hạn độ sâu hoặc người chơi bị trúng nổ
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return self.evaluate_state_adversarial(state)

        valid_actions = get_valid_actions(state)
        if not valid_actions:
            return self.evaluate_state_adversarial(state)

        v = -float('inf')
        valid_actions = self.order_actions(valid_actions, state)
        for action in valid_actions:
            next_state = simulate_state(state, action)
            v = max(v, self.min_value(next_state, alpha, beta, depth - 1))
            # Cắt tỉa Alpha-Beta
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state: dict, alpha: float, beta: float, depth: int) -> float:
        """MIN node: Đại diện cho hành động đối kháng của đối thủ để tối thiểu hóa điểm số của người chơi."""
        self.nodes_expanded += 1
        if depth == 0 or state["player_pos"] in state["explosions"]:
            return self.evaluate_state_adversarial(state)

        enemies = state["enemies"]
        if not enemies:
            # Nếu không có kẻ địch trên bản đồ, chuyển tiếp thành MAX node ở lượt sau
            return self.max_value(state, alpha, beta, depth - 1)

        # Mô hình hóa đối thủ: Chọn kẻ địch có khoảng cách Manhattan gần người chơi nhất
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

        v = float('inf')
        for next_pos in valid_moves:
            # Giả lập vị trí di chuyển tiếp theo của kẻ địch trong trạng thái game
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
            
            # Tính toán nhánh MAX tiếp theo
            v = min(v, self.max_value(next_state, alpha, beta, depth - 1))
            # Cắt tỉa Alpha-Beta
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v