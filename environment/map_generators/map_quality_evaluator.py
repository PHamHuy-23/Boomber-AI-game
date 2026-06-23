"""
Map Quality Evaluator
======================
Module đánh giá chất lượng bản đồ Bomberman theo nhiều tiêu chí định lượng.

CÁC METRICS ĐƯỢC ĐO:
  1. brick_density_accuracy   : |actual_ratio - target_ratio| (càng nhỏ càng tốt)
  2. symmetry_score           : % cặp ô đối xứng có cùng giá trị (càng cao càng tốt)
  3. reachability_score       : 1.0 nếu 4 spawn kết nối, 0.0 nếu không
  4. open_space_ratio         : % ô đi được / tổng ô (cân bằng là tốt)
  5. spawn_safety_score       : % ô trong safe zone là empty (phải = 1.0)
  6. corridor_diversity       : Độ đa dạng độ rộng hành lang (entropy-based)
  7. item_distribution_score  : Độ đều phân bố vật phẩm trên bản đồ (std dev của density per quadrant)
  8. generation_time_ms       : Thời gian sinh bản đồ (ms)
  9. backtrack_calls          : Số lần backtrack (chỉ với Backtracking/Hybrid agents)
  10. map_entropy             : Entropy Shannon của phân bố ô (đo độ đa dạng tổng thể)
  11. longest_open_path       : Độ dài đường đi dài nhất không bị chặn (BFS diameter)
  12. choke_point_count       : Số điểm cổ chai (ô bị loại sẽ chia đôi bản đồ)

CÁCH HOẠT ĐỘNG:
  - evaluate(walls, bricks, spawns, items=None, gen_time_ms=0.0) → Dict[str, float]
  - compare(results_list) → DataFrame-style comparison table
  - Mỗi metric được chuẩn hóa về [0, 1] (trừ raw counts) trong aggregate_score
  - aggregate_score = weighted average của các metric quan trọng nhất
"""

import math
from collections import deque
from typing import Dict, Set, Tuple, List, Optional

Cell = Tuple[int, int]


