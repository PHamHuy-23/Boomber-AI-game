from enum import IntEnum
from typing import List, Dict, Set, Tuple
from pydantic import BaseModel, Field

class TileType(IntEnum):
    EMPTY = 0
    WALL = 1
    BRICK = 2
    BOMB = 3
    EXPLOSION = 4
    ITEM_RADIUS = 5
    ITEM_CAPACITY = 6

class Action(IntEnum):
    STOP = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    PLACE_BOMB = 5

class AgentState(BaseModel):
    id: str
    x: int
    y: int
    lives: int = 1
    max_bombs: int = 1  # capacity (starts at 1, max 5)
    bomb_range: int = 1  # radius (starts at 1, max 5)
    bombs_left: int = 1  # remaining bombs to place
    is_alive: bool = True
    direction: str = "down"

class BombState(BaseModel):
    x: int
    y: int
    owner_id: str
    timer: int = 7  # starts at 7, detonates when <= 0
    range: int

class GameState(BaseModel):
    width: int
    height: int
    grid: List[List[int]]  # grid of TileType values
    agents: Dict[str, AgentState]
    bombs: List[BombState] = Field(default_factory=list)
    explosions: Set[Tuple[int, int]] = Field(default_factory=set)  # coords affected by fire in current step
    explosion_origins: List[List[int]] = Field(default_factory=list)
    step_count: int = 0
