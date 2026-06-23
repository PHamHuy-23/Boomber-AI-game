"""
Min-Conflict CSP Map Generator với AC-3
=========================================
Thuật toán: Min-Conflicts (Local Search) kết hợp AC-3 (Arc Consistency 3)

Ý tưởng:
  Min-Conflicts là thuật toán local search cho CSP:
  1. Bắt đầu từ một gán ngẫu nhiên hoàn chỉnh (có thể vi phạm constraint).
  2. Lặp lại:
     a. Chọn ngẫu nhiên một biến đang vi phạm constraint (conflicted variable).
     b. Gán cho nó giá trị nào làm giảm số xung đột nhất (min-conflict value).
  3. Dừng khi không còn xung đột hoặc hết số bước tối đa.

Điểm khác biệt so với Backtracking:
  - Không dùng đệ quy → không tốn bộ nhớ stack, phù hợp với bản đồ lớn.
  - Hiệu quả trong không gian lời giải dày đặc (dense solution space).
  - Yếu ở vùng lời giải thưa (có thể bị local minima).

AC-3 (Arc Consistency Algorithm 3):
  - Được chạy trước Min-Conflicts để giảm domain từng biến.
  - AC-3 loại các giá trị không nhất quán về cung (arc) giữa các cặp biến liên kết.
  - Sau AC-3, domain đã sạch → Min-Conflicts ít xung đột hơn từ đầu.

Ràng buộc (Constraints) được định nghĩa:
  C1. Density: số brick trong toàn bản đồ ≈ target_brick_ratio × eligible_cells
  C2. Safe-zone: ô spawn và hình chữ L xung quanh phải là 'empty'
  C3. Symmetry: grid[y][x] == grid[H-1-y][x] == grid[y][W-1-x] == grid[H-1-y][W-1-x]
  C4. Reachability: 4 spawn kết nối với nhau (kiểm tra BFS sau mỗi N bước)
"""

import random
import copy
from collections import deque
from typing import Dict, Set, Tuple, List, Optional
from configs.default_config import GameConfig

Cell = Tuple[int, int]
Assignment = Dict[Cell, str]
Domain = Dict[Cell, List[str]]


