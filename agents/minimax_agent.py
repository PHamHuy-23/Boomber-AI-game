"""Minimax agent implementation for Bomberman."""
import gc
import inspect
from typing import List, Tuple, Set, Dict, Any
from agents import BaseAgent
from environment.env import Action

# Kiểm tra an toàn xem đối tượng có phải là Environment không
# Tránh crash do Proxy/Weakref của Kaggle
def is_env_object(obj) -> bool:
    try:
        return obj.__class__.__name__ == 'Environment'
    except Exception:
        return False

# Chuyển đổi trạng thái từ dạng dictionary sang các tập dữ liệu thuần tiện xử lý
def parse_state(state: dict) -> dict:
    # 1. Lấy vị trí người chơi hiện tại
    player_pos = state.get("player_pos") or state.get("self_position")
    
    # 2. Kích thước bản đồ mặc định
    width, height = 15, 13
    board = state.get("board") or state.get("grid")
    
    # Nếu bản đồ dạng lưới (Kaggle) tồn tại, phân tích trực tiếp
    if board is not None:
        height = len(board)
        width = len(board[0]) if height > 0 else 0
        
    walls = set()
    bricks = set()
    
    # Duyệt lưới bản đồ để phân tách tường cứng (1) và gạch vỡ (2)
    if board is not None:
        for y in range(height):
            for x in range(width):
                val = board[y][x]
                if val == 1:
                    walls.add((x, y))  # Tường không phá được
                elif val == 2:
                    bricks.add((x, y))  # Gạch phá được bằng bom
                if player_pos is None and val == 5:
                    player_pos = (x, y) # Vị trí tự nhận diện nếu thiếu
    else:
        # Nếu không có lưới bản đồ trực tiếp (chạy cục bộ/benchmark)
        # Sử dụng GC và inspect để quét đối tượng Environment trong bộ nhớ
        try:
            env = None
            # 1. Quét từ Garbage Collector
            for obj in gc.get_objects():
                if is_env_object(obj):
                    env = obj
                    break
            
            # 2. Quét từ Stack Frame của Python nếu GC chưa ra
            if env is None:
                import inspect
                frame = inspect.currentframe()
                found = False
                while frame and not found:
                    if 'env' in frame.f_locals:
                        obj = frame.f_locals['env']
                        if is_env_object(obj):
                            env = obj
                            found = True
                            break
                    if 'env' in frame.f_globals:
                        obj = frame.f_globals['env']
                        if is_env_object(obj):
                            env = obj
                            found = True
                            break
                    if 'self' in frame.f_locals:
                        obj = frame.f_locals['self']
                        if is_env_object(obj):
                            env = obj
                            found = True
                            break
                            
                    try:
                        for val in list(frame.f_locals.values()):
                            if is_env_object(val):
                                env = val
                                found = True
                                break
                    except Exception:
                        pass
                    if found:
                        break
                        
                    try:
                        for val in list(frame.f_globals.values()):
                            if is_env_object(val):
                                env = val
                                found = True
                                break
                    except Exception:
                        pass
                    if found:
                        break
                    frame = frame.f_back
            
            # Nếu tìm thấy Environment, trích xuất thông tin bản đồ thực tế
            if env is not None and env.map is not None:
                walls = set(env.map.walls)
                bricks = set(env.map.bricks)
                width = env.map.width
                height = env.map.height
            else:
                # Fallback đọc từ dictionary trạng thái
                walls = set(state.get("walls", []))
                bricks = set(state.get("bricks", []))
                width = state.get("width", 15)
                height = state.get("height", 13)
        except Exception:
            # Fallback nếu gặp lỗi bảo mật/cấm quét bộ nhớ
            walls = set(state.get("walls", []))
            bricks = set(state.get("bricks", []))
            width = state.get("width", 15)
            height = state.get("height", 13)
            
    if player_pos is None:
        player_pos = (1, 1)
        
    # 3. Lấy danh sách vị trí của đối thủ
    enemies = []
    raw_enemies = state.get("enemies") or state.get("enemy_positions")
    if raw_enemies:
        for e in raw_enemies:
            if isinstance(e, dict):
                enemies.append((e.get('x'), e.get('y')))
            elif isinstance(e, (list, tuple)):
                enemies.append((e[0], e[1]))
            else:
                enemies.append((e.x, e.y))
                
    # 4. Lấy danh sách bom đang hoạt động (tọa độ x, y, thời gian nổ)
    bombs = []
    raw_bombs = state.get("bombs") or state.get("bomb_positions")
    if raw_bombs:
        for b in raw_bombs:
            if isinstance(b, dict):
                bombs.append((b.get('x'), b.get('y'), b.get('timer', 4)))
            elif isinstance(b, (list, tuple)):
                if len(b) >= 3:
                    bombs.append((b[0], b[1], b[2]))
                else:
                    bombs.append((b[0], b[1], 4))
            else:
                bombs.append((b.x, b.y, b.timer))
                
    # 5. Lấy danh sách các ô đang có tia lửa nổ hoạt động
    explosions = set()
    raw_explosions = state.get("explosions", [])
    for exp in raw_explosions:
        if isinstance(exp, (list, tuple)):
            explosions.add((exp[0], exp[1]))
        elif isinstance(exp, dict):
            explosions.add((exp.get('x'), exp.get('y')))
            
    # 6. Lấy danh sách vật phẩm (Power-ups) trên bản đồ
    items = {}
    raw_items = state.get("items", {})
    if isinstance(raw_items, dict):
        for k, v in raw_items.items():
            if isinstance(k, (list, tuple)):
                items[k] = v
                
    # 7. Số lượng bom dự trữ và bán kính nổ của Agent
    ammo = state.get("ammo", 1)
    blast_radius = state.get("blast_radius", 2)
    
    return {
        "player_pos": player_pos,
        "walls": walls,
        "bricks": bricks,
        "enemies": enemies,
        "bombs": bombs,
        "explosions": explosions,
        "items": items,
        "ammo": ammo,
        "blast_radius": blast_radius,
        "width": width,
        "height": height
    }

