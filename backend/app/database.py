import os
import sqlite3
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
    """
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

def save_match_results(match_id: str, steps: int, winner_id: Optional[str], stats_list: List[Dict[str, Any]]):
    """
    Saves a completed match and its agent stats in a single transaction.
    """
    conn = get_db_connection()
    try:
        with conn:
            # 1. Insert match
            conn.execute(
                "INSERT INTO matches (id, steps, winner_id) VALUES (?, ?, ?)",
                (match_id, steps, winner_id)
            )
            # 2. Insert stats for each agent
            for stats in stats_list:
                conn.execute(
                    """
                    INSERT INTO agent_match_stats (
                        match_id, agent_id, rank, survival_steps, kills, suicides, bricks_destroyed, items_collected, avg_latency_ms
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        match_id,
                        stats["agent_id"],
                        stats["rank"],
                        stats["survival_steps"],
                        stats["kills"],
                        stats["suicides"],
                        stats["bricks_destroyed"],
                        stats["items_collected"],
                        stats["avg_latency_ms"]
                    )
                )
    finally:
        conn.close()
