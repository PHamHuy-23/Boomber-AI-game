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
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (winner_id) REFERENCES agents(id)
);

CREATE TABLE IF NOT EXISTS agent_match_stats (
    match_id TEXT NOT NULL,
    agent_id TEXT NOT NULL,
    rank INTEGER NOT NULL,
    survival_steps INTEGER NOT NULL,
    kills INTEGER NOT NULL,
    suicides INTEGER NOT NULL,
    bricks_destroyed INTEGER NOT NULL,
    items_collected INTEGER NOT NULL,
    avg_latency_ms REAL NOT NULL,
    PRIMARY KEY (match_id, agent_id),
    FOREIGN KEY (match_id) REFERENCES matches(id),
    FOREIGN KEY (agent_id) REFERENCES agents(id)
);
