"""
Các công cụ tìm kiếm dùng chung cho các agent Bomberman.

File này chứa bộ phân tích trạng thái (parser), bộ mô phỏng (simulator), và bộ đánh giá (evaluator)
được sử dụng bởi tất cả các agent tìm kiếm trong không gian trạng thái (State-space Search)
như: Hill Climbing, Simulated Annealing, BFS, DFS, Greedy, A*.
"""
import gc
import random
from typing import Tuple, Dict, Set, List

def is_env_object(obj) -> bool:
    """Kiểm tra xem đối tượng có phải là thực thể của lớp Environment hay không."""
    try:
        return obj.__class__.__name__ == 'Environment'
    except Exception:
        return False

def parse_state(state: dict) -> dict:
    """
    Phân tích và chuẩn hóa trạng thái game từ môi trường (raw state dict) thành định dạng chuẩn.
    Trả về dict chứa: player_pos, walls, bricks, enemies, bombs, explosions, items, ammo, blast_radius, width, height.
    """
    player_pos = state.get("player_pos") or state.get("self_position")
    width, height = 15, 13
    board = state.get("board") or state.get("grid")
    if board is not None:
        height = len(board)
        width = len(board[0]) if height > 0 else 0
    walls = set()
    bricks = set()
    if board is not None:
        for y in range(height):
            for x in range(width):
                val = board[y][x]
                if val == 1:
                    walls.add((x, y)) # 1 đại diện cho Tường (Walls)
                elif val == 2:
                    bricks.add((x, y)) # 2 đại diện cho Gạch (Bricks)
                if player_pos is None and val == 5:
                    player_pos = (x, y) # 5 đại diện cho Player nếu không có trường riêng
    else:
        try:
            # Lấy thông tin bản đồ trực tiếp từ bộ nhớ Garbage Collector nếu có đối tượng Environment
            env = None
            for obj in gc.get_objects():
                if is_env_object(obj):
                    env = obj
                    break
            if env is not None and env.map is not None:
                walls = set(env.map.walls)
                bricks = set(env.map.bricks)
                width = env.map.width
                height = env.map.height
            else:
                walls = set(map(tuple, state.get("walls", [])))
                bricks = set(map(tuple, state.get("bricks", [])))
                width = state.get("width", 15)
                height = state.get("height", 13)
        except Exception:
            walls = set(map(tuple, state.get("walls", [])))
            bricks = set(map(tuple, state.get("bricks", [])))
            width = state.get("width", 15)
            height = state.get("height", 13)
    if player_pos is None:
        player_pos = (1, 1)
    
    # Phân tích danh sách kẻ địch
    enemies = []
    raw = state.get("enemies") or state.get("enemy_positions")
    if raw:
        for e in raw:
            if isinstance(e, dict):
                enemies.append((e.get('x'), e.get('y')))
            elif isinstance(e, (list, tuple)):
                enemies.append((e[0], e[1]))
            else:
                enemies.append((e.x, e.y))
                
    # Phân tích danh sách bom hiện tại
    bombs = []
    raw = state.get("bombs") or state.get("bomb_positions")
    if raw:
        for b in raw:
            if isinstance(b, dict):
                bombs.append((b.get('x'), b.get('y'), b.get('timer', 4)))
            elif isinstance(b, (list, tuple)):
                bombs.append((b[0], b[1], b[2] if len(b) >= 3 else 4))
            else:
                bombs.append((b.x, b.y, b.timer))
                
    # Phân tích vùng đang bùng nổ
    explosions = set()
    for exp in state.get("explosions", []):
        if isinstance(exp, (list, tuple)):
            explosions.add((exp[0], exp[1]))
        elif isinstance(exp, dict):
            explosions.add((exp.get('x'), exp.get('y')))
            
    # Phân tích các vật phẩm nâng cấp
    items = {}
    raw = state.get("items", {})
    if isinstance(raw, dict):
        for k, v in raw.items():
            if isinstance(k, (list, tuple)):
                items[tuple(k)] = v
                
    return {
        "player_pos": player_pos,
        "walls": walls,
        "bricks": bricks,
        "enemies": enemies,
        "bombs": bombs,
        "explosions": explosions,
        "items": items,
        "ammo": state.get("ammo", 1),
        "blast_radius": state.get("blast_radius", 2),
        "width": width,
        "height": height
    }

