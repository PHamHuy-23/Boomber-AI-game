import os
import sqlite3
import json
from typing import List, Dict, Any, Optional

# Resolve absolute paths relative to database.py location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "bomberman.db")
SCHEMA_PATH = os.path.join(DB_DIR, "schema.sql")

def get_db_connection() -> sqlite3.Connection:
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Initializes the database using the schema.sql script.
    Checks if the schema is outdated and deletes it if necessary.
    """
    os.makedirs(DB_DIR, exist_ok=True)
    
    # Simple migration check: check if DB exists but lacks the new replay_data column
    if os.path.exists(DB_PATH):
        try:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("SELECT replay_data FROM matches LIMIT 1")
            conn.close()
        except sqlite3.OperationalError:
            print("Old database schema detected. Deleting old database to upgrade schema.")
            try:
                conn.close()
            except Exception:
                pass
            try:
                os.remove(DB_PATH)
            except Exception as e:
                print(f"Failed to remove old database: {e}")
                
    if not os.path.exists(SCHEMA_PATH):
        raise FileNotFoundError(f"Schema file not found at {SCHEMA_PATH}")
        
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        schema_sql = f.read()
        
    conn = get_db_connection()
    try:
        conn.executescript(schema_sql)
        conn.commit()
    finally:
        conn.close()

def register_default_agents():
    """
    Seeds default agent profiles in the database.
    """
    default_agents = [
        ("player_1", "Player 1 (User)", "Manual"),
        ("player_2", "Agent 2 (Bot)", "Random"),
        ("player_3", "Agent 3 (Bot)", "Random"),
        ("player_4", "Agent 4 (Bot)", "Random")
    ]
    
    conn = get_db_connection()
    try:
        for aid, name, algo in default_agents:
            conn.execute(
                "INSERT OR IGNORE INTO agents (id, name, algorithm) VALUES (?, ?, ?)",
                (aid, name, algo)
            )
        conn.commit()
    finally:
        conn.close()

def save_match_results(
    match_id: str, 
    steps: int, 
    winner_id: Optional[str], 
    stats_list: List[Dict[str, Any]],
    map_preset: str = "classic",
    seed: int = 42,
    difficulty: str = "Medium",
    enemy_count: int = 1,
    bomb_count: int = 0,
    game_length: int = 0,
    replay_data: str = "[]"
):
    """
    Saves a completed match and its agent stats in a single transaction.
    """
    conn = get_db_connection()
    try:
        with conn:
            # 1. Insert match with all parameters and replay data
            conn.execute(
                """
                INSERT INTO matches (
                    id, steps, winner_id, map_preset, seed, difficulty, enemy_count, bomb_count, game_length, replay_data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (match_id, steps, winner_id, map_preset, seed, difficulty, enemy_count, bomb_count, game_length, replay_data)
            )
            # 2. Insert stats for each agent
            for stats in stats_list:
                conn.execute(
                    """
                    INSERT INTO agent_match_stats (
                        match_id, agent_id, algorithm, rank, survival_steps, kills, suicides, bricks_destroyed, items_collected, avg_latency_ms,
                        score, nodes_expanded, search_depth, branching_factor, path_length, bomb_accuracy, escape_success_rate, kill_rate,
                        death_cause, cpu_usage, memory_usage, hazard_escape_success, bomb_placement_success, enemy_trap_success,
                        dead_end_escape, explosion_avoidance, item_collection, powerup_usage, avg_planning_horizon, enemy_prediction_accuracy
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        match_id,
                        stats["agent_id"],
                        stats.get("algorithm", "minimax"),
                        stats["rank"],
                        stats["survival_steps"],
                        stats["kills"],
                        stats["suicides"],
                        stats["bricks_destroyed"],
                        stats["items_collected"],
                        stats["avg_latency_ms"],
                        stats.get("score", 0),
                        stats.get("nodes_expanded", 0),
                        stats.get("search_depth", 0),
                        stats.get("branching_factor", 0.0),
                        stats.get("path_length", 0.0),
                        stats.get("bomb_accuracy", 0.0),
                        stats.get("escape_success_rate", 0.0),
                        stats.get("kill_rate", 0.0),
                        stats.get("death_cause", "survived"),
                        stats.get("cpu_usage", 0.0),
                        stats.get("memory_usage", 0.0),
                        stats.get("hazard_escape_success", 0),
                        stats.get("bomb_placement_success", 0),
                        stats.get("enemy_trap_success", 0),
                        stats.get("dead_end_escape", 0),
                        stats.get("explosion_avoidance", 0),
                        stats.get("item_collection", 0),
                        stats.get("powerup_usage", 0),
                        stats.get("avg_planning_horizon", 0.0),
                        stats.get("enemy_prediction_accuracy", 0.0)
                    )
                )
    finally:
        conn.close()
