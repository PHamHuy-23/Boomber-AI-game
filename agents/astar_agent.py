"""
A* Agent - Agent tìm kiếm A* (A-Star Search) cho game Bomberman.

Triết lý thiết kế:
  A* tìm kiếm trên cây trạng thái mô phỏng bằng cách dùng hàng đợi ưu tiên (Priority Queue / Min-Heap).
  Độ ưu tiên được tính bằng công thức: f(n) = g(n) + h(n)
    - g(n) = W * depth (chi phí tích lũy để đi đến độ sâu hiện tại, với W = 100.0)
    - h(n) = -evaluate_state(sim_state) (ước lượng chi phí còn lại, giá trị âm của điểm số heuristic)
  Điều này giúp agent tìm kiếm hành động tối ưu một cách hiệu quả hơn bằng cách bỏ qua các nhánh trạng thái kém hứa hẹn.
"""
import gc
import heapq
from collections import deque
from typing import List, Tuple, Set, Dict, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def is_safe_tile(pos, hazard_zones, explosions) -> bool:
    """Trả về True nếu ô đó an toàn (không nổ, không nằm trong vùng bom đe dọa)."""
    return pos not in hazard_zones and pos not in explosions

def manhattan(a, b) -> int:
    """Tính khoảng cách Manhattan giữa hai điểm a và b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start: Tuple[int, int],
          goal_set: Set[Tuple[int, int]],
          walls: set,
          bricks: set,
          bombs: list,
          explosions: set,
          hazard_zones: Dict[Tuple[int, int], int],
          width: int,
          height: int,
          danger_mode: bool = False) -> Optional[List[Tuple[int, int]]]:
    """
    Thuật toán tìm kiếm A* trên lưới bản đồ 2D.
    Tìm đường đi ngắn nhất từ `start` tới ô tối ưu trong `goal_set`.
    
    Công thức: f(n) = g(n) + h(n)
      - g(n): số bước thực tế từ start đến ô hiện tại.
      - h(n): khoảng cách Manhattan ngắn nhất tới bất kỳ ô đích nào trong goal_set.
    """
    if not goal_set:
        return None

    bomb_positions = {(bx, by) for bx, by, _ in bombs}

    # Hàm heuristic ước lượng khoảng cách tới đích gần nhất
    def heuristic(pos: Tuple[int, int]) -> int:
        return min(abs(pos[0] - g[0]) + abs(pos[1] - g[1]) for g in goal_set)

    # open_heap lưu tuple: (f_score, g_score, x, y)
    start_h = heuristic(start)
    open_heap = []
    heapq.heappush(open_heap, (start_h, 0, start[0], start[1]))

    g_score = {start: 0}
    came_from = {}
    closed_set = set()

    while open_heap:
        f, g_heap, cx, cy = heapq.heappop(open_heap)
        current = (cx, cy)

        if current in closed_set:
            continue
        closed_set.add(current)

        # Kiểm tra đích khi POP để đảm bảo đường đi tối ưu nhất
        if current in goal_set:
            path = []
            node = current
            while node != start:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return list(reversed(path))

        g = g_score.get(current, float('inf'))

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            neighbor = (nx, ny)

            # Kiểm tra các ràng buộc bản đồ
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if neighbor in walls or neighbor in bricks:
                continue
            if neighbor in bomb_positions and neighbor != start:
                continue
            if neighbor in explosions:
                continue
            if neighbor in hazard_zones and hazard_zones[neighbor] <= 1:
                continue
            if not danger_mode and neighbor in hazard_zones:
                continue

            if neighbor in closed_set:
                continue

            tentative_g = g + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                h_val = heuristic(neighbor)
                # Đưa vào heap với độ ưu tiên f = tentative_g + h_val
                heapq.heappush(open_heap, (tentative_g + h_val, tentative_g, nx, ny))

    return None

def path_to_action(path) -> str:
    """Chuyển đổi đường đi thành hành động di chuyển đầu tiên."""
    if not path or len(path) < 2:
        return "WAIT"
    cx, cy = path[0]
    nx, ny = path[1]
    if nx == cx - 1:
        return "LEFT"
    if nx == cx + 1:
        return "RIGHT"
    if ny == cy - 1:
        return "UP"
    if ny == cy + 1:
        return "DOWN"
    return "WAIT"

def should_place_bomb(pos, enemies, bricks, walls, blast_radius, width, height) -> bool:
    """Kiểm tra xem đặt bom tại vị trí này có hiệu quả hay không."""
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

class AStarAgent(BaseAgent):
    """
    AStarAgent tìm kiếm trên cây trạng thái mô phỏng bằng thuật toán A*.
    Sử dụng hàng đợi ưu tiên để luôn mở rộng trạng thái tiềm năng nhất.
    """

    def choose_action(self, state: dict) -> str:
        # --- Phân tích trạng thái ---
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]
        bricks = info["bricks"]
        bombs = info["bombs"]
        ammo = info["ammo"]
        width = info["width"]
        height = info["height"]

        # Điểm của trạng thái WAIT hiện tại
        current_sim = simulate_state(info, "WAIT")
        current_score = evaluate_state(current_sim)
        
        # W = Trọng số phạt cho mỗi bước đi sâu hơn (tương ứng g(n))
        W = 100.0
        open_heap = []
        counter = 0
        # Đưa trạng thái gốc vào hàng đợi: (f_value, counter, sim_state, path, depth)
        heapq.heappush(open_heap, (-current_score, counter, info, [], 0))
        
        best_action = "WAIT"
        best_score = current_score
        depth_limit = 4 # Độ sâu tối đa mô phỏng 4 bước
        max_expansions = 100 # Giới hạn số nút được duyệt để bảo đảm thời gian thực tế
        expansions = 0
        
        while open_heap and expansions < max_expansions:
            priority, _, curr_state, path, depth = heapq.heappop(open_heap)
            expansions += 1
            
            if depth > 0:
                score = evaluate_state(curr_state)
            else:
                score = current_score

            # Cập nhật hành động tốt nhất nếu đạt điểm cao hơn
            if score > best_score:
                best_score = score
                best_action = path[0] if path else "WAIT"
                
            if depth >= depth_limit:
                continue
                
            # Tạo các trạng thái tiếp theo khả thi
            c_px, c_py = curr_state["player_pos"]
            c_walls = curr_state["walls"]
            c_bricks = curr_state["bricks"]
            c_bombs = curr_state["bombs"]
            c_ammo = curr_state["ammo"]
            c_width = curr_state["width"]
            c_height = curr_state["height"]
            
            c_bomb_positions = {(bx, by) for bx, by, _ in c_bombs}
            
            # 1. Hành động WAIT
            wait_sim = simulate_state(curr_state, "WAIT")
            wait_score = evaluate_state(wait_sim)
            # f(n) = W * depth - score
            wait_priority = W * (depth + 1) - wait_score
            counter += 1
            heapq.heappush(open_heap, (wait_priority, counter, wait_sim, path + ["WAIT"], depth + 1))
            
            # 2. Hành động di chuyển
            for action, dx, dy in [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]:
                nx, ny = c_px + dx, c_py + dy
                if 0 <= nx < c_width and 0 <= ny < c_height:
                    if (nx, ny) not in c_walls and (nx, ny) not in c_bricks:
                        if (nx, ny) not in c_bomb_positions or (nx, ny) == (c_px, c_py):
                            sim = simulate_state(curr_state, action)
                            sim_score = evaluate_state(sim)
                            sim_priority = W * (depth + 1) - sim_score
                            counter += 1
                            heapq.heappush(open_heap, (sim_priority, counter, sim, path + [action], depth + 1))
                            
            # 3. Hành động đặt BOMB
            if c_ammo > 0 and (c_px, c_py) not in c_bomb_positions:
                sim = simulate_state(curr_state, "BOMB")
                sim_score = evaluate_state(sim)
                sim_priority = W * (depth + 1) - sim_score
                counter += 1
                heapq.heappush(open_heap, (sim_priority, counter, sim, path + ["BOMB"], depth + 1))
                
        return best_action
