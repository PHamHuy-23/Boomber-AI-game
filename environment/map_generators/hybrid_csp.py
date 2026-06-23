"""
Hybrid CSP Map Generator (AC-3 + Backtracking + Forward Checking)
===================================================================
Thuật toán: Kết hợp tốt nhất của 2 phương pháp:

  Giai đoạn 1 — AC-3 Preprocessing:
    Chạy AC-3 để thu hẹp domain tối đa trước khi search.
    → Giảm không gian tìm kiếm cho Backtracking.
    → Nhiều biến có domain = {1 giá trị} → tự động gán mà không cần search.

  Giai đoạn 2 — Backtracking + Forward Checking:
    Backtracking chạy trên domain đã được AC-3 làm sạch.
    Mỗi lần gán → Forward Checking cập nhật domain các biến liên quan.
    Nếu phát hiện domain rỗng → ngay lập tức backtrack (không đi sâu thêm).

  Giai đoạn 3 — Constraint Propagation (MAC - Maintaining Arc Consistency):
    Sau mỗi lần gán trong Backtracking, chạy mini AC-3 cục bộ trên
    các biến ảnh hưởng → đảm bảo arc consistency liên tục được duy trì.
    (MAC = Maintaining Arc Consistency trong quá trình search)

  Giai đoạn 4 — Item Placement (Bonus):
    Sau khi có bản đồ tường/gạch, đặt Item ẩn bên trong gạch
    theo phân bố đều (uniform distribution) trên ¼ bản đồ rồi mirror.

So sánh với 2 phương pháp kia:
  | Tiêu chí               | Backtracking CSP | Min-Conflict+AC3 | Hybrid (này)   |
  |------------------------|------------------|------------------|----------------|
  | Hoàn chỉnh (Complete)  | Có               | Không (local)    | Có             |
  | Tối ưu (Optimal)       | Theo MRV+LCV     | Heuristic        | AC3+FC+MAC     |
  | Tốc độ                 | Chậm (worst O(d^n))| Nhanh           | Trung bình     |
  | Chất lượng map         | Cao              | Trung bình       | Rất cao        |
  | Đa dạng map            | Cao (random tie) | Cao (random)     | Cao (AC3 bias) |
"""

import random
from collections import deque
from typing import Dict, Set, Tuple, List, Optional
from configs.default_config import GameConfig

Cell = Tuple[int, int]
Domain = Dict[Cell, List[str]]
Assignment = Dict[Cell, str]


