"""Default configuration parameters for BombermanAI."""

class GameConfig:
    # Grid dimensions (usually odd numbers for symmetrical layouts)
    MAP_WIDTH: int = 15
    MAP_HEIGHT: int = 13

    # Agent configuration
    INITIAL_LIVES: int = 3
    INITIAL_MAX_BOMBS: int = 1
    INITIAL_BLAST_RADIUS: int = 2

    # Obstacle densities
    WALL_DENSITY: float = 0.15   # Density of permanent pillars (excluding outer border)
    BRICK_DENSITY: float = 0.35  # Density of destructible bricks

    # Bomb & explosion timings (in game ticks/steps)
    BOMB_LIFETIME: int = 4       # Number of ticks before a bomb explodes
    EXPLOSION_LIFETIME: int = 2  # Number of ticks an explosion remains active

    # Items / Power-ups
    ITEM_SPAWN_CHANCE: float = 0.30  # Probability of spawning an item when a brick is destroyed

    # Enemies
    INITIAL_ENEMY_COUNT: int = 3

    # Game limits
    MAX_STEPS: int = 300
