"""
Kaggle-Ready Map Generator Benchmark
======================================
Script chay danh gia so sanh 3 thuat toan sinh ban do tren 1000 ban do.
Thiet ke de chay truc tiep tren Kaggle Notebooks (CPU-only, khong can GPU).

Cách chạy:
    python benchmarks/map_gen_benchmark.py --num-maps 1000 --seed 42 --output results/

Hoặc trong Kaggle Notebook:
    from benchmarks.map_gen_benchmark import run_full_benchmark
    results = run_full_benchmark(num_maps=1000, seed=42)
    results["comparison_table"]  # bảng so sánh tổng hợp
    results["dataframe"]         # pandas DataFrame để vẽ biểu đồ

THUẬT TOÁN SO SÁNH:
  1. Baseline Random            : Sinh ngẫu nhiên không có CSP (baseline)
  2. Backtracking CSP           : Backtracking + MRV + LCV + Forward Checking
  3. Min-Conflict + AC-3        : Min-Conflicts Local Search + AC-3 Preprocessing
  4. Hybrid CSP (AC-3 + BT+FC+MAC): Kết hợp tốt nhất

OUTPUT:
  - summary.txt    : Bảng so sánh tổng hợp
  - detailed.csv   : Raw metrics của từng bản đồ (để phân tích sâu)
  - boxplot data   : Phân phối aggregate_score của từng thuật toán
"""

import time
import random
import os
import sys
import json
import argparse
import multiprocessing
from multiprocessing import Pool, Manager
from typing import Dict, List, Optional, Tuple, Set

# Fix Windows console UTF-8 encoding
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# So luong CPU su dung mac dinh
NUM_WORKERS = min(4, multiprocessing.cpu_count())

# Đảm bảo import được từ root project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from environment.map_generators.backtracking_csp  import BacktrackingCSPMapGenerator
from environment.map_generators.min_conflict_csp   import MinConflictCSPMapGenerator
from environment.map_generators.hybrid_csp         import HybridCSPMapGenerator
from environment.map_generators.map_quality_evaluator import MapQualityEvaluator
from configs.default_config import GameConfig


# ═══════════════════════════════════════════════════════════════
#  Baseline: Random Map Generator (control group)
# ═══════════════════════════════════════════════════════════════

class RandomMapGenerator:
    """
    Baseline sinh bản đồ ngẫu nhiên hoàn toàn (không có CSP).
    Dùng để làm nhóm đối chứng trong so sánh.
    """
    def __init__(self, width=GameConfig.MAP_WIDTH, height=GameConfig.MAP_HEIGHT,
                 brick_density=GameConfig.BRICK_DENSITY, seed=None):
        self.width  = width
        self.height = height
        self.brick_density = brick_density
        self._rng = random.Random(seed)

    def generate(self) -> Tuple[Set, Set, List]:
        W, H = self.width, self.height
        walls = set()
        # Biên
        for y in range(H):
            for x in range(W):
                if x==0 or x==W-1 or y==0 or y==H-1:
                    walls.add((x,y))
        # Trụ
        for y in range(2, H-2, 2):
            for x in range(2, W-2, 2):
                walls.add((x,y))

        spawns = [(1,1),(W-2,1),(1,H-2),(W-2,H-2)]
        safe = set()
        for sx, sy in spawns:
            safe.add((sx,sy))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                safe.add((sx+dx,sy+dy))

        eligible = [(x,y) for y in range(1,H-1) for x in range(1,W-1)
                    if (x,y) not in walls and (x,y) not in safe]

        self._rng.shuffle(eligible)
        n_bricks = int(len(eligible) * self.brick_density)
        bricks = set(eligible[:n_bricks])

        return walls, bricks, spawns


# ═══════════════════════════════════════════════════════════════
#  Worker function (chay trong process rieng biet)
# ═══════════════════════════════════════════════════════════════

