import os
import pytest
from app import database

@pytest.fixture(autouse=True)
def setup_test_db(tmp_path):
    # Override database path to pointing to a temp path
    test_db = os.path.join(tmp_path, "test_bomberman.db")
    orig_db_path = database.DB_PATH
    database.DB_PATH = test_db
    database.init_db()
    database.register_default_agents()
    yield
    # Restore original path
    database.DB_PATH = orig_db_path

def test_database_initialization():
    conn = database.get_db_connection()
    try:
        # Check if default agents are successfully inserted
        agents = conn.execute("SELECT * FROM agents").fetchall()
        assert len(agents) == 4
        agent_ids = [a["id"] for a in agents]
        assert "player_1" in agent_ids
        assert "player_2" in agent_ids
    finally:
        conn.close()

def test_save_match_and_stats():
    match_id = "test-match-uuid-123"
    steps = 150
    winner_id = "player_1"
    
    stats_list = [
        {
            "agent_id": "player_1",
            "rank": 1,
            "survival_steps": 150,
            "kills": 2,
            "suicides": 0,
            "bricks_destroyed": 10,
            "items_collected": 3,
            "avg_latency_ms": 1.25
        },
        {
            "agent_id": "player_2",
            "rank": 2,
            "survival_steps": 95,
            "kills": 0,
            "suicides": 1,
            "bricks_destroyed": 4,
            "items_collected": 1,
            "avg_latency_ms": 0.85
        }
    ]
    
    # Save results
    database.save_match_results(match_id, steps, winner_id, stats_list)
    
    # Query database and verify
    conn = database.get_db_connection()
    try:
        match_row = conn.execute("SELECT * FROM matches WHERE id = ?", (match_id,)).fetchone()
        assert match_row is not None
        assert match_row["steps"] == 150
        assert match_row["winner_id"] == "player_1"
        
        stats_rows = conn.execute("SELECT * FROM agent_match_stats WHERE match_id = ? ORDER BY rank", (match_id,)).fetchall()
        assert len(stats_rows) == 2
        assert stats_rows[0]["agent_id"] == "player_1"
        assert stats_rows[0]["kills"] == 2
        assert stats_rows[0]["avg_latency_ms"] == 1.25
        assert stats_rows[1]["agent_id"] == "player_2"
        assert stats_rows[1]["suicides"] == 1
    finally:
        conn.close()
