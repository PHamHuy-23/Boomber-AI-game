"""
Simulated Annealing Agent - Agent luyện kim (Simulated Annealing) cho game Bomberman.

Triết lý thiết kế:
  Simulated Annealing là một thuật toán tìm kiếm cục bộ tối ưu hóa.
  Tương tự như Leo đồi (Hill Climbing) nhưng thông minh hơn ở chỗ: nó chấp nhận các nước đi
  "tệ hơn" với một xác suất nhất định là exp(ΔE / T) để giúp agent thoát khỏi cực trị cục bộ (local optima).
  
  Nhiệt độ T (Temperature) ban đầu được thiết lập cao (khuyến khích khám phá ngẫu nhiên), sau đó giảm dần
  theo tỷ lệ làm nguội (cooling_rate). Khi T tiến dần về mức tối thiểu (min_temp), thuật toán chuyển dần
  từ khám phá (exploration) sang khai thác (exploitation).
"""
import gc
import math
import random
from collections import deque
from typing import Tuple, Dict, Set, List
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def get_hazard_zones(bombs, walls, bricks, blast_radius, width, height) -> Dict:
    """Xác định các vùng nguy hiểm bị ảnh hưởng bởi bom."""
    hazard = {}
    for bx, by, timer in bombs:
        if (bx, by) not in hazard or timer < hazard[(bx, by)]:
            hazard[(bx, by)] = timer
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for dist in range(1, blast_radius + 1):
                tx, ty = bx + dx * dist, by + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls:
                    break
                if (tx, ty) not in hazard or timer < hazard[(tx, ty)]:
                    hazard[(tx, ty)] = timer
                if (tx, ty) in bricks:
                    break
    return hazard

def bfs_escape(start, walls, bricks, bombs, explosions, hazard_zones, width, height) -> str:
    """Dùng BFS để tìm hướng đi đầu tiên thoát khỏi vùng nguy hiểm hazard_zones."""
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        (cx, cy), path = queue.popleft()
        # Tìm thấy một ô an toàn (không nguy hiểm, không có nổ)
        if (cx, cy) not in hazard_zones and (cx, cy) not in explosions:
            return path[0] if path else "WAIT"
        for dx, dy, action in [(0, -1, "UP"), (0, 1, "DOWN"), (-1, 0, "LEFT"), (1, 0, "RIGHT")]:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if (nx, ny) in walls or (nx, ny) in bricks:
                continue
            if (nx, ny) in bomb_positions and (nx, ny) != start:
                continue
            if (nx, ny) in explosions:
                continue
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [action]))
    return "WAIT"

def should_place_bomb(pos, enemies, bricks, walls, blast_radius, width, height) -> bool:
    """Trả về True nếu đặt bom ở vị trí hiện tại có thể gây sát thương cho địch hoặc phá gạch."""
    px, py = pos
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for dist in range(1, blast_radius + 1):
            tx, ty = px + dx * dist, py + dy * dist
            if not (0 <= tx < width and 0 <= ty < height):
                break
            if (tx, ty) in walls:
                break
            if any(tx == ex and ty == ey for ex, ey in enemies):
                return True
            if (tx, ty) in bricks:
                return True
    return False

class SimulatedAnnealingAgent(BaseAgent):
    """
    SimulatedAnnealingAgent mô phỏng thuật toán luyện kim (Simulated Annealing) chuẩn sách giáo khoa.
    Tìm kiếm trên không gian đường đi hoàn chỉnh độ dài 4 bước bằng cách biến đổi (đột biến) hành động.
    """

    def __init__(self, initial_temp: float = 100.0, cooling_rate: float = 0.95, min_temp: float = 0.05, max_iterations: int = 150):
        super().__init__()
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp
        self.max_iterations = max_iterations

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
        
        best_path = list(current_path)
        best_score = current_score
        
        temp = self.initial_temp
        domain = ["WAIT", "UP", "DOWN", "LEFT", "RIGHT", "BOMB"]
        
        # Vòng lặp tối ưu hóa Simulated Annealing
        for _ in range(self.max_iterations):
            if temp < self.min_temp:
                break
                
            # Tạo đường đi láng giềng bằng cách thay đổi ngẫu nhiên một hành động trong chuỗi
            neighbor_path = list(current_path)
            mutate_idx = random.randint(0, len(current_path) - 1)
            new_action = random.choice([a for a in domain if a != current_path[mutate_idx]])
            neighbor_path[mutate_idx] = new_action
            
            neighbor_score = self.evaluate_path(neighbor_path, info)
            delta_e = neighbor_score - current_score
            
            if delta_e > 0:
                current_path = neighbor_path
                current_score = neighbor_score
                if current_score > best_score:
                    best_score = current_score
                    best_path = list(current_path)
            else:
                prob = math.exp(delta_e / temp)
                if random.random() < prob:
                    current_path = neighbor_path
                    current_score = neighbor_score
                    
            temp *= self.cooling_rate
            
        return best_path[0]
