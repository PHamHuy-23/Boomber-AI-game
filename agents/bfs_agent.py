"""
BFS Agent - Agent tìm kiếm theo chiều rộng (Breadth-First Search) cho game Bomberman.

Triết lý thiết kế:
  BFS được dùng để duyệt cây trạng thái mô phỏng lên đến độ sâu 3 (depth_limit = 3).
  Mỗi bước, agent tạo hàng đợi FIFO chứa các trạng thái giả lập tiếp theo (gồm di chuyển, đặt bom, chờ).
  Nó chọn nước đi đầu tiên của chuỗi hành động dẫn tới trạng thái mô phỏng có điểm số heuristic cao nhất.
"""
import gc
from collections import deque
from typing import List, Tuple, Set, Dict, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def is_safe_tile(pos, hazard_zones, explosions) -> bool:
    """Trả về True nếu ô đó an toàn (không có vụ nổ hoạt động và không nằm trong vùng nguy hiểm từ bom)."""
    return pos not in hazard_zones and pos not in explosions

def bfs(start: Tuple[int, int],
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
    BFS trên lưới bản đồ 2D (Sử dụng Queue FIFO, không dùng heuristic).
    Tìm đường đi từ điểm `start` đến ô gần nhất trong `goal_set`.
    Trả về danh sách các ô tạo nên đường đi (path) hoặc None nếu không tìm thấy.

    Các ràng buộc bản đồ được kiểm tra trực tiếp:
      - Tránh tường, gạch.
      - Tránh ô có bom đang đặt (trừ ô xuất phát).
      - Tránh vùng đang có lửa nổ.
      - Tránh vùng nguy hiểm sắp nổ (timer <= 1).
      - danger_mode = True: Cho phép đi qua vùng nguy hiểm (timer > 1) để tìm lối thoát.
    """
    if not goal_set:
        return None

    bomb_positions = {(bx, by) for bx, by, _ in bombs}

    # Hàng đợi FIFO: mỗi phần tử lưu (tọa độ hiện tại, đường đi từ start đến tọa độ này)
    frontier: deque = deque()
    frontier.append((start, [start]))
    visited: Set[Tuple[int, int]] = {start}

    while frontier:
        node, path = frontier.popleft() # Lấy ở đầu hàng đợi (FIFO)

        # Kiểm traích (Goal test) ngay khi dequeue
        if node in goal_set:
            return path

        cx, cy = node

        # Duyệt các ô láng giềng theo 4 hướng
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            neighbor = (nx, ny)

            # Ràng buộc 1: Trong bản đồ
            if not (0 <= nx < width and 0 <= ny < height):
                continue

            # Ràng buộc 2: Không đi vào tường hoặc gạch
            if neighbor in walls or neighbor in bricks:
                continue

            # Ràng buộc 3: Không đi vào ô có bom (trừ ô xuất phát)
            if neighbor in bomb_positions and neighbor != start:
                continue

            # Ràng buộc 4: Không đi vào ô đang nổ
            if neighbor in explosions:
                continue

            # Ràng buộc 5: Tránh vùng sắp nổ ngay lập tức (timer <= 1)
            if neighbor in hazard_zones and hazard_zones[neighbor] <= 1:
                continue

            # Ràng buộc 6: Tránh vùng nguy hiểm (timer > 1) trừ khi đang ở chế độ nguy cấp (danger_mode)
            if not danger_mode and neighbor in hazard_zones:
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append((neighbor, path + [neighbor]))

    return None

def path_to_action(path) -> str:
    """Chuyển đổi đường đi (danh sách tọa độ) thành hành động di chuyển đầu tiên của người chơi."""
    if not path or len(path) < 2:
        return "WAIT"
    (cx, cy) = path[0]
    (nx, ny) = path[1]
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
    """Trả về True nếu đặt bom tại `pos` có thể phá hủy gạch hoặc tiêu diệt kẻ địch."""
    px, py = pos
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for dist in range(1, blast_radius + 1):
            tx, ty = px + dx * dist, py + dy * dist
            if not (0 <= tx < width and 0 <= ty < height):
                break
            if (tx, ty) in walls:
                break
            if any(abs(tx - ex) + abs(ty - ey) == 0 for ex, ey in enemies):
                return True
            if (tx, ty) in bricks:
                return True
    return False

class BFSAgent(BaseAgent):
    """
    BFSAgent sử dụng thuật toán Tìm kiếm theo chiều rộng (BFS) trên cây trạng thái mô phỏng.
    Nó duyệt qua tất cả các chuỗi hành động có thể (lên, xuống, trái, phải, đặt bom, chờ) lên đến 3 bước.
    """

    def choose_action(self, state: dict) -> str:
        # --- Phân tích trạng thái game hiện tại ---
        info = parse_state(state)
        px, py = info["player_pos"]
        walls = info["walls"]
        bricks = info["bricks"]
        bombs = info["bombs"]
        ammo = info["ammo"]
        width = info["width"]
        height = info["height"]

        # Mô phỏng hành động WAIT ở trạng thái hiện tại để lấy điểm số ban đầu làm mốc so sánh
        current_sim = simulate_state(info, "WAIT")
        current_score = evaluate_state(current_sim)

        # Hàng đợi FIFO để duyệt cây hành động mô phỏng: (sim_state, danh_sách_hành_động, độ_sâu_tìm_kiếm)
        queue = deque([(info, [], 0)])
        
        best_action = "WAIT"
        best_score = current_score
        depth_limit = 3 # Giới hạn độ sâu mô phỏng 3 bước đi để đảm bảo hiệu năng
        
        while queue:
            curr_state, path, depth = queue.popleft() # Lấy phần tử ở đầu hàng đợi (FIFO)
            
            # Đánh giá trạng thái mô phỏng nếu không phải là nút gốc (độ sâu > 0)
            if depth > 0:
                score = evaluate_state(curr_state)
                # Cập nhật hành động tốt nhất nếu tìm thấy trạng thái mô phỏng có điểm số cao hơn
                if score > best_score:
                    best_score = score
                    best_action = path[0] if path else "WAIT"
                
            if depth >= depth_limit:
                continue
                
            # Tạo các trạng thái tiếp theo khả thi từ trạng thái đang xét
            c_px, c_py = curr_state["player_pos"]
            c_walls = curr_state["walls"]
            c_bricks = curr_state["bricks"]
            c_bombs = curr_state["bombs"]
            c_ammo = curr_state["ammo"]
            c_width = curr_state["width"]
            c_height = curr_state["height"]
            
            c_bomb_positions = {(bx, by) for bx, by, _ in c_bombs}
            
            # 1. Nhánh WAIT (Chờ)
            wait_sim = simulate_state(curr_state, "WAIT")
            queue.append((wait_sim, path + ["WAIT"], depth + 1))
            
            # 2. Nhánh di chuyển (UP, DOWN, LEFT, RIGHT)
            for action, dx, dy in [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]:
                nx, ny = c_px + dx, c_py + dy
                # Kiểm tra xem ô tiếp theo có đi được không (nằm trong bản đồ, không là tường/gạch, không có bom)
                if 0 <= nx < c_width and 0 <= ny < c_height:
                    if (nx, ny) not in c_walls and (nx, ny) not in c_bricks:
                        if (nx, ny) not in c_bomb_positions or (nx, ny) == (c_px, c_py):
                            sim = simulate_state(curr_state, action)
                            queue.append((sim, path + [action], depth + 1))
                            
            # 3. Nhánh BOMB (Đặt bom nếu còn đạn và chưa có bom tại vị trí đứng)
            if c_ammo > 0 and (c_px, c_py) not in c_bomb_positions:
                sim = simulate_state(curr_state, "BOMB")
                queue.append((sim, path + ["BOMB"], depth + 1))
                
        return best_action
