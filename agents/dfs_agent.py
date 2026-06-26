"""DFS Agent - Depth-First Search agent for Bomberman.

Triết lý thiết kế:
  DFS là cơ chế QUYẾT ĐỊNH TRUNG TÂM. Mỗi bước, agent xây dựng một
  unified goal set gồm tất cả tile đáng đến, rồi gọi MỘT lần DFS duy nhất
  để tìm một tile trong goal set. Ràng buộc nguy hiểm được encode trực tiếp
  vào điều kiện duyệt node.

So sánh DFS vs BFS:
  - BFS (Queue FIFO): duyệt theo lớp, đảm bảo tìm đường đi ngắn nhất.
  - DFS (Stack LIFO): đi sâu theo một hướng trước khi backtrack, KHÔNG đảm bảo
    đường đi ngắn nhất (agent có thể đi vòng, circuitous route).
"""
import gc
from typing import List, Tuple, Set, Dict, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state




def is_safe_tile(pos, hazard_zones, explosions) -> bool:
    """Return True if the tile is safe (no active explosion and not in hazard zone)."""
    return pos not in hazard_zones and pos not in explosions


def path_to_action(path) -> str:
    """Convert path (list of positions) to first action string."""
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
    """Return True if placing a bomb at `pos` would hit an enemy or brick."""
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
    DFS thuần túy (LIFO stack, không heuristic) từ `start` đến một tile
    trong `goal_set`. Trả về đường đi (list of positions) hoặc None.

    Đặc trưng của DFS (so với BFS):
      - Sử dụng Stack LIFO (danh sách Python với append/pop) thay vì Queue FIFO.
      - Goal test được thực hiện khi POP khỏi stack (theo chuẩn sách giáo khoa).
      - DFS không đảm bảo tìm được đường đi ngắn nhất (có thể đi vòng,
        đi sâu hết mức trước khi backtrack).

    Ràng buộc được encode trực tiếp vào điều kiện duyệt node:
      - Tường / gạch                        → không expand.
      - Tile đang có explosion               → không expand.
      - Tile trong blast zone timer <= 1     → không expand.
      - Tile có bomb đang đặt               → không expand (trừ vị trí xuất phát).

    Tham số `danger_mode`:
      - False (mặc định): tránh toàn bộ hazard zone (bao gồm timer > 1).
      - True: DFS thoát nguy hiểm — cho phép đi qua hazard zone có timer > 1
              để tìm lối ra; vẫn chặn explosion và timer <= 1.
    """
    if not goal_set:
        return None

    # Tập bomb positions để kiểm tra không đi vào ô có bomb
    bomb_positions = {(bx, by) for bx, by, _ in bombs}

    # --- Khởi tạo frontier (stack LIFO) và visited ---
    frontier = []
    frontier.append((start, [start]))   # mỗi phần tử: (node, path_đến_node)
    visited = {start}

    # --- Vòng lặp DFS: duyệt theo chiều sâu sử dụng stack LIFO ---
    while frontier:
        node, path = frontier.pop()     # LIFO pop từ cuối danh sách

        # --- Goal test: kiểm tra ngay khi dequeue/pop (chuẩn sách giáo khoa) ---
        if node in goal_set:
            return path

        cx, cy = node

        # --- Expand: sinh ra các láng giềng 4 hướng ---
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            neighbor = (nx, ny)

            # Ràng buộc 1: trong giới hạn bản đồ
            if not (0 <= nx < width and 0 <= ny < height):
                continue

            # Ràng buộc 2: không phải tường hoặc gạch (không thể đi qua)
            if neighbor in walls or neighbor in bricks:
                continue

            # Ràng buộc 3: không đi vào ô có bomb (trừ vị trí xuất phát)
            if neighbor in bomb_positions and neighbor != start:
                continue

            # Ràng buộc 4: không đi vào ô đang có explosion
            if neighbor in explosions:
                continue

            # Ràng buộc 5: không đi vào blast zone sắp nổ (timer <= 1)
            if neighbor in hazard_zones and hazard_zones[neighbor] <= 1:
                continue

            # Ràng buộc 6 (chỉ khi không phải danger_mode):
            # tránh toàn bộ blast zone (kể cả timer > 1)
            if not danger_mode and neighbor in hazard_zones:
                continue

            # Đưa vào stack và đánh dấu visited ngay khi push để tránh duplicate
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append((neighbor, path + [neighbor]))

    return None   # không tìm được đường đến bất kỳ goal nào


class DFSAgent(BaseAgent):
    """
    DFS Agent — Depth-First Search là cơ chế quyết định trung tâm.

    Mỗi bước:
      1. Xây dựng UNIFIED GOAL SET: tập hợp tất cả tile đáng đến
         (safe tiles khi nguy hiểm, item tiles, enemy-adjacent, brick-adjacent).
      2. Gọi MỘT lần dfs() duy nhất → tìm tile trong goal set.
      3. Nếu đã đứng tại goal (cạnh enemy/brick) và có escape → đặt BOMB.
      4. Không có heuristic, không có priority chain, không có weighted score.

    DFS KHÔNG đảm bảo đường đi ngắn nhất (có thể đi vòng do tính chất LIFO stack).
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

        current_sim = simulate_state(info, "WAIT")
        current_score = evaluate_state(current_sim)

        # DFS Search using stack: (sim_state, path_of_actions, depth)
        stack = [(info, [], 0)]
        
        best_action = "WAIT"
        best_score = current_score
        depth_limit = 3
        
        while stack:
            curr_state, path, depth = stack.pop()
            
            # Evaluate current node's simulated state if not root
            if depth > 0:
                score = evaluate_state(curr_state)
                if score > best_score:
                    best_score = score
                    best_action = path[0] if path else "WAIT"
                
            if depth >= depth_limit:
                continue
                
            # Generate valid actions from curr_state
            c_px, c_py = curr_state["player_pos"]
            c_walls = curr_state["walls"]
            c_bricks = curr_state["bricks"]
            c_bombs = curr_state["bombs"]
            c_ammo = curr_state["ammo"]
            c_width = curr_state["width"]
            c_height = curr_state["height"]
            
            c_bomb_positions = {(bx, by) for bx, by, _ in c_bombs}
            
            # BOMB (push to stack first, so it is evaluated after movement LIFO)
            if c_ammo > 0 and (c_px, c_py) not in c_bomb_positions:
                sim = simulate_state(curr_state, "BOMB")
                stack.append((sim, path + ["BOMB"], depth + 1))
            
            # Movements
            for action, dx, dy in [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]:
                nx, ny = c_px + dx, c_py + dy
                if 0 <= nx < c_width and 0 <= ny < c_height:
                    if (nx, ny) not in c_walls and (nx, ny) not in c_bricks:
                        if (nx, ny) not in c_bomb_positions or (nx, ny) == (c_px, c_py):
                            sim = simulate_state(curr_state, action)
                            stack.append((sim, path + [action], depth + 1))
                            
            # WAIT
            wait_sim = simulate_state(curr_state, "WAIT")
            stack.append((wait_sim, path + ["WAIT"], depth + 1))
            
        return best_action
