"""
Map Generator module exposing all CSP-based map generation strategies.

Available generators:
    - BacktrackingCSPMapGenerator   : Backtracking + MRV + LCV + Forward Checking
    - MinConflictCSPMapGenerator    : Min-Conflicts (local search) + AC-3 propagation
    - HybridCSPMapGenerator         : AC-3 preprocessing → Backtracking + Forward Checking (best of both)
"""

from environment.map_generators.backtracking_csp import BacktrackingCSPMapGenerator
from environment.map_generators.min_conflict_csp import MinConflictCSPMapGenerator
from environment.map_generators.hybrid_csp import HybridCSPMapGenerator
from environment.map_generators.map_quality_evaluator import MapQualityEvaluator

__all__ = [
    "BacktrackingCSPMapGenerator",
    "MinConflictCSPMapGenerator",
    "HybridCSPMapGenerator",
    "MapQualityEvaluator",
]