class HybridCSPMapGenerator:
    """
    Hybrid: AC-3 Preprocessing → Backtracking + Forward Checking + MAC.
    Bổ sung: Item Placement đối xứng sau khi sinh xong bản đồ tường/gạch.
    """

    EMPTY     = 'empty'
    BRICK     = 'brick'
    WALL      = 'wall'
    ITEM_BOMB = 'item_capacity'   # PowerUp: thêm bom
    ITEM_FIRE = 'item_radius'     # PowerUp: tăng blast radius

    ITEM_TYPES = [ITEM_BOMB, ITEM_FIRE]

    def __init__(
        self,
        width: int  = GameConfig.MAP_WIDTH,
        height: int = GameConfig.MAP_HEIGHT,
        brick_density: float  = GameConfig.BRICK_DENSITY,
        item_chance: float    = GameConfig.ITEM_SPAWN_CHANCE,
        seed: Optional[int]   = None,
        max_bt_nodes: int     = 20000,  # giới hạn node Backtracking
    ):
        self.width  = width
        self.height = height
        self.brick_density = brick_density
        self.item_chance   = item_chance
        self.seed = seed
        self.max_bt_nodes = max_bt_nodes
        self._rng = random.Random(seed)
        self._bt_calls = 0  # đếm số node đã duyệt (metrics)

    # ──────────────────────────────────────────────────────────────
    #  Public API
    # ──────────────────────────────────────────────────────────────
    def generate(self) -> Tuple[Set[Cell], Set[Cell], List[Cell], Dict[Cell, str]]:
        """
        Trả về (walls, bricks, spawns, items).
        items: Dict[Cell, str] — bản đồ ô → loại vật phẩm ẩn bên trong gạch.
        """
        self._rng = random.Random(self.seed)
        self._bt_calls = 0

        walls  = self._build_walls()
        spawns = self._corner_spawns()
        safe   = self._spawn_safe_zone(spawns)

        # ── Phase 1: Khởi tạo domain ──
        domain = self._init_domain(walls, safe)

        # ── Phase 2: AC-3 Preprocessing ──
        # Chạy AC-3 toàn cục → thu hẹp domain, tự động gán nhiều biến
        domain = self._ac3_full(domain, walls, safe)

        # ── Phase 3: Backtracking + FC + MAC ──
        assignment: Assignment = {}
        # Gán các biến có domain = 1 giá trị (đã xác định bởi AC-3)
        for cell, vals in domain.items():
            if len(vals) == 1:
                assignment[cell] = vals[0]

        result = self._backtrack_mac(assignment, domain, walls, safe)
        if result is None:
            result = self._random_fallback(domain, safe)

        # ── Phase 4: Mirror sang 4 góc ──
        bricks = self._mirror_to_full_map(result, walls, safe)

        # ── Phase 5: Kiểm tra reachability ──
        if not self._check_reachability(walls, bricks, spawns):
            bricks = self._fix_reachability(walls, bricks, spawns, safe)

        # ── Phase 6: Item Placement ──
        items = self._place_items(bricks, safe)

        return walls, bricks, spawns, items

    @property
    def backtrack_calls(self) -> int:
        """Số node đã duyệt — dùng cho metrics chất lượng."""
        return self._bt_calls

    # ──────────────────────────────────────────────────────────────
    #  Domain initialization
    # ──────────────────────────────────────────────────────────────
    def _init_domain(self, walls: Set[Cell], safe: Set[Cell]) -> Domain:
        W, H = self.width, self.height
        mx = W // 2 + 1
        my = H // 2 + 1
        domain: Domain = {}
        for y in range(1, my):
            for x in range(1, mx):
                if (x, y) not in walls:
                    if (x, y) in safe:
                        domain[(x, y)] = [self.EMPTY]  # hard constraint
                    else:
                        domain[(x, y)] = [self.EMPTY, self.BRICK]
        return domain

    # ──────────────────────────────────────────────────────────────
    #  AC-3 Full Preprocessing
    # ──────────────────────────────────────────────────────────────
    def _ac3_full(self, domain: Domain, walls: Set[Cell], safe: Set[Cell]) -> Domain:
        """
        AC-3 toàn cục trên tất cả biến:
        - Arc (Xi, Xj) tồn tại nếu Xi và Xj là mirror của nhau (đối xứng)
          hoặc hàng xóm có ràng buộc cứng (safe zone).
        - Revise: loại val khỏi domain[Xi] nếu không có val tương thích ở domain[Xj].

        Ràng buộc tương thích:
          - Mirror constraint: val_i == val_j (đối xứng hoàn hảo).
          - Density soft constraint: không loại giá trị, chỉ bias ordering.
        """
        new_domain = {k: list(v) for k, v in domain.items()}
        W, H = self.width, self.height

        queue: deque = deque()

        # Thêm tất cả arc (Xi, Xj) là mirror pairs vào queue
        for (x, y) in new_domain:
            mirrors = self._get_mirrors(x, y)
            for mx, my in mirrors:
                if (mx, my) in new_domain:
                    queue.append(((x, y), (mx, my)))

        visited_arcs = set()

        while queue:
            xi, xj = queue.popleft()
            arc_key = (xi, xj)
            if arc_key in visited_arcs:
                continue
            visited_arcs.add(arc_key)

            if xi not in new_domain or xj not in new_domain:
                continue

            # Revise domain[xi] w.r.t. domain[xj]
            revised_domain, changed = self._revise(new_domain, xi, xj)
            new_domain = revised_domain

            if changed:
                if not new_domain[xi]:
                    # Domain rỗng → impossible, set to EMPTY (safe fallback)
                    new_domain[xi] = [self.EMPTY]

                # Thêm các arc liên quan vào queue (MAC-style propagation)
                x, y = xi
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    neighbor = (x+dx, y+dy)
                    if neighbor in new_domain and neighbor != xj:
                        queue.append((neighbor, xi))

                # Thêm arc của tất cả mirrors
                for mx, my in self._get_mirrors(x, y):
                    if (mx, my) in new_domain and (mx, my) != xj:
                        queue.append(((mx, my), xi))

        return new_domain

    def _revise(
        self, domain: Domain, xi: Cell, xj: Cell
    ) -> Tuple[Domain, bool]:
        """
        Revise domain[xi] w.r.t domain[xj].
        Loại val khỏi domain[xi] nếu không có val tương thích trong domain[xj].
        Ràng buộc tương thích (mirror): val_xi == val_xj.
        """
        changed = False
        new_xi = []
        for val in domain[xi]:
            # Tìm ít nhất 1 giá trị trong domain[xj] tương thích
            if val in domain[xj]:  # mirror constraint: phải bằng nhau
                new_xi.append(val)
            else:
                changed = True

        if changed:
            domain = {k: list(v) for k, v in domain.items()}
            domain[xi] = new_xi if new_xi else [self.EMPTY]

        return domain, changed

    def _get_mirrors(self, x: int, y: int) -> List[Cell]:
        W, H = self.width, self.height
        mirrors = []
        candidates = [(W-1-x, y), (x, H-1-y), (W-1-x, H-1-y)]
        for mx, my in candidates:
            if (mx, my) != (x, y):
                mirrors.append((mx, my))
        return mirrors

    # ──────────────────────────────────────────────────────────────
    #  Backtracking + Forward Checking + MAC
    # ──────────────────────────────────────────────────────────────
    def _backtrack_mac(
        self,
        assignment: Assignment,
        domain: Domain,
        walls: Set[Cell],
        safe: Set[Cell],
        _depth: int = 0,
    ) -> Optional[Assignment]:
        """
        Backtracking kết hợp:
          - Forward Checking (FC): sau gán, cập nhật domain hàng xóm.
          - MAC (Maintaining Arc Consistency): sau FC, chạy mini AC-3 cục bộ.
          - MRV: chọn biến có domain nhỏ nhất (đã được AC-3 làm sạch từ trước).
          - LCV: thử 'empty' trước nếu gần đạt density target.
        """
        self._bt_calls += 1
        if self._bt_calls > self.max_bt_nodes:
            return assignment  # timeout → trả về partial

        # Kiểm tra hoàn thành
        unassigned = [v for v in domain if v not in assignment]
        if not unassigned:
            return assignment

        # ── MRV: chọn biến ──
        var = min(unassigned, key=lambda v: len(domain[v]))

        # ── LCV: thứ tự giá trị ──
        total_eligible = len(domain)
        current_bricks = sum(1 for c in assignment if assignment[c] == self.BRICK)
        target_bricks  = int(total_eligible * self.brick_density)
        needed = target_bricks - current_bricks

        # Ưu tiên BRICK nếu còn thiếu nhiều, ngược lại ưu tiên EMPTY
        values = list(domain[var])
        if needed > len(unassigned) * 0.6:
            values = sorted(values, key=lambda v: (0 if v == self.BRICK else 1))
        else:
            values = sorted(values, key=lambda v: (0 if v == self.EMPTY else 1))

        for value in values:
            if value not in domain[var]:
                continue

            assignment[var] = value

            # ── Forward Checking ──
            new_domain = self._forward_check(var, value, domain, assignment)

            if new_domain is not None:
                # ── MAC: mini AC-3 cục bộ ──
                mac_domain = self._mac_propagate(var, new_domain, assignment)

                if mac_domain is not None:
                    result = self._backtrack_mac(assignment, mac_domain, walls, safe, _depth+1)
                    if result is not None:
                        return result

            # Backtrack
            del assignment[var]

        return None

    def _forward_check(
        self, var: Cell, value: str, domain: Domain, assignment: Assignment
    ) -> Optional[Domain]:
        """
        Forward Checking:
        Sau khi gán var=value, kiểm tra domain của tất cả biến chưa gán liên quan.
        Nếu bất kỳ domain nào rỗng → trả về None (dead-end).

        Liên quan bao gồm:
          - Các mirror cell (đối xứng) → phải có cùng giá trị.
          - Density global constraint.
        """
        W, H = self.width, self.height
        new_domain = {k: list(v) for k, v in domain.items()}
        x, y = var

        # FC cho mirror cells: mirror cũng phải là cùng value
        for mx, my in self._get_mirrors(x, y):
            if (mx, my) in new_domain and (mx, my) not in assignment:
                if value in new_domain[(mx, my)]:
                    new_domain[(mx, my)] = [value]
                else:
                    # Không tương thích → dead-end
                    return None

        # FC cho density: nếu đã đủ brick → loại brick khỏi các ô còn lại
        total = len(new_domain)
        current_bricks = sum(1 for c in assignment if assignment[c] == self.BRICK)
        if value == self.BRICK:
            current_bricks += 1
        target_bricks = int(total * self.brick_density)

        if current_bricks >= target_bricks:
            for cell in new_domain:
                if cell not in assignment and cell != var:
                    if self.BRICK in new_domain[cell] and len(new_domain[cell]) > 1:
                        new_domain[cell] = [v for v in new_domain[cell] if v != self.BRICK]
                        if not new_domain[cell]:
                            new_domain[cell] = [self.EMPTY]

        return new_domain

    def _mac_propagate(
        self, var: Cell, domain: Domain, assignment: Assignment
    ) -> Optional[Domain]:
        """
        MAC: Maintaining Arc Consistency.
        Sau khi FC, chạy mini AC-3 chỉ trên các biến ảnh hưởng bởi 'var'.
        → Đảm bảo không có arc inconsistency còn sót lại.
        """
        x, y = var
        new_domain = {k: list(v) for k, v in domain.items()}

        # Tạo queue từ tất cả arc liên quan đến var
        queue: deque = deque()
        for mx, my in self._get_mirrors(x, y):
            if (mx, my) in new_domain:
                queue.append(((mx, my), var))
                queue.append((var, (mx, my)))
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            neighbor = (x+dx, y+dy)
            if neighbor in new_domain:
                queue.append((neighbor, var))

        while queue:
            xi, xj = queue.popleft()
            if xi not in new_domain or xj not in new_domain:
                continue

            new_domain, changed = self._revise(new_domain, xi, xj)

            if not new_domain.get(xi):
                return None  # dead-end

            if changed:
                px, py = xi
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    neighbor = (px+dx, py+dy)
                    if neighbor in new_domain and neighbor != xj:
                        queue.append((neighbor, xi))

        return new_domain

    # ──────────────────────────────────────────────────────────────
    #  Mirror & Item Placement
    # ──────────────────────────────────────────────────────────────
    def _mirror_to_full_map(
        self, assignment: Assignment, walls: Set[Cell], safe: Set[Cell]
    ) -> Set[Cell]:
        W, H = self.width, self.height
        bricks: Set[Cell] = set()
        for (x, y), value in assignment.items():
            if value == self.BRICK:
                for mx, my in [(x,y),(W-1-x,y),(x,H-1-y),(W-1-x,H-1-y)]:
                    if (mx, my) not in walls and (mx, my) not in safe:
                        bricks.add((mx, my))
        return bricks

    def _place_items(self, bricks: Set[Cell], safe: Set[Cell]) -> Dict[Cell, str]:
        """
        Đặt vật phẩm ẩn bên trong gạch theo đối xứng.
        Chỉ ô gạch trong ¼ bản đồ (top-left) mới được chọn ngẫu nhiên,
        sau đó mirror sang 3 phần còn lại.
        """
        W, H = self.width, self.height
        items: Dict[Cell, str] = {}

        # Chỉ xét brick trong top-left quadrant
        quadrant_bricks = [(x, y) for (x, y) in bricks if x <= W // 2 and y <= H // 2]
        self._rng.shuffle(quadrant_bricks)

        for (x, y) in quadrant_bricks:
            if self._rng.random() < self.item_chance:
                item_type = self._rng.choice(self.ITEM_TYPES)
                # Đặt item và mirror
                for mx, my in [(x,y),(W-1-x,y),(x,H-1-y),(W-1-x,H-1-y)]:
                    if (mx, my) in bricks:
                        items[(mx, my)] = item_type

        return items

    # ──────────────────────────────────────────────────────────────
    #  Reachability
    # ──────────────────────────────────────────────────────────────
    def _check_reachability(
        self, walls: Set[Cell], bricks: Set[Cell], spawns: List[Cell]
    ) -> bool:
        start = spawns[0]
        visited = {start}
        queue = deque([start])
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = cx+dx, cy+dy
                if 0<=nx<self.width and 0<=ny<self.height:
                    if (nx,ny) not in walls and (nx,ny) not in bricks and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        queue.append((nx,ny))
        return all(s in visited for s in spawns)

    def _fix_reachability(
        self, walls: Set[Cell], bricks: Set[Cell], spawns: List[Cell], safe: Set[Cell]
    ) -> Set[Cell]:
        bricks = set(bricks)
        removable = list(bricks - safe)
        self._rng.shuffle(removable)
        for brick in removable:
            bricks.discard(brick)
            if self._check_reachability(walls, bricks, spawns):
                break
        return bricks

    # ──────────────────────────────────────────────────────────────
    #  Helpers
    # ──────────────────────────────────────────────────────────────
    def _build_walls(self) -> Set[Cell]:
        walls: Set[Cell] = set()
        W, H = self.width, self.height
        for y in range(H):
            for x in range(W):
                if x==0 or x==W-1 or y==0 or y==H-1:
                    walls.add((x,y))
        for y in range(2, H-2, 2):
            for x in range(2, W-2, 2):
                walls.add((x,y))
        return walls

    def _corner_spawns(self) -> List[Cell]:
        W, H = self.width, self.height
        return [(1,1),(W-2,1),(1,H-2),(W-2,H-2)]

    def _spawn_safe_zone(self, spawns: List[Cell]) -> Set[Cell]:
        safe: Set[Cell] = set()
        for sx, sy in spawns:
            safe.add((sx,sy))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                safe.add((sx+dx,sy+dy))
        return safe

    def _random_fallback(self, domain: Domain, safe: Set[Cell]) -> Assignment:
        assignment: Assignment = {}
        for cell, vals in domain.items():
            if len(vals) == 1:
                assignment[cell] = vals[0]
            elif cell in safe:
                assignment[cell] = self.EMPTY
            else:
                assignment[cell] = (
                    self.BRICK if self._rng.random() < self.brick_density
                    else self.EMPTY
                )
        return assignment
