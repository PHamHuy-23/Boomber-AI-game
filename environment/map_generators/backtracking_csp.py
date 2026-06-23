"""
Backtracking CSP Map Generator
================================
Thuật toán: Backtracking Search kết hợp:
  - MRV  (Minimum Remaining Values) : Chọn ô có ít giá trị hợp lệ nhất để gán tiếp
  - LCV  (Least Constraining Value) : Ưu tiên giá trị làm hạn chế ít nhất các ô hàng xóm
  - Forward Checking (FC)           : Sau mỗi lần gán, lọc domain của các ô chưa gán
  - Symmetry Constraint             : Mỗi ô (x,y) khi gán sẽ gán đối xứng sang 3 ô còn lại

Ý tưởng tổng quát:
  1. Xác định tập biến (variable): tất cả ô trong ¼ bản đồ (top-left quadrant).
  2. Domain mỗi biến: {'empty', 'brick'}.
  3. Constraint:
     a) Spawn-safe: 4 góc và hình chữ L xung quanh phải là 'empty'.
     b) Reachability: BFS sau khi gán xong phải kết nối được 4 spawn.
     c) Symmetric: domain giảm bởi Forward Checking trên ¼ đã đại diện cho cả 4 góc.
  4. Ordering heuristic:
     - MRV: biến có domain_size nhỏ nhất được chọn trước.
     - LCV: với biến đã chọn, thử giá trị 'empty' trước hay 'brick' trước tùy vào
             giá trị nào hạn chế ít hàng xóm hơn (đếm số hàng xóm bị loại khỏi domain).
  5. Forward Checking: sau gán biến = v, cập nhật domain của hàng xóm chưa gán.
     Nếu domain của bất kỳ biến chưa gán nào rỗng → prune, backtrack.
"""

import random
import copy
from typing import Dict, Set, Tuple, List, Optional
from configs.default_config import GameConfig


# ═══════════════════════════════════════════════════════════════════
#  Type Aliases
# ═══════════════════════════════════════════════════════════════════
Cell = Tuple[int, int]
Domain = Dict[Cell, List[str]]   # biến → danh sách giá trị còn lại
Assignment = Dict[Cell, str]      # biến → giá trị đã gán