def _worker_task(args: Tuple) -> List[Dict]:
    """
    Ham worker chay trong process rieng (duoc goi boi multiprocessing.Pool).
    Moi worker xu ly mot batch seeds doc lap.

    Args:
        args: (name, generator_class, generator_kwargs, evaluator_config, seed_list, worker_id)

    Returns:
        List[Dict]: Metrics cua tung ban do trong batch nay.
    """
    (
        name,
        generator_class,
        generator_kwargs,
        evaluator_config,
        seed_list,
        worker_id,
    ) = args

    # Khoi tao evaluator trong process con (khong the truyen object qua pickle)
    evaluator = MapQualityEvaluator(**evaluator_config)
    results = []

    for i, seed in enumerate(seed_list):
        gen_kwargs = dict(generator_kwargs)
        gen_kwargs['seed'] = seed

        gen = generator_class(**gen_kwargs)

        # Do thoi gian sinh ban do
        t0 = time.perf_counter()
        result = gen.generate()
        gen_time_ms = (time.perf_counter() - t0) * 1000

        # Unpack result
        if len(result) == 4:
            walls, bricks, spawns, items = result
        else:
            walls, bricks, spawns = result
            items = {}

        bt_calls = getattr(gen, 'backtrack_calls', getattr(gen, '_bt_calls', 0))

        metrics = evaluator.evaluate(
            walls=walls,
            bricks=bricks,
            spawns=spawns,
            items=items if items else None,
            gen_time_ms=gen_time_ms,
            backtrack_calls=bt_calls,
            generator_name=name,
        )
        metrics['seed']       = seed
        metrics['map_index']  = seed  # dung seed lam index de sau merge van sap xep duoc
        metrics['worker_id']  = worker_id
        results.append(metrics)

    return results


# ═══════════════════════════════════════════════════════════════
#  Core Benchmark Runner (multiprocessing)
# ═══════════════════════════════════════════════════════════════

def benchmark_single_generator(
    name: str,
    generator_class,
    generator_kwargs: dict,
    evaluator_config: dict,
    num_maps: int,
    start_seed: int,
    verbose: bool = True,
    num_workers: int = NUM_WORKERS,
) -> List[Dict]:
    """
    Chay danh gia mot thuat toan tren num_maps ban do su dung Pool da tien trinh.

    Co che:
      - Chia num_maps seeds thanh num_workers batch bang nhau.
      - Moi batch duoc chay doc lap boi 1 process trong Pool.
      - Ket qua duoc merge va sap xep lai theo map_index.

    Returns:
        List[Dict]: Danh sach metrics cua tung ban do, sap xep theo seed.
    """
    if verbose:
        print(f"\n{'-'*50}")
        print(f"  Benchmarking: {name}")
        print(f"  Maps: {num_maps} | Workers: {num_workers} | Start Seed: {start_seed}")
        print(f"{'-'*50}")

    # Chia seeds thanh chunks cho tung worker
    all_seeds = list(range(start_seed, start_seed + num_maps))
    chunk_size = (num_maps + num_workers - 1) // num_workers  # ceil division
    seed_chunks = [
        all_seeds[i * chunk_size : (i + 1) * chunk_size]
        for i in range(num_workers)
        if i * chunk_size < len(all_seeds)
    ]

    # Tao danh sach tham so cho tung worker
    worker_args = [
        (name, generator_class, generator_kwargs, evaluator_config, chunk, wid)
        for wid, chunk in enumerate(seed_chunks)
    ]

    t_start = time.perf_counter()

    # Chay Pool voi num_workers process song song
    with Pool(processes=num_workers) as pool:
        batch_results = pool.map(_worker_task, worker_args)

    elapsed = time.perf_counter() - t_start

    # Merge va sap xep ket qua
    all_results: List[Dict] = []
    for batch in batch_results:
        all_results.extend(batch)
    all_results.sort(key=lambda r: r['map_index'])

    # Gan lai map_index theo thu tu 0..N-1
    for idx, r in enumerate(all_results):
        r['map_index'] = idx

    if verbose:
        total_gen_time = sum(r.get('generation_time_ms', 0) for r in all_results)
        avg = sum(r['aggregate_score'] for r in all_results) / len(all_results)
        print(f"  => Done! Avg Score: {avg:.4f} | Wall time: {elapsed:.1f}s "
              f"| Total gen time: {total_gen_time/1000:.1f}s")

    return all_results


# ═══════════════════════════════════════════════════════════════
#  Aggregate Statistics
# ═══════════════════════════════════════════════════════════════