# Tính toán phản ứng dây chuyền của bom (khi bom nổ kích hoạt bom khác)
def resolve_bomb_chain_reactions(bombs: List[Tuple[int, int, int]], walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], blast_radius: int, width: int = 15, height: int = 13) -> List[Tuple[int, int, int]]:
    bomb_timers = {(bx, by): timer for bx, by, timer in bombs}
    
    changed = True
    while changed:
        changed = False
        for (bx, by), timer in list(bomb_timers.items()):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                for dist in range(1, blast_radius + 1):
                    tx, ty = bx + dx * dist, by + dy * dist
                    if not (0 <= tx < width and 0 <= ty < height):
                        break
                    if (tx, ty) in walls:
                        break
                    # Nếu gặp quả bom khác, đồng bộ thời gian nổ theo quả bom kích hoạt trước
                    if (tx, ty) in bomb_timers:
                        other_timer = bomb_timers[(tx, ty)]
                        if timer < other_timer:
                            bomb_timers[(tx, ty)] = timer
                            changed = True
                        break
                    if (tx, ty) in bricks:
                        break
                        
    return [(bx, by, timer) for (bx, by), timer in bomb_timers.items()]

# Xác định vùng nguy hiểm của bom (các ô nằm trong tia lửa nổ tương lai)
def get_bomb_hazard_zones(bombs: List[Tuple[int, int, int]], walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], blast_radius: int, width: int = 15, height: int = 13) -> Dict[Tuple[int, int], int]:
    hazard_zones = {}
    for bx, by, timer in bombs:
        if (bx, by) not in hazard_zones or timer < hazard_zones[(bx, by)]:
            hazard_zones[(bx, by)] = timer
            
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            for dist in range(1, blast_radius + 1):
                tx, ty = bx + dx * dist, by + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls:
                    break
                # Ghi nhận ô nguy hiểm kèm thời gian bom nổ đếm ngược (timer càng nhỏ càng nguy hiểm)
                if (tx, ty) not in hazard_zones or timer < hazard_zones[(tx, ty)]:
                    hazard_zones[(tx, ty)] = timer
                if (tx, ty) in bricks:
                    break
    return hazard_zones