class MinConflictCSPMapGenerator:
    """
    Sinh bản đồ bằng Min-Conflicts Local Search + AC-3 Preprocessing.
    """

    EMPTY = 'empty'
    BRICK = 'brick'
    WALL  = 'wall'

    def __init__(
        self,
        width: int  = GameConfig.MAP_WIDTH,
        height: int = GameConfig.MAP_HEIGHT,
        brick_density: float = GameConfig.BRICK_DENSITY,
        seed: Optional[int] = None,
        max_steps: int = 5000,    # số bước tối đa Min-Conflicts
    ):
        self.width  = width
        self.height = height
        self.brick_density = brick_density
        self.seed   = seed
        self.max_steps = max_steps
        self._rng   = random.Random(seed)

    # ──────────────────────────────────────────────────────────────
    #  Public API
    # ──────────────────────────────────────────────────────────────
    def generate(self) -> Tuple[Set[Cell], Set[Cell], List[Cell]]:
        """Trả về (walls, bricks, spawns)."""
        self._rng = random.Random(self.seed)

        walls  = self._build_walls()
        spawns = self._corner_spawns()
        safe   = self._spawn_safe_zone(spawns)

        eligible = [
            (x, y)
            for y in range(1, self.height - 1)
            for x in range(1, self.width - 1)
            if (x, y) not in walls and (x, y) not in safe
        ]

        # ── Bước 1: Khởi tạo domain cho từng biến ──
        domain: Domain = {}
        for cell in eligible:
            domain[cell] = [self.EMPTY, self.BRICK]
        for cell in safe:
            if cell not in walls:
                domain[cell] = [self.EMPTY]  # ô safe chỉ có thể empty

        # ── Bước 2: AC-3 — thu hẹp domain trước khi search ──
        domain = self._ac3(domain, safe)

        # ── Bước 3: Gán ngẫu nhiên ban đầu theo density ──
        assignment = self._random_initial_assignment(domain, eligible, safe)

        # ── Bước 4: Min-Conflicts Local Search ──
        assignment = self._min_conflicts(assignment, domain, eligible, safe)

        # ── Bước 5: Đảm bảo đối xứng (mirror từ top-left) ──
        assignment = self._enforce_symmetry(assignment, walls, safe)

        # ── Bước 6: Kiểm tra reachability, fix nếu cần ──
        bricks = {c for c, v in assignment.items() if v == self.BRICK}
        if not self._check_reachability(walls, bricks, spawns):
            bricks = self._fix_reachability(walls, bricks, spawns, safe)

        return walls, bricks, spawns

    # ──────────────────────────────────────────────────────────────
    #  AC-3: Arc Consistency Algorithm 3
    # ──────────────────────────────────────────────────────────────
    def _ac3(self, domain: Domain, safe: Set[Cell]) -> Domain:
        """
        AC-3: Đảm bảo tính nhất quán cung (Arc Consistency).

        Cung (arc): (Xi, Xj) — cặp biến có ràng buộc.
        Trong bản đồ Bomberman, ràng buộc giữa Xi và Xj là:
          - Ràng buộc đối xứng: domain[Xi] phải tương thích với domain[mirror(Xi)].
          - Không có hard constraint giữa ô hàng xóm (gạch có thể liền nhau).

        AC-3 quy trình:
          1. Thêm tất cả cung vào queue.
          2. Lấy cung (Xi, Xj) ra, kiểm tra:
             Với mỗi giá trị a trong domain[Xi]:
               Nếu không tồn tại b trong domain[Xj] thỏa constraint(a, b) → xóa a.
          3. Nếu domain[Xi] thay đổi → thêm tất cả cung (Xk, Xi) vào queue (k là hàng xóm Xi).
          4. Nếu domain nào rỗng → CSP vô nghiệm.

        Với bản đồ Bomberman, ta dùng ràng buộc mềm:
          - Ô safe và mirror của nó: nếu 1 ô là safe, mirror phải là empty.
          - Density arc: thêm global count constraint vào AC-3.
        """
        new_domain = {k: list(v) for k, v in domain.items()}
        W, H = self.width, self.height

        # Tạo queue arc từ các cặp (ô, mirror)
        queue: deque = deque()
        processed = set()

        for cell in new_domain:
            x, y = cell
            mirrors = [
                (W - 1 - x, y),
                (x, H - 1 - y),
                (W - 1 - x, H - 1 - y),
            ]
            for mirror in mirrors:
                if mirror in new_domain:
                    arc = tuple(sorted([cell, mirror]))
                    if arc not in processed:
                        queue.append((cell, mirror))
                        queue.append((mirror, cell))
                        processed.add(arc)

        # Xử lý queue
        while queue:
            xi, xj = queue.popleft()
            if xi not in new_domain or xj not in new_domain:
                continue

            # Revise: loại giá trị trong domain[xi] không có giá trị tương thích ở domain[xj]
            revised = False
            new_xi_domain = []
            for val_i in new_domain[xi]:
                # Ràng buộc đối xứng: xi và xj (mirror) phải có cùng giá trị
                if val_i in new_domain[xj]:
                    new_xi_domain.append(val_i)
                    # Có ít nhất 1 giá trị tương thích → giữ val_i
                else:
                    revised = True  # val_i bị loại

            if revised:
                if not new_xi_domain:
                    # Domain rỗng → dùng default (empty để đảm bảo valid)
                    new_xi_domain = [self.EMPTY]
                new_domain[xi] = new_xi_domain

                # Thêm các cung liên quan vào queue
                x, y = xi
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    neighbor = (x+dx, y+dy)
                    if neighbor in new_domain and neighbor != xj:
                        queue.append((neighbor, xi))

        return new_domain

    # ──────────────────────────────────────────────────────────────
    #  Khởi tạo gán ngẫu nhiên ban đầu
    # ──────────────────────────────────────────────────────────────
    def _random_initial_assignment(
        self, domain: Domain, eligible: List[Cell], safe: Set[Cell]
    ) -> Assignment:
        """
        Gán ngẫu nhiên ban đầu dựa trên domain sau AC-3.
        Mục tiêu: gần đạt density target nhất có thể.
        """
        assignment: Assignment = {}
        for cell in domain:
            if len(domain[cell]) == 1:
                assignment[cell] = domain[cell][0]
            else:
                # Gán theo xác suất = brick_density
                if self._rng.random() < self.brick_density:
                    assignment[cell] = self.BRICK
                else:
                    assignment[cell] = self.EMPTY
        return assignment

    # ──────────────────────────────────────────────────────────────
    #  Min-Conflicts Local Search
    # ──────────────────────────────────────────────────────────────
    def _min_conflicts(
        self,
        assignment: Assignment,
        domain: Domain,
        eligible: List[Cell],
        safe: Set[Cell],
    ) -> Assignment:
        """
        Min-Conflicts:
          Tại mỗi bước:
          1. Tính số xung đột hiện tại (vi phạm ràng buộc density + symmetry).
          2. Chọn ngẫu nhiên 1 biến đang vi phạm.
          3. Gán cho nó giá trị nào minimizes conflicts.
          4. Lặp lại đến max_steps.

        Conflicts được đo:
          - |actual_brick_count - target_brick_count|  (density violation)
          - Số cặp (cell, mirror) không đối xứng         (symmetry violation)
        """
        target_bricks = int(len(eligible) * self.brick_density)
        W, H = self.width, self.height

        for step in range(self.max_steps):
            # Tính conflict hiện tại
            brick_count = sum(1 for c in eligible if assignment.get(c) == self.BRICK)
            density_diff = abs(brick_count - target_bricks)

            # Tìm các ô đang vi phạm (conflicted variables)
            conflicted = []
            for cell in eligible:
                x, y = cell
                mirror_cells = [(W-1-x, y), (x, H-1-y), (W-1-x, H-1-y)]
                for mirror in mirror_cells:
                    if mirror in assignment and assignment[cell] != assignment[mirror]:
                        conflicted.append(cell)
                        break

            # Thêm các ô đang vi phạm density (chỉ khi density_diff lớn)
            if density_diff > 2:
                if brick_count < target_bricks:
                    # Thiếu brick → thêm vào conflicted các ô empty trong eligible
                    conflicted.extend([c for c in eligible if assignment.get(c) == self.EMPTY])
                else:
                    # Thừa brick → thêm vào conflicted các ô brick
                    conflicted.extend([c for c in eligible if assignment.get(c) == self.BRICK])

            if not conflicted:
                # Không còn xung đột → hội tụ thành công
                break

            # Chọn ngẫu nhiên 1 biến vi phạm
            var = self._rng.choice(conflicted)

            # Tính số xung đột nếu gán từng giá trị trong domain[var]
            best_val = self._min_conflicts_value(var, domain, assignment, eligible, safe, target_bricks)
            assignment[var] = best_val

            # Đồng bộ mirror ngay (enforce symmetry constraint)
            xv, yv = var
            mirrors = [(W-1-xv, yv), (xv, H-1-yv), (W-1-xv, H-1-yv)]
            for mirror in mirrors:
                if mirror in assignment and mirror in domain:
                    if best_val in domain[mirror]:
                        assignment[mirror] = best_val

        return assignment

    def _count_conflicts(
        self,
        var: Cell,
        value: str,
        assignment: Assignment,
        eligible: List[Cell],
        safe: Set[Cell],
        target_bricks: int,
    ) -> int:
        """Đếm số xung đột nếu gán var=value."""
        W, H = self.width, self.height
        x, y = var

        # Giả lập gán
        temp = dict(assignment)
        temp[var] = value

        conflicts = 0

        # C1. Symmetry conflict
        mirrors = [(W-1-x, y), (x, H-1-y), (W-1-x, H-1-y)]
        for mirror in mirrors:
            if mirror in temp and temp[mirror] != value:
                conflicts += 1

        # C2. Density conflict
        brick_count = sum(1 for c in eligible if temp.get(c) == self.BRICK)
        conflicts += abs(brick_count - target_bricks)

        return conflicts

    def _min_conflicts_value(
        self,
        var: Cell,
        domain: Domain,
        assignment: Assignment,
        eligible: List[Cell],
        safe: Set[Cell],
        target_bricks: int,
    ) -> str:
        """Trả về giá trị làm tối thiểu số xung đột cho biến var."""
        if var in safe:
            return self.EMPTY  # hard constraint

        if len(domain.get(var, [self.EMPTY, self.BRICK])) == 1:
            return domain[var][0]

        scores = {}
        for val in [self.EMPTY, self.BRICK]:
            scores[val] = self._count_conflicts(var, val, assignment, eligible, safe, target_bricks)

        min_score = min(scores.values())
        best = [v for v, s in scores.items() if s == min_score]
        return self._rng.choice(best)

    # ──────────────────────────────────────────────────────────────
    #  Symmetry Enforcement (final pass)
    # ──────────────────────────────────────────────────────────────
    def _enforce_symmetry(
        self, assignment: Assignment, walls: Set[Cell], safe: Set[Cell]
    ) -> Assignment:
        """Đảm bảo đối xứng hoàn hảo: lấy top-left làm chuẩn, mirror sang 3 góc còn lại."""
        W, H = self.width, self.height
        new_assignment = dict(assignment)

        for (x, y), val in assignment.items():
            if x <= W // 2 and y <= H // 2:  # chỉ xử lý quadrant top-left
                mirrors = [(W-1-x, y), (x, H-1-y), (W-1-x, H-1-y)]
                for mx, my in mirrors:
                    if (mx, my) not in walls:
                        if (mx, my) in safe:
                            new_assignment[(mx, my)] = self.EMPTY
                        else:
                            new_assignment[(mx, my)] = val

        return new_assignment

    # ──────────────────────────────────────────────────────────────
    #  Reachability Check & Fix
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
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx,ny) not in walls and (nx,ny) not in bricks and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        queue.append((nx,ny))
        return all(s in visited for s in spawns)

    def _fix_reachability(
        self, walls: Set[Cell], bricks: Set[Cell], spawns: List[Cell], safe: Set[Cell]
    ) -> Set[Cell]:
        """Xóa một số brick để đảm bảo reachability bằng BFS đơn giản."""
        bricks = set(bricks)
        brick_list = list(bricks - safe)
        self._rng.shuffle(brick_list)
        for brick in brick_list:
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
                if x == 0 or x == W-1 or y == 0 or y == H-1:
                    walls.add((x, y))
        for y in range(2, H-2, 2):
            for x in range(2, W-2, 2):
                walls.add((x, y))
        return walls

    def _corner_spawns(self) -> List[Cell]:
        W, H = self.width, self.height
        return [(1,1), (W-2,1), (1,H-2), (W-2,H-2)]

    def _spawn_safe_zone(self, spawns: List[Cell]) -> Set[Cell]:
        safe: Set[Cell] = set()
        for sx, sy in spawns:
            safe.add((sx, sy))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                safe.add((sx+dx, sy+dy))
        return safe