def get_hazard_zones(bombs, walls, bricks, blast_radius, width, height) -> Dict:
    """
    Xác định các vùng nguy hiểm (hazard zones) bị ảnh hưởng bởi bom.
    Trả về dict ánh xạ mỗi tọa độ bị đe dọa tới thời gian còn lại trước khi bom nổ (timer nhỏ nhất).
    """
    hazard = {}
    for bx, by, timer in bombs:
        # Bản thân ô đặt bom là vùng nguy hiểm
        if (bx, by) not in hazard or timer < hazard[(bx, by)]:
            hazard[(bx, by)] = timer
            
        # Lan truyền tia lửa theo 4 hướng (lên, xuống, trái, phải)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for dist in range(1, blast_radius + 1):
                tx, ty = bx + dx * dist, by + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls: # Tường cứng cản tia lửa nổ
                    break
                if (tx, ty) not in hazard or timer < hazard[(tx, ty)]:
                    hazard[(tx, ty)] = timer
                if (tx, ty) in bricks: # Gạch cản tia lửa nổ (nhưng bản thân gạch vẫn bị phá hủy)
                    break
    return hazard

def simulate_state(info: dict, action: str) -> dict:
    """
    Mô phỏng trạng thái tiếp theo của game sau khi người chơi thực hiện một hành động (action).
    Hỗ trợ mô phỏng di chuyển, đặt bom, đếm ngược bom nổ, kích nổ dây chuyền, kẻ địch bị tiêu diệt, gạch bị phá hủy.
    """
    px, py = info["player_pos"]
    walls = info["walls"]
    bricks = set(info["bricks"])
    enemies = list(info["enemies"])
    items = dict(info["items"])
    bombs = list(info["bombs"])
    explosions = set(info["explosions"])
    ammo = info["ammo"]
    blast_radius = info["blast_radius"]
    width = info["width"]
    height = info["height"]

    sim_player_pos = (px, py)
    sim_bombs = list(bombs)
    sim_ammo = ammo
    sim_bricks = set(bricks)
    sim_enemies = list(enemies)
    sim_items = dict(items)
    sim_explosions = set(explosions)

    # 1. Mô phỏng hành động của Player
    if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
        dx, dy = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}[action]
        sim_player_pos = (px + dx, py + dy)
        if sim_player_pos in sim_items:
            del sim_items[sim_player_pos] # Ăn vật phẩm
    elif action == "BOMB":
        sim_bombs.append((px, py, 4)) # Đặt bom mới với thời gian chờ nổ là 4 tick
        sim_ammo = ammo - 1

    # 2. Cập nhật đếm ngược thời gian của bom và xử lý kích nổ
    next_bombs = []
    bombed_this_turn = []
    for bx, by, timer in sim_bombs:
        if timer <= 1:
            bombed_this_turn.append((bx, by, blast_radius))
        else:
            next_bombs.append((bx, by, timer - 1)) # Giảm timer đi 1 tick

    sim_bombs = next_bombs

    # Chuẩn bị cấu trúc dữ liệu bom để xử lý nổ dây chuyền (chain reaction)
    bombs_dict = {(b[0], b[1]): b for b in sim_bombs}
    for bx, by, br in bombed_this_turn:
        bombs_dict[(bx, by)] = (bx, by, 0)

    # Vòng lặp xử lý vụ nổ và lan truyền kích nổ dây chuyền
    while bombed_this_turn:
        bx, by, br = bombed_this_turn.pop(0)
        sim_explosions.add((bx, by))
        # Tiêu diệt kẻ địch đứng ngay tại tâm vụ nổ
        sim_enemies = [e for e in sim_enemies if not (e[0] == bx and e[1] == by)]

        # Lan truyền tia lửa nổ theo 4 hướng
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for dist in range(1, br + 1):
                tx, ty = bx + dx * dist, py + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls:
                    break

                sim_explosions.add((tx, ty))

                # Phá hủy gạch
                if (tx, ty) in sim_bricks:
                    sim_bricks.discard((tx, ty))
                    if (tx, ty) in sim_items:
                        del sim_items[(tx, ty)] # Phá hủy vật phẩm ẩn trong gạch
                    break # Tia lửa dừng lại khi trúng gạch

                # Tiêu diệt kẻ địch trong tầm nổ
                sim_enemies = [e for e in sim_enemies if not (e[0] == tx and e[1] == ty)]

                # Kích nổ dây chuyền nếu gặp quả bom khác
                if (tx, ty) in bombs_dict:
                    match_bombs = [b for b in sim_bombs if b[0] == tx and b[1] == ty]
                    if match_bombs:
                        sim_bombs = [b for b in sim_bombs if not (b[0] == tx and b[1] == ty)]
                        bombed_this_turn.append((tx, ty, br))

    sim_hazard_zones = get_hazard_zones(sim_bombs, walls, sim_bricks, blast_radius, width, height)

    # 3. Tính toán các dự báo hiệu quả khi hành động là "BOMB" (để làm phần thưởng heuristic)
    projected_destroyed_bricks = set(info.get("projected_destroyed_bricks", []))
    projected_hit_enemies = set(info.get("projected_hit_enemies", []))
    bomb_efficiency_reward = info.get("bomb_efficiency_reward", 0.0)

    if action == "BOMB":
        other_bomb_positions = {(bx, by) for bx, by, _ in bombs}
        chained_bombs_count = 0
        new_projected_destroyed_bricks = set()
        new_projected_hit_enemies = set()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for dist in range(1, blast_radius + 1):
                tx, ty = px + dx * dist, py + dy * dist
                if not (0 <= tx < width and 0 <= ty < height):
                    break
                if (tx, ty) in walls:
                    break
                if (tx, ty) in sim_bricks:
                    new_projected_destroyed_bricks.add((tx, ty))
                    break
                if (tx, ty) in other_bomb_positions:
                    chained_bombs_count += 1
                for ex, ey in sim_enemies:
                    if ex == tx and ey == ty:
                        new_projected_hit_enemies.add((ex, ey))

        projected_destroyed_bricks.update(new_projected_destroyed_bricks)
        projected_hit_enemies.update(new_projected_hit_enemies)
        # Cộng điểm thưởng dựa trên hiệu quả ước tính của quả bom vừa đặt
        bomb_efficiency_reward += (
            len(new_projected_destroyed_bricks) * 200.0 + # Phá gạch: +200 điểm
            len(new_projected_hit_enemies) * 400.0 +       # Trúng địch: +400 điểm
            chained_bombs_count * 150.0                    # Nổ dây chuyền: +150 điểm
        )

    return {
        "player_pos": sim_player_pos,
        "walls": walls,
        "bricks": sim_bricks,
        "enemies": sim_enemies,
        "bombs": sim_bombs,
        "explosions": sim_explosions,
        "items": sim_items,
        "ammo": sim_ammo,
        "blast_radius": blast_radius,
        "width": width,
        "height": height,
        "hazard_zones": sim_hazard_zones,
        "projected_destroyed_bricks": projected_destroyed_bricks,
        "projected_hit_enemies": projected_hit_enemies,
        "bomb_efficiency_reward": bomb_efficiency_reward
    }

