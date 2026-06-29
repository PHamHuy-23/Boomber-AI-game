-- SQLite schema for Bomberman AI Performance Metrics

CREATE TABLE IF NOT EXISTS agents (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    algorithm TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS matches (
    id TEXT PRIMARY KEY,
    steps INTEGER NOT NULL,
    winner_id TEXT,
    map_preset TEXT,
    seed INTEGER,
    difficulty TEXT,
    enemy_count INTEGER,
    bomb_count INTEGER,
    game_length INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    replay_data TEXT,
    FOREIGN KEY (winner_id) REFERENCES agents(id)
);

CREATE TABLE IF NOT EXISTS agent_match_stats (
    match_id TEXT NOT NULL,
    agent_id TEXT NOT NULL,
    algorithm TEXT,
    rank INTEGER NOT NULL,
    survival_steps INTEGER NOT NULL,
    kills INTEGER NOT NULL,
    suicides INTEGER NOT NULL,
    bricks_destroyed INTEGER NOT NULL,
    items_collected INTEGER NOT NULL,
    avg_latency_ms REAL NOT NULL,
    score INTEGER NOT NULL,
    nodes_expanded INTEGER,
    search_depth INTEGER,
    branching_factor REAL,
    path_length REAL,
    bomb_accuracy REAL,
    escape_success_rate REAL,
    kill_rate REAL,
    death_cause TEXT,
    cpu_usage REAL,
    memory_usage REAL,
    hazard_escape_success INTEGER,
    bomb_placement_success INTEGER,
    enemy_trap_success INTEGER,
    dead_end_escape INTEGER,
    explosion_avoidance INTEGER,
    item_collection INTEGER,
    powerup_usage INTEGER,
    avg_planning_horizon REAL,
    enemy_prediction_accuracy REAL,
    PRIMARY KEY (match_id, agent_id),
    FOREIGN KEY (match_id) REFERENCES matches(id),
    FOREIGN KEY (agent_id) REFERENCES agents(id)
);