# Thuật toán BFS tìm đường thoát hiểm khỏi vùng nguy hiểm của bom
def check_escape_path(start_pos: Tuple[int, int], walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], bombs: List[Tuple[int, int, int]], blast_radius: int, current_explosions: Set[Tuple[int, int]], width: int = 15, height: int = 13) -> bool:
    resolved_bombs = resolve_bomb_chain_reactions(bombs, walls, bricks, blast_radius, width, height)
    hazard_zones = get_bomb_hazard_zones(resolved_bombs, walls, bricks, blast_radius, width, height)
    
    # Nếu vị trí hiện tại không nằm trong vùng nguy hiểm, xem như an toàn
    if start_pos not in hazard_zones and start_pos not in current_explosions:
        return True
        
    queue = [(start_pos[0], start_pos[1], 0)]
    visited = {(start_pos[0], start_pos[1], 0)}
    bomb_positions = {(bx, by) for bx, by, _ in resolved_bombs}
    
    max_bfs_steps = 15  # Giới hạn tìm kiếm tránh tràn bộ nhớ
    while queue:
        cx, cy, t = queue.pop(0)
        
        if t > max_bfs_steps:
            continue
            
        # Tìm thấy ô an toàn nằm ngoài vùng bom và không có lửa nổ
        if (cx, cy) not in hazard_zones and (cx, cy) not in current_explosions:
            return True
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if (nx, ny) in walls or (nx, ny) in bricks:
                continue
            # Không được đi xuyên qua bom khác (trừ ô xuất phát ban đầu)
            if (nx, ny) in bomb_positions and (nx, ny) != start_pos:
                continue
            if (nx, ny) in current_explosions:
                continue
                
            # Nếu ô di chuyển tới sẽ bị nổ trước hoặc đúng thời điểm bước chân vào, bỏ qua
            if (nx, ny) in hazard_zones and hazard_zones[(nx, ny)] <= t + 1:
                continue
                
            if (nx, ny, t + 1) not in visited:
                visited.add((nx, ny, t + 1))
                queue.append((nx, ny, t + 1))
                
    return False

# Thuật toán BFS đa đích (Multi-target BFS): tìm khoảng cách ngắn nhất đồng thời tới:
# Vật phẩm gần nhất, Ô đặt bom gần gạch nhất, và Đối thủ gần nhất.
# Giúp tối ưu hóa hiệu suất (chỉ cần chạy BFS đúng 1 lần thay vì 3 lần).
def bfs_shortest_path_distance_multi(start: Tuple[int, int], item_targets: Set[Tuple[int, int]], brick_targets: Set[Tuple[int, int]], enemy_targets: Set[Tuple[int, int]], walls: Set[Tuple[int, int]], bricks: Set[Tuple[int, int]], bombs: List[Tuple[int, int, int]] = None, width: int = 15, height: int = 13) -> Tuple[float, float, float]:
    min_item_dist = float('inf')
    min_brick_dist = float('inf')
    min_enemy_dist = float('inf')
    
    # Kiểm tra nhanh tại ô xuất phát
    if start in item_targets:
        min_item_dist = 0.0
    if start in brick_targets:
        min_brick_dist = 0.0
    if start in enemy_targets:
        min_enemy_dist = 0.0
        
    if min_item_dist == 0.0 and min_brick_dist == 0.0 and min_enemy_dist == 0.0:
        return 0.0, 0.0, 0.0
        
    queue = [(start[0], start[1], 0)]
    visited = {start}
    bomb_positions = {(bx, by) for bx, by, _ in bombs} if bombs else set()
    
    while queue:
        cx, cy, dist = queue.pop(0)
        
        # Kết thúc sớm nếu đã tìm thấy cả 3 loại mục tiêu
        if min_item_dist != float('inf') and min_brick_dist != float('inf') and min_enemy_dist != float('inf'):
            break
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) in item_targets and min_item_dist == float('inf'):
                    min_item_dist = float(dist + 1)
                if (nx, ny) in brick_targets and min_brick_dist == float('inf'):
                    min_brick_dist = float(dist + 1)
                if (nx, ny) in enemy_targets and min_enemy_dist == float('inf'):
                    min_enemy_dist = float(dist + 1)
                    
                # Chỉ đi qua các ô trống (không tường, không gạch, không bom)
                if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))
                        
    return min_item_dist, min_brick_dist, min_enemy_dist