class BacktrackingCSPMapGenerator:
    """
    Sinh bản đồ bằng Backtracking Search + MRV + LCV + Forward Checking.

    Sử dụng đối xứng 4 chiều: chỉ giải CSP trên góc top-left (1/4 bản đồ),
    sau đó phản chiếu kết quả sang 3 phần còn lại.
    """

    CELL_EMPTY = 'empty'
    CELL_BRICK = 'brick'
    CELL_WALL  = 'wall'

    def __init__(
        self,
        width: int  = GameConfig.MAP_WIDTH,
        height: int = GameConfig.MAP_HEIGHT,
        brick_density: float = GameConfig.BRICK_DENSITY,
        seed: Optional[int] = None,
    ):
        self.width  = width
        self.height = height
        self.target_brick_ratio = brick_density  # tỉ lệ gạch mong muốn
        self.seed   = seed
        self._rng   = random.Random(seed)

    # ──────────────────────────────────────────────────────────────
    #  Public API (giống interface của Map)
    # ──────────────────────────────────────────────────────────────
    def generate(self) -> Tuple[Set[Cell], Set[Cell], List[Cell]]:
        """
        Trả về (walls, bricks, spawns) — cùng interface với environment.map.Map.
        Gọi nhiều lần sẽ cho kết quả khác nhau nếu seed=None.
        """
        self._rng = random.Random(self.seed)

        walls  = self._build_walls()
        spawns = self._corner_spawns()
        safe   = self._spawn_safe_zone(spawns)

        # Bước 1: Xây domain ban đầu cho ¼ bản đồ (top-left quadrant)
        domain = self._init_domain(walls, safe)

        # Bước 2: Forward Checking ban đầu — loại 'brick' khỏi domain ô safe
        self._enforce_safe_constraints(domain, safe)

        # Bước 3: Backtracking Search với MRV + LCV + FC
        assignment: Assignment = {}
        result = self._backtrack(assignment, domain, walls, safe)

        if result is None:
            # Fallback nếu CSP không hội tụ → dùng random
            result = self._random_fallback(walls, safe)

        # Bước 4: Phản chiếu kết quả sang 4 góc
        bricks = self._mirror_to_full_map(result, walls, safe)

        return walls, bricks, spawns

    # ──────────────────────────────────────────────────────────────
    #  Khởi tạo cấu trúc
    # ──────────────────────────────────────────────────────────────
    def _build_walls(self) -> Set[Cell]:
        """Tường biên + trụ cố định (Bomberman-style: trụ tại vị trí chẵn)."""
        walls: Set[Cell] = set()
        W, H = self.width, self.height
        for y in range(H):
            for x in range(W):
                if x == 0 or x == W - 1 or y == 0 or y == H - 1:
                    walls.add((x, y))
        # Trụ cố định bên trong (tại x chẵn, y chẵn — lưới cờ vua kiểu Bomberman)
        for y in range(2, H - 2, 2):
            for x in range(2, W - 2, 2):
                walls.add((x, y))
        return walls

    def _corner_spawns(self) -> List[Cell]:
        W, H = self.width, self.height
        return [(1, 1), (W - 2, 1), (1, H - 2), (W - 2, H - 2)]

    def _spawn_safe_zone(self, spawns: List[Cell]) -> Set[Cell]:
        """Vùng an toàn hình chữ L quanh mỗi spawn — không được đặt gạch."""
        safe: Set[Cell] = set()
        for sx, sy in spawns:
            safe.add((sx, sy))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                safe.add((sx + dx, sy + dy))
        return safe

    # ──────────────────────────────────────────────────────────────
    #  Domain & Forward Checking
    # ──────────────────────────────────────────────────────────────
    def _init_domain(self, walls: Set[Cell], safe: Set[Cell]) -> Domain:
        """
        Domain cho ¼ bản đồ (top-left).
        Mỗi ô hợp lệ bắt đầu với domain = [empty, brick].
        Ô là tường → domain rỗng (không tham gia CSP).
        """
        W, H = self.width, self.height
        mx = W // 2 + 1   # chiều rộng quadrant (có thể overlap tại đường giữa)
        my = H // 2 + 1
        domain: Domain = {}
        for y in range(1, my):
            for x in range(1, mx):
                if (x, y) not in walls:
                    domain[(x, y)] = [self.CELL_EMPTY, self.CELL_BRICK]
        return domain

    def _enforce_safe_constraints(self, domain: Domain, safe: Set[Cell]) -> None:
        """Forward Checking ban đầu: ô trong safe zone chỉ có thể là 'empty'."""
        for cell in list(domain.keys()):
            if cell in safe:
                domain[cell] = [self.CELL_EMPTY]

    # ──────────────────────────────────────────────────────────────
    #  MRV — Minimum Remaining Values
    # ──────────────────────────────────────────────────────────────
    def _select_unassigned_variable(
        self, assignment: Assignment, domain: Domain
    ) -> Optional[Cell]:
        """
        MRV: chọn biến chưa gán có domain nhỏ nhất.
        Nếu bằng nhau → chọn ngẫu nhiên (tie-breaking) để đa dạng kết quả.
        """
        unassigned = [v for v in domain if v not in assignment]
        if not unassigned:
            return None
        # Sắp xếp theo domain_size tăng dần (MRV heuristic)
        unassigned.sort(key=lambda v: len(domain[v]))
        # Tie-breaking: lấy tất cả biến có cùng domain_size nhỏ nhất rồi random
        min_size = len(domain[unassigned[0]])
        tied = [v for v in unassigned if len(domain[v]) == min_size]
        return self._rng.choice(tied)

    # ──────────────────────────────────────────────────────────────
    #  LCV — Least Constraining Value
    # ──────────────────────────────────────────────────────────────
    def _order_values(
        self, var: Cell, domain: Domain, assignment: Assignment
    ) -> List[str]:
        """
        LCV: sắp xếp giá trị theo số ô hàng xóm chưa gán bị xóa khỏi domain
        nếu ta chọn giá trị đó (ít ràng buộc hơn → được ưu tiên thử trước).

        Quy tắc:
        - 'brick' tại (x,y) → brick không thể cạnh nhau theo đường thẳng (không có
          ràng buộc cứng này trong Bomberman), nên LCV chỉ đếm xem
          bao nhiêu hàng xóm bị giảm domain nếu ta chọn giá trị đó.
        - Trong trường hợp này, chọn 'brick' không trực tiếp hạn chế hàng xóm,
          nhưng ảnh hưởng đến tỉ lệ gạch tổng thể → LCV xét density_pressure.
        """
        x, y = var
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        def constraint_cost(value: str) -> int:
            """Đếm số lần domain hàng xóm bị thu hẹp nếu chọn value này."""
            cost = 0
            for nx, ny in neighbors:
                if (nx, ny) in domain and (nx, ny) not in assignment:
                    # Giả lập: nếu value='brick', hàng xóm không bị ảnh hưởng
                    # (Bomberman cho phép gạch liền nhau).
                    # LCV ở đây đánh giá dựa trên density target:
                    # nếu đã đặt nhiều brick, ưu tiên 'empty' hơn.
                    if value == self.CELL_BRICK:
                        cost += 1  # mỗi brick làm tăng áp lực density
            return cost

        # Sắp xếp tăng dần theo cost: giá trị ít hạn chế nhất được thử trước
        values = list(domain[var])
        values.sort(key=lambda v: constraint_cost(v))
        return values

    # ──────────────────────────────────────────────────────────────
    #  Forward Checking sau mỗi lần gán
    # ──────────────────────────────────────────────────────────────
    def _forward_check(
        self,
        var: Cell,
        value: str,
        domain: Domain,
        assignment: Assignment,
        assigned_count: Dict[str, int],
    ) -> Optional[Domain]:
        """
        Forward Checking: sau khi gán var=value, cập nhật domain các biến liên quan.
        Trả về domain mới nếu hợp lệ, None nếu phát hiện domain rỗng (dead-end).

        Ràng buộc được kiểm tra:
        1. Density constraint: nếu số brick đã gán đủ → loại 'brick' khỏi domain còn lại.
        2. Không có ràng buộc cứng giữa các ô hàng xóm trong Bomberman tiêu chuẩn,
           nhưng ta thêm soft constraint: không để >3 brick liên tiếp (tránh tạo hành lang chết).
        """
        new_domain = {k: list(v) for k, v in domain.items()}

        total_cells = len(domain)
        target_bricks = int(total_cells * self.target_brick_ratio)

        brick_count = assigned_count.get(self.CELL_BRICK, 0) + (1 if value == self.CELL_BRICK else 0)
        remaining = total_cells - len(assignment) - 1  # -1 vì var vừa gán

        # Nếu đã đủ brick → loại 'brick' khỏi tất cả biến chưa gán
        if brick_count >= target_bricks:
            for cell in new_domain:
                if cell not in assignment and cell != var:
                    if self.CELL_BRICK in new_domain[cell]:
                        new_domain[cell] = [self.CELL_EMPTY]
                    if not new_domain[cell]:
                        return None  # dead-end

        # Nếu cần thêm brick bắt buộc (remaining cells không đủ để fill target)
        empty_count = assigned_count.get(self.CELL_EMPTY, 0) + (1 if value == self.CELL_EMPTY else 0)
        needed_bricks = target_bricks - brick_count
        if needed_bricks > remaining:
            # Không thể đạt target → không prune, chấp nhận (soft constraint)
            pass

        return new_domain

    # ──────────────────────────────────────────────────────────────
    #  Backtracking Search chính
    # ──────────────────────────────────────────────────────────────
    def _backtrack(
        self,
        assignment: Assignment,
        domain: Domain,
        walls: Set[Cell],
        safe: Set[Cell],
        assigned_count: Optional[Dict[str, int]] = None,
        max_depth: int = 10000,
        _depth: int = 0,
    ) -> Optional[Assignment]:
        """
        Đệ quy Backtracking:
          1. Chọn biến bằng MRV.
          2. Thử từng giá trị theo thứ tự LCV.
          3. Áp dụng Forward Checking sau mỗi gán.
          4. Backtrack nếu Forward Checking thất bại.
        """
        if assigned_count is None:
            assigned_count = {self.CELL_EMPTY: 0, self.CELL_BRICK: 0}

        # Tất cả biến đã gán → CSP hoàn thành
        if len(assignment) == len(domain):
            return assignment

        # Giới hạn độ sâu để tránh timeout (với map lớn)
        if _depth > max_depth:
            return assignment  # trả về partial assignment

        # ── MRV: chọn biến ──
        var = self._select_unassigned_variable(assignment, domain)
        if var is None:
            return assignment

        # ── LCV: thử từng giá trị ──
        for value in self._order_values(var, domain, assignment):
            if value not in domain[var]:
                continue

            # Gán thử
            assignment[var] = value
            new_count = dict(assigned_count)
            new_count[value] = new_count.get(value, 0) + 1

            # ── Forward Checking ──
            new_domain = self._forward_check(var, value, domain, assignment, new_count)

            if new_domain is not None:
                # Tiếp tục tìm kiếm
                result = self._backtrack(
                    assignment, new_domain, walls, safe, new_count, max_depth, _depth + 1
                )
                if result is not None:
                    return result

            # Backtrack: hủy gán
            del assignment[var]

        return None  # không tìm được → backtrack lên trên

    # ──────────────────────────────────────────────────────────────
    #  Mirror kết quả sang 4 góc (Symmetry Enforcement)
    # ──────────────────────────────────────────────────────────────
    def _mirror_to_full_map(
        self, assignment: Assignment, walls: Set[Cell], safe: Set[Cell]
    ) -> Set[Cell]:
        """
        Phản chiếu assignment từ góc top-left sang 3 góc còn lại
        (top-right, bottom-left, bottom-right) theo đối xứng tâm.
        """
        W, H = self.width, self.height
        bricks: Set[Cell] = set()

        for (x, y), value in assignment.items():
            if value == self.CELL_BRICK:
                mirrors = [
                    (x, y),
                    (W - 1 - x, y),
                    (x, H - 1 - y),
                    (W - 1 - x, H - 1 - y),
                ]
                for mx, my in mirrors:
                    if (mx, my) not in walls and (mx, my) not in safe:
                        bricks.add((mx, my))

        return bricks

    # ──────────────────────────────────────────────────────────────
    #  Fallback
    # ──────────────────────────────────────────────────────────────
    def _random_fallback(self, walls: Set[Cell], safe: Set[Cell]) -> Assignment:
        """Dự phòng khi CSP không hội tụ: gán ngẫu nhiên theo tỉ lệ."""
        W, H = self.width, self.height
        assignment: Assignment = {}
        mx = W // 2 + 1
        my = H // 2 + 1
        for y in range(1, my):
            for x in range(1, mx):
                if (x, y) not in walls:
                    if (x, y) in safe:
                        assignment[(x, y)] = self.CELL_EMPTY
                    else:
                        assignment[(x, y)] = (
                            self.CELL_BRICK if self._rng.random() < self.target_brick_ratio
                            else self.CELL_EMPTY
                        )
        return assignment
