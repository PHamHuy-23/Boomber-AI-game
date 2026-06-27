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
    SimulatedAnnealingAgent mô phỏng thuật toán luyện kim trên không gian hành động.
    Duyệt ngẫu nhiên trên cây trạng thái giả lập lên tới độ sâu 4 và tối ưu hóa bằng nhiệt độ giảm dần.
    """

    def __init__(self, initial_temp: float = 50.0, cooling_rate: float = 0.97, min_temp: float = 1.0):
        super().__init__()
        self.temperature = initial_temp     # Nhiệt độ ban đầu
        self.cooling_rate = cooling_rate     # Tốc độ làm nguội (T = T * cooling_rate)
        self.min_temp = min_temp             # Nhiệt độ tối thiểu

    def choose_action(self, state: dict) -> str:
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]
        bricks = info["bricks"]
        bombs = info["bombs"]
        ammo = info["ammo"]
        width = info["width"]
        height = info["height"]

        bomb_positions = {(bx, by) for bx, by, _ in bombs}

        # Khởi tạo trạng thái mô phỏng ban đầu tại gốc
        root_sim = simulate_state(info, "WAIT")
        root_score = evaluate_state(root_sim)
        
        c_sim_state = info
        current_score = root_score
        current_path = []
        
        best_action = "WAIT"
        best_score = root_score
        
        temp = self.temperature
        num_iterations = 20 # Số lượt thử mô phỏng luyện kim ở mỗi tick
        depth_limit = 4     # Độ sâu tối đa mô phỏng
        
        for _ in range(num_iterations):
            # Nếu vượt quá giới hạn độ sâu, reset lại về trạng thái gốc để bắt đầu nhánh mới
            if len(current_path) >= depth_limit:
                c_sim_state = info
                current_score = root_score
                current_path = []
                
            # Sinh ra các hành động hợp lệ từ trạng thái hiện tại
            c_px, c_py = c_sim_state["player_pos"]
            c_walls = c_sim_state["walls"]
            c_bricks = c_sim_state["bricks"]
            c_bombs = c_sim_state["bombs"]
            c_ammo = c_sim_state["ammo"]
            c_width = c_sim_state["width"]
            c_height = c_sim_state["height"]
            
            c_bomb_positions = {(bx, by) for bx, by, _ in c_bombs}
            
            valid_actions = ["WAIT"]
            for action, dx, dy in [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]:
                nx, ny = c_px + dx, c_py + dy
                if 0 <= nx < c_width and 0 <= ny < c_height:
                    if (nx, ny) not in c_walls and (nx, ny) not in c_bricks:
                        if (nx, ny) not in c_bomb_positions or (nx, ny) == (c_px, c_py):
                            valid_actions.append(action)
            if c_ammo > 0 and (c_px, c_py) not in c_bomb_positions:
                valid_actions.append("BOMB")
                
            if not valid_actions:
                c_sim_state = info
                current_score = root_score
                current_path = []
                continue
                
            # Lựa chọn ngẫu nhiên một láng giềng làm ứng viên tiếp theo
            chosen_action = random.choice(valid_actions)
            neighbor_sim = simulate_state(c_sim_state, chosen_action)
            neighbor_score = evaluate_state(neighbor_sim)
            
            # Tính toán ΔE (Sự thay đổi về mặt chất lượng trạng thái)
            delta_e = neighbor_score - current_score
            accept = False
            
            if delta_e > 0:
                accept = True # Chấp nhận ngay nếu láng giềng tốt hơn
            else:
                # Nếu láng giềng tệ hơn, chấp nhận với xác suất Boltzmann P = exp(ΔE / T)
                prob = math.exp(delta_e / max(temp, 0.001))
                accept = random.random() < prob
                
            if accept:
                c_sim_state = neighbor_sim
                current_score = neighbor_score
                current_path.append(chosen_action)
                # Lưu giữ hành động tốt nhất lịch sử tìm kiếm được
                if current_score > best_score:
                    best_score = current_score
                    best_action = current_path[0]
                    
            # Giảm nhiệt độ dần dần (Cooling down)
            temp = max(self.min_temp, temp * self.cooling_rate)
            
        return best_action