# Hàm lượng giá Heuristic (đánh giá mức độ tốt/xấu của một ô đứng trên thang điểm số)
def heuristic_evaluate(pos: Tuple[int, int], state_info: dict, placed_bomb: Tuple[int, int, int] = None) -> float:
    px, py = pos
    width, height = state_info["width"], state_info["height"]
    
    # 1. Tránh tuyệt đối ô đang nổ hoặc ô có đối thủ đứng trực tiếp
    if pos in state_info["explosions"]:
        return -100000.0
        
    for ex, ey in state_info["enemies"]:
        if px == ex and py == ey:
            return -100000.0
            
    # 2. Đánh giá tính an toàn: Phải có ít nhất 1 đường thoát hiểm
    bombs_to_check = list(state_info["bombs"])
    if placed_bomb:
        bombs_to_check.append(placed_bomb)
        
    if not check_escape_path(pos, state_info["walls"], state_info["bricks"], bombs_to_check, state_info["blast_radius"], state_info["explosions"], width, height):
        return -80000.0 # Phạt nặng nếu bị kẹt/không có đường thoát
        
    # 3. Phạt nếu đứng trong vùng ảnh hưởng nguy hiểm của bom (cho dù có đường thoát)
    resolved_bombs = resolve_bomb_chain_reactions(bombs_to_check, state_info["walls"], state_info["bricks"], state_info["blast_radius"], width, height)
    hazard_zones = get_bomb_hazard_zones(resolved_bombs, state_info["walls"], state_info["bricks"], state_info["blast_radius"], width, height)
    
    score = 0.0
    
    if pos in hazard_zones:
        timer = hazard_zones[pos]
        score -= (5.0 - timer) * 150.0 # Bom sắp nổ (timer nhỏ) phạt nặng hơn bom mới đặt (timer lớn)
        
    # 4. Xử lý cự ly với kẻ địch (Tấn công khi có bom, phòng thủ chạy trốn khi hết vũ khí)
    min_enemy_dist = float('inf')
    for ex, ey in state_info["enemies"]:
        dist = abs(px - ex) + abs(py - ey)
        if dist < min_enemy_dist:
            min_enemy_dist = dist
            
    if min_enemy_dist == 1:
        if state_info["ammo"] > 0:
            score += 2000.0  # Thưởng lớn khi áp sát đối phương khi có bom
        else:
            score -= 3000.0  # Trốn chạy gấp nếu ở cạnh đối thủ mà hết bom
    elif min_enemy_dist == 2:
        if state_info["ammo"] > 0:
            score += 1000.0
        else:
            score -= 300.0
    elif min_enemy_dist == 3:
        if state_info["ammo"] > 0:
            score += 500.0
        else:
            score -= 30.0
        
    # Tạo danh sách các ô mục tiêu phục vụ tìm đường BFS
    item_targets = set(state_info["items"].keys()) if state_info["items"] else set()
    
    # Ô đứng cạnh gạch để đặt bom phá
    brick_targets = set()
    if state_info["bricks"]:
        for bx, by in state_info["bricks"]:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tx, ty = bx + dx, by + dy
                if 0 <= tx < width and 0 <= ty < height and (tx, ty) not in state_info["walls"] and (tx, ty) not in state_info["bricks"]:
                    brick_targets.add((tx, ty))
                    
    # Ô đứng cạnh kẻ địch để đặt bom tiêu diệt
    enemy_targets = set()
    if state_info["enemies"]:
        for ex, ey in state_info["enemies"]:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tx, ty = ex + dx, ey + dy
                if 0 <= tx < width and 0 <= ty < height and (tx, ty) not in state_info["walls"] and (tx, ty) not in state_info["bricks"]:
                    enemy_targets.add((tx, ty))
                    
    # Chạy BFS đa đích tìm khoảng cách ngắn nhất
    dist_item, dist_brick, dist_enemy = bfs_shortest_path_distance_multi(
        pos, item_targets, brick_targets, enemy_targets,
        state_info["walls"], state_info["bricks"], bombs_to_check, width, height
    )
    
    # 5. Thưởng khuyến khích ăn vật phẩm tăng sức mạnh
    if dist_item != float('inf'):
        score += 1500.0 / (dist_item + 1)
        
    # 6. Thưởng khuyến khích di chuyển lại gần gạch để khai phá
    if dist_brick != float('inf'):
        score += 300.0 / (dist_brick + 1)
        
    # 7. Thưởng di chuyển săn lùng kẻ địch
    if dist_enemy != float('inf'):
        if not state_info["bricks"]:
            # Khi bản đồ hết gạch hoàn toàn -> Ưu tiên tuyệt đối việc săn lùng
            score += 800.0 / (dist_enemy + 1)
        else:
            if state_info["ammo"] > 0:
                score += 100.0 / (dist_enemy + 1)
            else:
                score -= 50.0 / (dist_enemy + 1)
                
    return score