def compute_aggregate_stats(results: List[Dict]) -> Dict:
    """
    Tính thống kê tổng hợp (mean, std, min, max, median) cho mỗi metric.
    """
    if not results:
        return {}

    float_keys = [k for k, v in results[0].items() if isinstance(v, (int, float)) and k not in ('seed', 'map_index')]

    stats = {'generator_name': results[0].get('generator_name', 'Unknown')}

    for key in float_keys:
        vals = [r[key] for r in results if key in r]
        if not vals:
            continue
        vals_sorted = sorted(vals)
        n = len(vals)
        mean = sum(vals) / n
        variance = sum((v - mean)**2 for v in vals) / n
        std = variance ** 0.5
        median = vals_sorted[n // 2]

        stats[f"{key}_mean"]   = round(mean, 4)
        stats[f"{key}_std"]    = round(std, 4)
        stats[f"{key}_min"]    = round(min(vals), 4)
        stats[f"{key}_max"]    = round(max(vals), 4)
        stats[f"{key}_median"] = round(median, 4)

    return stats


# ═══════════════════════════════════════════════════════════════
#  Main Benchmark Orchestrator
# ═══════════════════════════════════════════════════════════════

def run_full_benchmark(
    num_maps: int = 1000,
    seed: int = 42,
    output_dir: Optional[str] = None,
    verbose: bool = True,
    num_workers: int = NUM_WORKERS,
) -> Dict:
    """
    Chay benchmark day du so sanh 4 thuat toan, dung multiprocessing.

    Args:
        num_maps:    So ban do moi thuat toan (mac dinh 1000)
        seed:        Random seed goc
        output_dir:  Thu muc luu ket qua (None = khong luu file)
        verbose:     In tien trinh ra man hinh
        num_workers: So CPU process su dung (mac dinh: min(4, cpu_count))

    Returns:
        Dict chua:
            - 'raw_results':         {name: List[Dict]}
            - 'aggregate_stats':     {name: Dict}
            - 'comparison_table':    str
            - 'winner':              str
    """
    # evaluator_config duoc truyen vao tung worker process (co the pickle)
    evaluator_config = {
        "width":                GameConfig.MAP_WIDTH,
        "height":               GameConfig.MAP_HEIGHT,
        "target_brick_density": GameConfig.BRICK_DENSITY,
    }

    # Định nghĩa các thuật toán cần so sánh
    algorithms = [
        {
            "name":  "Random Baseline",
            "class": RandomMapGenerator,
            "kwargs": {
                "width":         GameConfig.MAP_WIDTH,
                "height":        GameConfig.MAP_HEIGHT,
                "brick_density": GameConfig.BRICK_DENSITY,
            }
        },
        {
            "name":  "Backtracking CSP (MRV+LCV+FC)",
            "class": BacktrackingCSPMapGenerator,
            "kwargs": {
                "width":         GameConfig.MAP_WIDTH,
                "height":        GameConfig.MAP_HEIGHT,
                "brick_density": GameConfig.BRICK_DENSITY,
            }
        },
        {
            "name":  "Min-Conflict + AC-3",
            "class": MinConflictCSPMapGenerator,
            "kwargs": {
                "width":         GameConfig.MAP_WIDTH,
                "height":        GameConfig.MAP_HEIGHT,
                "brick_density": GameConfig.BRICK_DENSITY,
                "max_steps":     3000,
            }
        },
        {
            "name":  "Hybrid CSP (AC-3+BT+FC+MAC)",
            "class": HybridCSPMapGenerator,
            "kwargs": {
                "width":         GameConfig.MAP_WIDTH,
                "height":        GameConfig.MAP_HEIGHT,
                "brick_density": GameConfig.BRICK_DENSITY,
                "item_chance":   GameConfig.ITEM_SPAWN_CHANCE,
                "max_bt_nodes":  15000,
            }
        },
    ]

    if verbose:
        print("=" * 60)
        print("  BOMBERMAN MAP GENERATOR BENCHMARK")
        print(f"  Maps per algorithm: {num_maps}")
        print(f"  Total maps:         {num_maps * len(algorithms)}")
        print(f"  Base seed:          {seed}")
        print(f"  CPU workers:        {num_workers} / {multiprocessing.cpu_count()} available")
        print("=" * 60)

    all_raw: Dict[str, List[Dict]] = {}
    all_stats: Dict[str, Dict] = {}
    benchmark_start = time.perf_counter()

    for alg in algorithms:
        raw = benchmark_single_generator(
            name=alg["name"],
            generator_class=alg["class"],
            generator_kwargs=alg["kwargs"],
            evaluator_config=evaluator_config,
            num_maps=num_maps,
            start_seed=seed,
            verbose=verbose,
            num_workers=num_workers,
        )
        all_raw[alg["name"]]   = raw
        all_stats[alg["name"]] = compute_aggregate_stats(raw)

    total_elapsed = time.perf_counter() - benchmark_start

    # ── Tạo comparison summary (1 dòng / thuật toán) ──
    summary_list = []
    for name, stats in all_stats.items():
        summary_list.append({
            "generator_name":        name,
            "aggregate_score":       stats.get("aggregate_score_mean", 0),
            "symmetry_score":        stats.get("symmetry_score_mean", 0),
            "reachability_score":    stats.get("reachability_score_mean", 0),
            "brick_density_accuracy":stats.get("brick_density_accuracy_mean", 0),
            "spawn_safety_score":    stats.get("spawn_safety_score_mean", 0),
            "corridor_diversity":    stats.get("corridor_diversity_mean", 0),
            "map_entropy":           stats.get("map_entropy_mean", 0),
            "longest_open_path_norm":stats.get("longest_open_path_norm_mean", 0),
            "choke_point_count":     stats.get("choke_point_count_mean", 0),
            "generation_time_ms":    stats.get("generation_time_ms_mean", 0),
            "backtrack_calls":       stats.get("backtrack_calls_mean", 0),
        })

    comparison_table = MapQualityEvaluator.compare_multiple(summary_list)

    # ── Xác định winner ──
    winner = max(summary_list, key=lambda x: x["aggregate_score"])["generator_name"]

    if verbose:
        print("\n" + "=" * 60)
        print("  BENCHMARK COMPLETE")
        print(f"  Total elapsed: {total_elapsed:.1f}s")
        print(f"  Speedup est.:  ~{num_workers}x (used {num_workers} workers)")
        print("=" * 60)
        print(comparison_table)
        print(f"\nWINNER: {winner}")

    result = {
        "raw_results":      all_raw,
        "aggregate_stats":  all_stats,
        "summary_list":     summary_list,
        "comparison_table": comparison_table,
        "winner":           winner,
        "total_time_s":     round(total_elapsed, 2),
    }

    # ── Lưu file nếu có output_dir ──
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

        # summary.txt
        with open(os.path.join(output_dir, "summary.txt"), "w", encoding="utf-8") as f:
            f.write(comparison_table)
            f.write(f"\n\nWINNER: {winner}\n")
            f.write(f"Total benchmark time: {total_elapsed:.1f}s\n")

        # aggregate_stats.json
        with open(os.path.join(output_dir, "aggregate_stats.json"), "w", encoding="utf-8") as f:
            json.dump(all_stats, f, indent=2, ensure_ascii=False)

        # detailed CSV (raw metrics)
        _save_detailed_csv(all_raw, os.path.join(output_dir, "detailed_results.csv"))

        if verbose:
            print(f"\n  Results saved to: {output_dir}/")

    # Thử tạo pandas DataFrame nếu có pandas (Kaggle luôn có)
    try:
        import pandas as pd
        all_rows = []
        for name, rows in all_raw.items():
            all_rows.extend(rows)
        result["dataframe"] = pd.DataFrame(all_rows)
        if verbose:
            print("  ✓ pandas DataFrame available at result['dataframe']")
    except ImportError:
        pass

    return result


def _save_detailed_csv(all_raw: Dict[str, List[Dict]], filepath: str):
    """Lưu raw results ra CSV file."""
    if not all_raw:
        return
    all_rows = []
    for name, rows in all_raw.items():
        all_rows.extend(rows)

    if not all_rows:
        return

    keys = list(all_rows[0].keys())
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(",".join(str(k) for k in keys) + "\n")
        for row in all_rows:
            f.write(",".join(str(row.get(k, "")) for k in keys) + "\n")


# ═══════════════════════════════════════════════════════════════
#  Standalone Quick Test
# ═══════════════════════════════════════════════════════════════

def quick_test(num_maps: int = 10, num_workers: int = NUM_WORKERS):
    """Chay nhanh de kiem tra cac generator hoat dong dung."""
    print(f"Quick test: {num_maps} maps/algo | {num_workers} workers")
    results = run_full_benchmark(num_maps=num_maps, seed=0, verbose=True, num_workers=num_workers)
    print("Winner:", results["winner"])
    return results


# ═══════════════════════════════════════════════════════════════
#  CLI Entry Point
# ═══════════════════════════════════════════════════════════════

# QUAN TRONG: guard nay bat buoc de multiprocessing.Pool hoat dong dung tren Windows
# (Windows dung 'spawn' thay vi 'fork', nen can __main__ guard)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Benchmark Bomberman Map Generators (CSP comparison)"
    )
    parser.add_argument("--num-maps",  type=int,   default=1000,
                        help="So ban do moi thuat toan (mac dinh: 1000)")
    parser.add_argument("--seed",      type=int,   default=42,
                        help="Random seed (mac dinh: 42)")
    parser.add_argument("--output",    type=str,   default="results/map_gen_benchmark",
                        help="Thu muc luu ket qua")
    parser.add_argument("--workers",   type=int,   default=NUM_WORKERS,
                        help=f"So CPU worker (mac dinh: {NUM_WORKERS})")
    parser.add_argument("--quick",     action="store_true",
                        help="Chay nhanh 10 maps de kiem tra")
    parser.add_argument("--quiet",     action="store_true",
                        help="Khong in tien trinh")
    args = parser.parse_args()

    if args.quick:
        quick_test(num_maps=10, num_workers=args.workers)
    else:
        run_full_benchmark(
            num_maps=args.num_maps,
            seed=args.seed,
            output_dir=args.output,
            verbose=not args.quiet,
            num_workers=args.workers,
        )