class MapQualityEvaluator:
    """
    Đánh giá chất lượng bản đồ Bomberman với bộ metrics toàn diện.

    Sử dụng:
        evaluator = MapQualityEvaluator(width=15, height=13)
        score = evaluator.evaluate(walls, bricks, spawns)
        print(evaluator.report(score))
    """

    # Trọng số cho aggregate score (tổng = 1.0)
    WEIGHTS = {
        "symmetry_score":            0.20,  # quan trọng nhất: đối xứng công bằng
        "reachability_score":        0.20,  # bắt buộc: có thể chơi được
        "brick_density_accuracy":    0.15,  # gần target density
        "spawn_safety_score":        0.15,  # an toàn cho người chơi
        "corridor_diversity":        0.10,  # đa dạng hành lang
        "open_space_ratio":          0.05,  # không quá chật hoặc trống
        "item_distribution_score":   0.05,  # phân bố vật phẩm đều
        "map_entropy":               0.05,  # đa dạng tổng thể
        "longest_open_path_norm":    0.05,  # không gian di chuyển thoáng
    }

    def __init__(
        self,
        width: int = 15,
        height: int = 13,
        target_brick_density: float = 0.35,
        target_open_space: float = 0.55,  # mong muốn 55% ô có thể đi
    ):
        self.width  = width
        self.height = height
        self.target_brick_density = target_brick_density
        self.target_open_space = target_open_space

    # ──────────────────────────────────────────────────────────────
    #  Main Evaluation Entry Point
    # ──────────────────────────────────────────────────────────────
    def evaluate(
        self,
        walls: Set[Cell],
        bricks: Set[Cell],
        spawns: List[Cell],
        items: Optional[Dict[Cell, str]] = None,
        gen_time_ms: float = 0.0,
        backtrack_calls: int = 0,
        generator_name: str = "Unknown",
    ) -> Dict[str, float]:
        """
        Đánh giá toàn diện một bản đồ.

        Args:
            walls:           Set ô tường cố định (bao gồm biên + trụ)
            bricks:          Set ô gạch có thể phá
            spawns:          Danh sách 4 điểm xuất phát
            items:           Dict ô → loại vật phẩm (optional)
            gen_time_ms:     Thời gian sinh bản đồ (ms)
            backtrack_calls: Số lần backtrack (0 nếu không dùng BT)
            generator_name:  Tên thuật toán

        Returns:
            Dict các metric và aggregate_score tổng hợp.
        """
        W, H = self.width, self.height
        total_cells = W * H
        inner_cells = [(x, y) for y in range(H) for x in range(W) if (x,y) not in walls]

        # 1. Brick density accuracy
        eligible = [c for c in inner_cells if c not in [s for s in spawns]]
        actual_density = len(bricks) / max(len(eligible), 1)
        density_accuracy = max(0.0, 1.0 - abs(actual_density - self.target_brick_density) / self.target_brick_density)

        # 2. Symmetry score
        symmetry = self._compute_symmetry(walls, bricks)

        # 3. Reachability
        reachability = 1.0 if self._check_reachability(walls, bricks, spawns) else 0.0

        # 4. Open space ratio
        walkable = [c for c in inner_cells if c not in bricks]
        open_ratio = len(walkable) / max(len(inner_cells), 1)
        # Độ gần với target (55%)
        open_score = max(0.0, 1.0 - abs(open_ratio - self.target_open_space) / self.target_open_space)

        # 5. Spawn safety
        safe_zone = self._compute_safe_zone(spawns)
        safe_score = sum(1 for c in safe_zone if c not in bricks and c not in walls) / max(len(safe_zone), 1)

        # 6. Corridor diversity (entropy of local corridor widths)
        corridor_div = self._corridor_diversity(walls, bricks)

        # 7. Item distribution score
        item_dist = self._item_distribution(bricks, items) if items else 0.5

        # 8. Map entropy (Shannon entropy of cell type distribution)
        map_ent = self._map_entropy(walls, bricks, total_cells)

        # 9. Longest open path (BFS diameter estimate)
        longest = self._longest_open_path(walls, bricks, spawns)
        max_possible = W + H  # Manhattan upper bound
        longest_norm = min(1.0, longest / max_possible)

        # 10. Choke point count (structural metric)
        choke_count = self._count_choke_points(walls, bricks, spawns)

        metrics = {
            "generator_name":           generator_name,
            # Raw metrics
            "brick_density_actual":     round(actual_density, 4),
            "brick_density_accuracy":   round(density_accuracy, 4),
            "symmetry_score":           round(symmetry, 4),
            "reachability_score":       round(reachability, 4),
            "open_space_ratio":         round(open_ratio, 4),
            "open_space_score":         round(open_score, 4),
            "spawn_safety_score":       round(safe_score, 4),
            "corridor_diversity":       round(corridor_div, 4),
            "item_distribution_score":  round(item_dist, 4),
            "map_entropy":              round(map_ent, 4),
            "longest_open_path":        longest,
            "longest_open_path_norm":   round(longest_norm, 4),
            "choke_point_count":        choke_count,
            # Performance metrics
            "generation_time_ms":       round(gen_time_ms, 3),
            "backtrack_calls":          backtrack_calls,
        }

        # Aggregate score
        metrics["aggregate_score"] = round(self._aggregate(metrics), 4)

        return metrics

    # ──────────────────────────────────────────────────────────────
    #  Individual Metrics
    # ──────────────────────────────────────────────────────────────
    def _compute_symmetry(self, walls: Set[Cell], bricks: Set[Cell]) -> float:
        """
        Đo độ đối xứng: duyệt tất cả cặp (x,y) và (W-1-x, y), (x, H-1-y).
        Tính % cặp có cùng loại ô (cả 4 góc đối xứng).
        """
        W, H = self.width, self.height
        total = 0
        matching = 0

        def cell_type(c: Cell) -> str:
            if c in walls: return 'wall'
            if c in bricks: return 'brick'
            return 'empty'

        for y in range(H // 2 + 1):
            for x in range(W // 2 + 1):
                cells = [(x,y), (W-1-x,y), (x,H-1-y), (W-1-x,H-1-y)]
                types = [cell_type(c) for c in cells]
                total += 1
                if len(set(types)) == 1:  # tất cả 4 góc cùng loại
                    matching += 1

        return matching / max(total, 1)

    def _check_reachability(
        self, walls: Set[Cell], bricks: Set[Cell], spawns: List[Cell]
    ) -> bool:
        """BFS từ spawn[0] kiểm tra có đến được 3 spawn còn lại không."""
        if not spawns:
            return False
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

    def _compute_safe_zone(self, spawns: List[Cell]) -> Set[Cell]:
        safe: Set[Cell] = set()
        for sx, sy in spawns:
            safe.add((sx,sy))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                safe.add((sx+dx,sy+dy))
        return safe

    def _corridor_diversity(self, walls: Set[Cell], bricks: Set[Cell]) -> float:
        """
        Đo độ đa dạng của hành lang.
        Thuật toán:
          1. Với mỗi ô đi được (x, y), đo "local width" = số ô empty trong hàng (row) và cột (col)
             trong một cửa sổ ±3.
          2. Tính entropy Shannon của phân bố width → diversity cao = hành lang đa dạng.
        """
        W, H = self.width, self.height
        widths = []

        for y in range(1, H-1):
            for x in range(1, W-1):
                if (x,y) in walls or (x,y) in bricks:
                    continue
                # Đếm ô empty liên tiếp theo chiều ngang
                w = 0
                for dx in range(-3, 4):
                    nx = x + dx
                    if 0 <= nx < W and (nx,y) not in walls and (nx,y) not in bricks:
                        w += 1
                widths.append(w)

        if not widths:
            return 0.0

        # Shannon entropy của phân bố width
        from collections import Counter
        counter = Counter(widths)
        total = sum(counter.values())
        entropy = -sum((c/total) * math.log2(c/total) for c in counter.values())
        # Chuẩn hóa về [0,1]: max entropy ≈ log2(7) ≈ 2.81
        return min(1.0, entropy / 2.81)

    def _item_distribution(
        self, bricks: Set[Cell], items: Dict[Cell, str]
    ) -> float:
        """
        Đo độ đều phân bố vật phẩm trên 4 góc bản đồ.
        Score = 1.0 nếu phân bố hoàn toàn đều giữa 4 quadrant.
        Score giảm theo độ lệch chuẩn của số item per quadrant.
        """
        W, H = self.width, self.height
        mid_x, mid_y = W // 2, H // 2

        quadrant_counts = [0, 0, 0, 0]
        for (x, y) in items:
            if x <= mid_x and y <= mid_y:
                quadrant_counts[0] += 1
            elif x > mid_x and y <= mid_y:
                quadrant_counts[1] += 1
            elif x <= mid_x and y > mid_y:
                quadrant_counts[2] += 1
            else:
                quadrant_counts[3] += 1

        if sum(quadrant_counts) == 0:
            return 1.0  # không có item → neutral

        mean = sum(quadrant_counts) / 4
        variance = sum((c - mean) ** 2 for c in quadrant_counts) / 4
        std_dev = math.sqrt(variance)
        # Normalize: std_dev = 0 → score=1.0, std_dev lớn → score giảm
        return max(0.0, 1.0 - std_dev / max(mean, 1))

    def _map_entropy(self, walls: Set[Cell], bricks: Set[Cell], total: int) -> float:
        """
        Shannon entropy của phân bố loại ô: wall/brick/empty.
        Entropy cao = bản đồ đa dạng (tốt cho gameplay).
        """
        n_wall  = len(walls)
        n_brick = len(bricks)
        n_empty = total - n_wall - n_brick
        counts  = [n_wall, n_brick, n_empty]
        total_c = sum(counts)
        if total_c == 0:
            return 0.0

        entropy = 0.0
        for c in counts:
            if c > 0:
                p = c / total_c
                entropy -= p * math.log2(p)

        # Chuẩn hóa: max entropy với 3 loại = log2(3) ≈ 1.585
        return min(1.0, entropy / math.log2(3))

    def _longest_open_path(
        self, walls: Set[Cell], bricks: Set[Cell], spawns: List[Cell]
    ) -> int:
        """
        Ước tính đường kính của không gian đi được (BFS-diameter).
        Chạy BFS từ mỗi spawn, lấy max khoảng cách.
        """
        max_dist = 0
        for start in spawns:
            dist = self._bfs_max_distance(walls, bricks, start)
            max_dist = max(max_dist, dist)
        return max_dist

    def _bfs_max_distance(
        self, walls: Set[Cell], bricks: Set[Cell], start: Cell
    ) -> int:
        """BFS từ start, trả về khoảng cách xa nhất đến được."""
        visited = {start: 0}
        queue = deque([start])
        max_d = 0
        while queue:
            cx, cy = queue.popleft()
            d = visited[(cx, cy)]
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = cx+dx, cy+dy
                if 0<=nx<self.width and 0<=ny<self.height:
                    if (nx,ny) not in walls and (nx,ny) not in bricks and (nx,ny) not in visited:
                        visited[(nx,ny)] = d + 1
                        max_d = max(max_d, d+1)
                        queue.append((nx,ny))
        return max_d

    def _count_choke_points(
        self, walls: Set[Cell], bricks: Set[Cell], spawns: List[Cell]
    ) -> int:
        """
        Đếm số ô cổ chai (choke point): ô empty mà nếu bị chặn sẽ
        chia bản đồ thành nhiều vùng không kết nối.

        Thuật toán: Articulation Point trong đồ thị ô đi được.
        Dùng DFS với stack để tìm articulation points.
        """
        # Xây đồ thị ô đi được
        walkable = set()
        for y in range(self.height):
            for x in range(self.width):
                if (x,y) not in walls and (x,y) not in bricks:
                    walkable.add((x,y))

        if not walkable:
            return 0

        # Tarjan's Articulation Point Algorithm
        visited = {}
        low = {}
        parent = {}
        ap_count = 0
        timer = [0]

        def dfs(u: Cell):
            nonlocal ap_count
            visited[u] = low[u] = timer[0]
            timer[0] += 1
            children = 0
            x, y = u
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                v = (x+dx, y+dy)
                if v not in walkable:
                    continue
                if v not in visited:
                    children += 1
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    # Articulation point condition
                    if parent.get(u) is None and children > 1:
                        ap_count += 1
                    if parent.get(u) is not None and low[v] >= visited[u]:
                        ap_count += 1
                elif v != parent.get(u):
                    low[u] = min(low[u], visited[v])

        start = next(iter(walkable))
        dfs(start)
        return ap_count

    # ──────────────────────────────────────────────────────────────
    #  Aggregate Score
    # ──────────────────────────────────────────────────────────────
    def _aggregate(self, metrics: Dict) -> float:
        """
        Tính điểm tổng hợp (weighted average) từ các metric chính.
        """
        score = 0.0
        for key, weight in self.WEIGHTS.items():
            val = metrics.get(key, 0.0)
            score += weight * float(val)
        return score

    # ──────────────────────────────────────────────────────────────
    #  Reporting
    # ──────────────────────────────────────────────────────────────
    def report(self, metrics: Dict) -> str:
        """Tạo báo cáo dạng text đẹp từ dict metrics."""
        lines = [
            f"{'='*55}",
            f"  MAP QUALITY REPORT — {metrics.get('generator_name', 'Unknown')}",
            f"{'='*55}",
            f"  Aggregate Score:       {metrics.get('aggregate_score', 0):.4f} / 1.0",
            f"{'─'*55}",
            f"  [Structure]",
            f"    Brick Density:       {metrics.get('brick_density_actual', 0):.2%}  (target {self.target_brick_density:.0%})",
            f"    Density Accuracy:    {metrics.get('brick_density_accuracy', 0):.4f}",
            f"    Symmetry Score:      {metrics.get('symmetry_score', 0):.4f}",
            f"    Open Space:          {metrics.get('open_space_ratio', 0):.2%}",
            f"  [Playability]",
            f"    Reachability:        {'✓ Connected' if metrics.get('reachability_score', 0) >= 1.0 else '✗ Disconnected'}",
            f"    Spawn Safety:        {metrics.get('spawn_safety_score', 0):.4f}",
            f"    Choke Points:        {metrics.get('choke_point_count', 0)}",
            f"    Longest Open Path:   {metrics.get('longest_open_path', 0)} tiles",
            f"  [Diversity]",
            f"    Corridor Diversity:  {metrics.get('corridor_diversity', 0):.4f}",
            f"    Map Entropy:         {metrics.get('map_entropy', 0):.4f}",
            f"    Item Distribution:   {metrics.get('item_distribution_score', 0):.4f}",
            f"  [Performance]",
            f"    Generation Time:     {metrics.get('generation_time_ms', 0):.1f} ms",
            f"    Backtrack Calls:     {metrics.get('backtrack_calls', 0)}",
            f"{'='*55}",
        ]
        return "\n".join(lines)

    @staticmethod
    def compare_multiple(results_list: List[Dict]) -> str:
        """
        So sánh nhiều kết quả đánh giá trong bảng text.

        Args:
            results_list: List các dict trả về từ evaluate()

        Returns:
            Bảng so sánh dạng text.
        """
        if not results_list:
            return "No results to compare."

        metrics_to_show = [
            ("aggregate_score",         "Aggregate Score"),
            ("symmetry_score",          "Symmetry"),
            ("reachability_score",      "Reachability"),
            ("brick_density_accuracy",  "Density Acc."),
            ("spawn_safety_score",      "Spawn Safety"),
            ("corridor_diversity",      "Corridor Div."),
            ("map_entropy",             "Map Entropy"),
            ("longest_open_path_norm",  "Open Path"),
            ("choke_point_count",       "Choke Pts"),
            ("generation_time_ms",      "Gen Time (ms)"),
            ("backtrack_calls",         "BT Calls"),
        ]

        names = [r.get("generator_name", f"Agent-{i}") for i, r in enumerate(results_list)]
        col_width = max(16, max(len(n) for n in names) + 2)
        label_width = 18

        header = f"{'Metric':<{label_width}}" + "".join(f"{n:>{col_width}}" for n in names)
        sep    = "─" * len(header)

        lines = [sep, header, sep]

        for key, label in metrics_to_show:
            row = f"{label:<{label_width}}"
            vals = [r.get(key, 0) for r in results_list]
            for i, v in enumerate(vals):
                if isinstance(v, float):
                    row += f"{v:>{col_width}.4f}"
                else:
                    row += f"{v:>{col_width}}"
            lines.append(row)

        lines.append(sep)

        # Highlight winner
        winners = {}
        for key, label in metrics_to_show:
            vals = [r.get(key, 0) for r in results_list]
            # Metrics where lower is better
            if key in ("choke_point_count", "generation_time_ms", "backtrack_calls"):
                best_idx = vals.index(min(vals))
            else:
                best_idx = vals.index(max(vals))
            winners[key] = names[best_idx]

        lines.append("")
        lines.append("WINNERS PER METRIC:")
        for key, label in metrics_to_show:
            lines.append(f"  {label:<20} → {winners[key]}")

        return "\n".join(lines)