# Giả lập trạng thái tiếp theo của game khi người chơi thực hiện 1 hành động
def simulate_state_forward(state_info: dict, player_action: str, step: int = 1) -> dict:
    next_state = {
        "player_pos": state_info["player_pos"],
        "walls": state_info["walls"],
        "bricks": state_info["bricks"],
        "enemies": list(state_info["enemies"]),
        "bombs": list(state_info["bombs"]),
        "explosions": set(state_info["explosions"]),
        "items": dict(state_info["items"]),
        "ammo": state_info["ammo"],
        "blast_radius": state_info["blast_radius"],
        "width": state_info["width"],
        "height": state_info["height"]
    }
    
    px, py = next_state["player_pos"]
    
    # 1. Giả lập dịch chuyển người chơi
    if player_action == "UP":
        ny = py - 1
        if (px, ny) not in next_state["walls"] and (px, ny) not in next_state["bricks"] and (px, ny) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["player_pos"] = (px, ny)
    elif player_action == "DOWN":
        ny = py + 1
        if (px, ny) not in next_state["walls"] and (px, ny) not in next_state["bricks"] and (px, ny) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["player_pos"] = (px, ny)
    elif player_action == "LEFT":
        nx = px - 1
        if (nx, py) not in next_state["walls"] and (nx, py) not in next_state["bricks"] and (nx, py) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["player_pos"] = (nx, py)
    elif player_action == "RIGHT":
        nx = px + 1
        if (nx, py) not in next_state["walls"] and (nx, py) not in next_state["bricks"] and (nx, py) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["player_pos"] = (nx, py)
    elif player_action == "BOMB":
        # Giả lập đặt bom tại tọa độ hiện tại của Agent
        if next_state["ammo"] > 0 and (px, py) not in {(b[0], b[1]) for b in next_state["bombs"]}:
            next_state["bombs"].append((px, py, 4))
            next_state["ammo"] -= 1
            
    # 2. Giả lập cập nhật bộ đếm thời gian của bom
    new_bombs = []
    exploded_bombs = []
    for bx, by, timer in next_state["bombs"]:
        if timer <= 1:
            exploded_bombs.append((bx, by))
        else:
            new_bombs.append((bx, by, timer - 1))
            
    next_state["bombs"] = new_bombs
    
    # Giải quyết các quả bom nổ ngay trong bước giả lập này
    if exploded_bombs:
        resolved_exploded = resolve_bomb_chain_reactions(
            [(bx, by, 0) for bx, by in exploded_bombs],
            next_state["walls"],
            next_state["bricks"],
            next_state["blast_radius"],
            next_state["width"],
            next_state["height"]
        )
        hazard = get_bomb_hazard_zones(resolved_exploded, next_state["walls"], next_state["bricks"], next_state["blast_radius"], next_state["width"], next_state["height"])
        next_state["explosions"] = set(hazard.keys())
        next_state["bricks"] = next_state["bricks"] - next_state["explosions"]  # Phá hủy gạch bằng tia lửa nổ
    else:
        if step == 1:
            next_state["explosions"] = set(state_info["explosions"])
        else:
            next_state["explosions"] = set()
        
    return next_state