def evaluate_state(sim_state: dict) -> float:
    """
    Hàm heuristic đánh giá độ tốt của một trạng thái mô phỏng (càng cao càng tốt).
    Được dùng để định hướng cho các thuật toán tìm kiếm cục bộ hoặc tìm kiếm cây quyết định.
    
    Cơ chế chấm điểm:
      1. Sống sót & An toàn: Né tránh vụ nổ (-1M điểm nếu chết, phạt nặng nếu đứng trong vùng bom sắp nổ).
      2. Khả năng di chuyển tự do: Thưởng điểm nếu có nhiều ô láng giềng an toàn và nhiều lối thoát hiểm.
      3. Phạt ngõ cụt: Trừ điểm nặng (-400k) nếu không có đường đi tiếp.
      4. Vật phẩm: Thưởng điểm khi lại gần vật phẩm và khi ăn vật phẩm.
      5. Kẻ địch: Phạt khi có kẻ địch gần nếu không có bom, hoặc thưởng khi dồn kẻ địch vào tầm bom.
      6. Gạch: Thưởng khi phá hủy gạch và đứng gần gạch cần phá.
      7. Phần thưởng hiệu quả bom: Điểm thưởng từ số lượng gạch/địch dự kiến tiêu diệt.
      8. Ưu tiên tâm bản đồ: Khuyến khích di chuyển ở khu vực giữa bản đồ để tăng độ linh hoạt.
    """
    pos = sim_state["player_pos"]
    hazard_zones = sim_state["hazard_zones"]
    explosions = sim_state["explosions"]
    walls = sim_state["walls"]
    bricks = sim_state["bricks"]
    bombs = sim_state["bombs"]
    bomb_positions = {(bx, by) for bx, by, _ in bombs}
    width = sim_state["width"]
    height = sim_state["height"]
    enemies = sim_state["enemies"]
    items = sim_state["items"]
    ammo = sim_state["ammo"]
    blast_radius = sim_state["blast_radius"]

    projected_destroyed_bricks = sim_state.get("projected_destroyed_bricks", set())
    projected_hit_enemies = sim_state.get("projected_hit_enemies", set())
    bomb_efficiency_reward = sim_state.get("bomb_efficiency_reward", 0.0)

    score = 0.0

    # 1. Survival & Safety Heuristic (Đánh giá mức độ an toàn và sống sót)
    if pos in explosions:
        return -1000000.0 # Chết chắc chắn trong vụ nổ

    in_hazard = pos in hazard_zones
    if in_hazard:
        timer = hazard_zones[pos]
        if timer <= 1:
            return -500000.0 # Cực kỳ nguy hiểm, bom sắp nổ ở tick sau
        score -= (5 - timer) * 150.0 # Phạt dựa trên thời gian bom nổ đến gần

    bomb_timers = {(bx, by): t for bx, by, t in bombs}
    if pos in bomb_positions:
        b_timer = bomb_timers.get(pos, 4)
        score -= (5 - b_timer) * 300.0 # Phạt khi đứng đè lên quả bom của chính mình sắp nổ

    # Kiểm tra số lượng ô láng giềng thực sự an toàn (không có bom/nổ/nguy cơ)
    safe_neighbors = 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions and (nx, ny) not in explosions:
                if (nx, ny) not in hazard_zones:
                    safe_neighbors += 1
    score += safe_neighbors * 200.0

    # 2. Escape Freedom (Độ tự do di chuyển)
    reachable_neighbors = 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions and (nx, ny) not in explosions:
                reachable_neighbors += 1
    score += reachable_neighbors * 50.0

    # Tính toán số lối thoát hiểm khả thi từ các ô láng giềng
    escape_routes = 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls and (nx, ny) not in bricks and (nx, ny) not in bomb_positions and (nx, ny) not in explosions:
                for ddx, ddy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nnx, nny = nx + ddx, ny + ddy
                    if (nnx, nny) == pos:
                        continue
                    if 0 <= nnx < width and 0 <= nny < height:
                        if (nnx, nny) not in walls and (nnx, nny) not in bricks and (nnx, nny) not in bomb_positions and (nnx, nny) not in explosions:
                            if (nnx, nny) not in hazard_zones:
                                escape_routes += 1
    score += escape_routes * 150.0

    # 3. Dead-end Penalty (Phạt ngõ cụt)
    if reachable_neighbors == 0:
        score -= 400000.0 # Bị kẹt hoàn toàn

    # 4. Item Proximity (Khoảng cách tới vật phẩm)
    score -= len(items) * 1000.0 # Ưu tiên ăn càng nhiều vật phẩm càng tốt (làm giảm số lượng item còn lại)
    if items:
        min_dist_item = min(abs(pos[0] - ix) + abs(pos[1] - iy) for ix, iy in items.keys())
        score += 600.0 / (min_dist_item + 1) # Thưởng điểm khi lại gần vật phẩm nhất

    # 5. Enemy Proximity (Tương tác với kẻ địch)
    effective_enemies_count = len(enemies) - len(projected_hit_enemies)
    score -= effective_enemies_count * 3000.0 # Thưởng lớn khi tiêu diệt được kẻ địch
    if enemies:
        min_dist_enemy = min(abs(pos[0] - ex) + abs(pos[1] - ey) for ex, ey in enemies)
        if ammo > 0:
            score += 300.0 / (min_dist_enemy + 1) # Nếu có bom, khuyến khích áp sát kẻ địch để đặt bom tiêu diệt
            if min_dist_enemy <= 1:
                score += 100.0
        else:
            score -= 200.0 / (min_dist_enemy + 1) # Nếu không còn bom, tránh xa kẻ địch để tự vệ

    # 6. Brick Proximity (Tương tác với gạch)
    effective_bricks = set(bricks) - projected_destroyed_bricks
    score -= len(effective_bricks) * 500.0 # Thưởng khi phá gạch thành công
    if bricks:
        min_dist_brick = min(abs(pos[0] - bx) + abs(pos[1] - by) for bx, by in bricks)
        score += 100.0 / (min_dist_brick + 1) # Khuyến khích di chuyển lại gần gạch để dọn đường
        if min_dist_brick == 1:
            score += 50.0

    # 7. Bomb Placement & Efficiency Reward (Thưởng hiệu quả đặt bom)
    score += bomb_efficiency_reward

    # 8. Center of Map Preference (Khuyến khích ở trung tâm bản đồ)
    cx, cy = width / 2.0, height / 2.0
    dist_to_center = abs(pos[0] - cx) + abs(pos[1] - cy)
    score += 10.0 / (dist_to_center + 1)

    return score
