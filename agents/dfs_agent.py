"""
DFS Agent - Agent tìm kiếm theo chiều sâu (Depth-First Search) cho game Bomberman.

Triết lý thiết kế:
  DFS được dùng để duyệt cây trạng thái mô phỏng bằng cách sử dụng một Stack (LIFO)
  cho tới giới hạn độ sâu 3 (depth_limit = 3).
  Do tính chất LIFO, DFS đi sâu vào một nhánh hành động trước khi backtrack sang nhánh khác.
"""
import gc
from typing import List, Tuple, Set, Dict, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state

def is_safe_tile(pos, hazard_zones, explosions) -> bool:
    """Trả về True nếu ô đó an toàn (không có vụ nổ hoạt động và không nằm trong vùng nguy hiểm từ bom)."""
    return pos not in hazard_zones and pos not in explosions

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

def dfs(start: Tuple[int, int],
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
    DFS trên lưới bản đồ 2D (Sử dụng Stack LIFO, không dùng heuristic).
    Tìm đường đi từ điểm `start` đến một ô trong `goal_set`.
    Trả về danh sách các ô tạo nên đường đi (path) hoặc None nếu không tìm thấy.
    """
    if not goal_set:
        return None

    bomb_positions = {(bx, by) for bx, by, _ in bombs}

    # Stack LIFO: mỗi phần tử lưu (tọa độ hiện tại, đường đi từ start đến tọa độ này)
    frontier = []
    frontier.append((start, [start]))
    visited = {start}

    while frontier:
        node, path = frontier.pop() # Lấy phần tử cuối cùng của stack (LIFO)

        # Kiểm tra đích (Goal test) ngay khi pop
        if node in goal_set:
            return path

        cx, cy = node

        # Duyệt láng giềng theo 4 hướng
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            neighbor = (nx, ny)

            # Các ràng buộc bản đồ tương tự BFS
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

            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append((neighbor, path + [neighbor]))

    return None

class DFSAgent(BaseAgent):
    """
    DFSAgent sử dụng tìm kiếm theo chiều sâu (DFS) trên cây trạng thái mô phỏng.
    Nó sử dụng một Stack để lưu trữ và duyệt qua các chuỗi hành động tới độ sâu 3.
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

        # Điểm số của trạng thái WAIT hiện tại làm mốc ban đầu
        current_sim = simulate_state(info, "WAIT")
        current_score = evaluate_state(current_sim)

        # Stack LIFO để duyệt cây hành động mô phỏng: (sim_state, danh_sách_hành_động, độ_sâu)
        stack = [(info, [], 0)]
        
        best_action = "WAIT"
        best_score = current_score
        depth_limit = 3
        
        while stack:
            curr_state, path, depth = stack.pop() # Pop phần tử cuối cùng của stack (LIFO)
            
            # Đánh giá trạng thái mô phỏng
            if depth > 0:
                score = evaluate_state(curr_state)
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
            
            # 1. Nhánh BOMB (đưa vào đầu tiên để được lấy ra sau cùng trong LIFO)
            if c_ammo > 0 and (c_px, c_py) not in c_bomb_positions:
                sim = simulate_state(curr_state, "BOMB")
                stack.append((sim, path + ["BOMB"], depth + 1))
            
            # 2. Nhánh di chuyển
            for action, dx, dy in [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]:
                nx, ny = c_px + dx, c_py + dy
                if 0 <= nx < c_width and 0 <= ny < c_height:
                    if (nx, ny) not in c_walls and (nx, ny) not in c_bricks:
                        if (nx, ny) not in c_bomb_positions or (nx, ny) == (c_px, c_py):
                            sim = simulate_state(curr_state, action)
                            stack.append((sim, path + [action], depth + 1))
                            
            # 3. Nhánh WAIT (đưa vào sau cùng để được lấy ra trước tiên trong LIFO)
            wait_sim = simulate_state(curr_state, "WAIT")
            stack.append((wait_sim, path + ["WAIT"], depth + 1))
            
        return best_action