# Lớp chính định nghĩa MinimaxAgent
class MinimaxAgent(BaseAgent):
    """An agent that uses Minimax search with heuristic lookahead to choose actions."""

    def __init__(self, depth: int = 2):
        self.depth = depth

    # Hàm đưa ra lựa chọn hành động tối ưu cho bước đi hiện tại của Agent
    def choose_action(self, state: dict) -> str:
        # Chuyển đổi trạng thái thô
        state_info = parse_state(state)
        
        legal_actions = state.get("legal_actions")
        if not legal_actions:
            legal_actions = ["UP", "DOWN", "LEFT", "RIGHT", "BOMB", "WAIT"]
            
        best_action = "WAIT"
        best_score = -float('inf')
        
        fallback_action = "WAIT"
        fallback_score = -float('inf')
        
        # Duyệt qua các hành động hợp lệ ở Bước 1
        for action1 in legal_actions:
            px, py = state_info["player_pos"]
            
            # Cắt tỉa (Pruning) các hành động bất khả thi để tiết kiệm tài nguyên
            if action1 == "UP" and (px, py - 1) in state_info["walls"] | state_info["bricks"]:
                continue
            if action1 == "DOWN" and (px, py + 1) in state_info["walls"] | state_info["bricks"]:
                continue
            if action1 == "LEFT" and (px - 1, py) in state_info["walls"] | state_info["bricks"]:
                continue
            if action1 == "RIGHT" and (px + 1, py) in state_info["walls"] | state_info["bricks"]:
                continue
            if action1 == "BOMB":
                if state_info["ammo"] <= 0:
                    continue
                if (px, py) in {(b[0], b[1]) for b in state_info["bombs"]}:
                    continue
                    
            # Giả lập trạng thái game sau khi đi hành động ở bước 1
            state_info_1 = simulate_state_forward(state_info, action1, step=1)
            score_1 = heuristic_evaluate(state_info_1["player_pos"], state_info_1)
            
            # Lưu lại hành động dự phòng an toàn nhất đề phòng tất cả các nhánh sau đều dẫn tới cái chết
            if score_1 > fallback_score:
                fallback_score = score_1
                fallback_action = action1
                
            # Nếu nước đi ở bước 1 đã dẫn tới cái chết (-50,000 điểm), cắt tỉa không duyệt tiếp nhánh này
            if score_1 <= -50000.0:
                continue
                
            # Duyệt tiếp Bước 2 (Lookahead Depth 2)
            max_score_2 = -float('inf')
            
            for action2 in ["UP", "DOWN", "LEFT", "RIGHT", "BOMB", "WAIT"]:
                px1, py1 = state_info_1["player_pos"]
                
                # Cắt tỉa nhánh giả lập bước 2
                if action2 == "UP" and (px1, py1 - 1) in state_info_1["walls"] | state_info_1["bricks"]:
                    continue
                if action2 == "DOWN" and (px1, py1 + 1) in state_info_1["walls"] | state_info_1["bricks"]:
                    continue
                if action2 == "LEFT" and (px1 - 1, py1) in state_info_1["walls"] | state_info_1["bricks"]:
                    continue
                if action2 == "RIGHT" and (px1 + 1, py1) in state_info_1["walls"] | state_info_1["bricks"]:
                    continue
                if action2 == "BOMB":
                    if state_info_1["ammo"] <= 0:
                        continue
                    if (px1, py1) in {(b[0], b[1]) for b in state_info_1["bombs"]}:
                        continue
                        
                # Giả lập trạng thái game sau hành động bước 2
                state_info_2 = simulate_state_forward(state_info_1, action2, step=2)
                score = heuristic_evaluate(state_info_2["player_pos"], state_info_2)
                
                # Điểm thưởng nếu đặt bom hiệu quả ở bước 1 (cạnh gạch hoặc cạnh địch)
                if action1 == "BOMB":
                    is_next_to_brick = any((px + dx, py + dy) in state_info["bricks"] for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)])
                    is_next_to_enemy = any(abs(px - ex) + abs(py - ey) <= 2 for ex, ey in state_info["enemies"])
                    if is_next_to_brick or is_next_to_enemy:
                        score += 3500.0 # Thưởng lớn khuyến khích đặt bom tấn công
                    else:
                        score -= 800.0  # Phạt nếu đặt bom vô nghĩa
                        
                if score > max_score_2:
                    max_score_2 = score
                    
            if max_score_2 == -float('inf'):
                max_score_2 = score_1
                
            # Cập nhật hành động tốt nhất dựa trên điểm số cực đại bước 2
            if max_score_2 > best_score:
                best_score = max_score_2
                best_action = action1
                
        # Nếu tất cả các nước đi tính toán ở bước 2 đều chết (-50,000), trả về nước đi dự phòng an toàn nhất
        if best_score <= -50000.0:
            return fallback_action
            
        return best_action