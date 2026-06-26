"""A* Agent - A-Star Search agent for Bomberman."""
import gc
import heapq
from collections import deque
from typing import List, Tuple, Set, Dict, Optional
from agents import BaseAgent
from agents.search_utils import parse_state, simulate_state, evaluate_state




def is_safe_tile(pos, hazard_zones, explosions) -> bool:
    """Return True if the tile is safe (no active explosion and not in hazard zone)."""
    return pos not in hazard_zones and pos not in explosions


def manhattan(a, b) -> int:
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
    A* Search thuần túy (Priority Queue, heuristic Manhattan) từ `start`
    đến tile tối ưu nhất trong `goal_set`. Trả về đường đi (list of positions) hoặc None.

    Bản chất thuật toán A*:
      - Sử dụng Min-Heap (heapq) làm open_set để luôn expand node có f = g + h nhỏ nhất trước.
      - g(n): chi phí thực từ start đến node n (mỗi bước di chuyển = 1).
      - h(n): heuristic admissible (không đánh giá cao hơn thực tế) là Manhattan distance
              tới goal gần nhất trong goal_set.
      - closed_set: tập hợp các node đã được expand (popped khỏi heap) để tránh expand lại.
      - came_from: lưu quan hệ cha-con để reconstruct path, tránh lưu trữ path trực tiếp
                   trong heap làm phình to bộ nhớ (Memory O(V^2)).
      - Goal test: thực hiện khi POP node khỏi heap (chuẩn giáo khoa).

    Ràng buộc được encode trực tiếp vào điều kiện duyệt node:
      - Tường / gạch                        → không expand.
      - Tile đang có explosion               → không expand.
      - Tile trong blast zone timer <= 1     → không expand.
      - Tile có bomb đang đặt               → không expand (trừ vị trí xuất phát).

    Tham số `danger_mode`:
      - False (mặc định): tránh toàn bộ hazard zone (bao gồm timer > 1).
      - True: A* thoát nguy hiểm — cho phép đi qua hazard zone có timer > 1
              để tìm lối ra; vẫn chặn explosion và timer <= 1.
    """
    if not goal_set:
        return None

    bomb_positions = {(bx, by) for bx, by, _ in bombs}

    def heuristic(pos: Tuple[int, int]) -> int:
        return min(abs(pos[0] - g[0]) + abs(pos[1] - g[1]) for g in goal_set)

    # open_set chứa tuple: (f, g, x, y)
    # Dùng x, y để tiebreaking, tránh so sánh tuple chứa node/objects
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

        # Goal test khi POP (sau khi lọc closed_set để đảm bảo tối ưu)
        if current in goal_set:
            # Reconstruct path từ came_from
            path = []
            node = current
            while node != start:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return list(reversed(path))

        # Luôn lấy chi phí g_score tối ưu thực tế từ start thay vì g_heap trong tuple cũ
        g = g_score.get(current, float('inf'))

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

            if neighbor in closed_set:
                continue

            tentative_g = g + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                h_val = heuristic(neighbor)
                heapq.heappush(open_heap, (tentative_g + h_val, tentative_g, nx, ny))

    return None


def path_to_action(path) -> str:
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
    A* Agent — A-Star Search là cơ chế quyết định trung tâm.

    Mỗi bước:
      1. Xây dựng UNIFIED GOAL SET: tập hợp tất cả tile đáng đến
         (safe tiles khi nguy hiểm, item tiles, enemy-adjacent, brick-adjacent).
      2. Gọi MỘT lần astar() duy nhất → tìm tile tối ưu nhất trong goal set
         dựa trên f = g + h (Manhattan distance tới goal gần nhất).
      3. Nếu đã đứng tại goal (cạnh enemy/brick) VÀ có escape → đặt BOMB.
      4. A* expand node có f = g + h nhỏ nhất trước. Do h là admissible, A* đảm
         bảo tìm đường đi tối ưu nhanh hơn BFS (không duyệt mù quáng mọi hướng).
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

        # A* Search on state space tree
        # Priority = W * depth - evaluate_state(sim_state)
        current_sim = simulate_state(info, "WAIT")
        current_score = evaluate_state(current_sim)
        
        W = 100.0
        open_heap = []
        counter = 0
        heapq.heappush(open_heap, (-current_score, counter, info, [], 0))
        
        best_action = "WAIT"
        best_score = current_score
        depth_limit = 4
        max_expansions = 100
        expansions = 0
        
        while open_heap and expansions < max_expansions:
            priority, _, curr_state, path, depth = heapq.heappop(open_heap)
            expansions += 1
            
            if depth > 0:
                score = evaluate_state(curr_state)
            else:
                score = current_score

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
            
            # WAIT
            wait_sim = simulate_state(curr_state, "WAIT")
            wait_score = evaluate_state(wait_sim)
            wait_priority = W * (depth + 1) - wait_score
            counter += 1
            heapq.heappush(open_heap, (wait_priority, counter, wait_sim, path + ["WAIT"], depth + 1))
            
            # Movements
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
                            
            # BOMB
            if c_ammo > 0 and (c_px, c_py) not in c_bomb_positions:
                sim = simulate_state(curr_state, "BOMB")
                sim_score = evaluate_state(sim)
                sim_priority = W * (depth + 1) - sim_score
                counter += 1
                heapq.heappush(open_heap, (sim_priority, counter, sim, path + ["BOMB"], depth + 1))
                
        return best_action
