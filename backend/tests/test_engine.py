import pytest
from app.models import TileType, Action, BombState
from app.engine import SimulationEngine

def test_initialization():
    engine = SimulationEngine(width=15, height=13)
    assert engine.width == 15
    assert engine.height == 13
    assert engine.state.grid[0][0] == TileType.WALL
    assert engine.state.grid[1][1] == TileType.EMPTY
    # Pillar at 2, 2
    assert engine.state.grid[2][2] == TileType.WALL

def test_agent_movement():
    engine = SimulationEngine(width=15, height=13)
    # Spawn agent at (1, 1)
    assert engine.add_agent("player_1", 1, 1)
    
    # Move Right
    engine.step({"player_1": Action.RIGHT})
    assert engine.state.agents["player_1"].x == 2
    assert engine.state.agents["player_1"].y == 1

    # Move Left
    engine.step({"player_1": Action.LEFT})
    assert engine.state.agents["player_1"].x == 1
    assert engine.state.agents["player_1"].y == 1

    # Try moving into border wall (UP)
    engine.step({"player_1": Action.UP})
    assert engine.state.agents["player_1"].x == 1
    assert engine.state.agents["player_1"].y == 1  # Blocked

def test_movement_obstacles():
    engine = SimulationEngine(width=15, height=13)
    # Set a brick at (2, 1)
    engine.grid[1][2] = TileType.BRICK
    engine.state.grid[1][2] = TileType.BRICK
    
    engine.add_agent("player_1", 1, 1)
    
    # Move Right into BRICK
    engine.step({"player_1": Action.RIGHT})
    assert engine.state.agents["player_1"].x == 1
    assert engine.state.agents["player_1"].y == 1  # Blocked by brick

def test_movement_into_bomb():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_1", 1, 1)
    engine.add_agent("player_2", 3, 1)
    
    # player_2 places bomb at (3, 1)
    engine.step({"player_2": Action.PLACE_BOMB})
    assert engine.state.grid[1][3] == TileType.BOMB
    
    # player_1 tries to move Right into (3, 1)
    engine.step({"player_1": Action.RIGHT, "player_2": Action.RIGHT})
    # player_1 was at (1, 1), moved to (2, 1)
    assert engine.state.agents["player_1"].x == 2
    # player_1 now tries to move Right from (2, 1) into (3, 1) which has a bomb
    engine.step({"player_1": Action.RIGHT})
    assert engine.state.agents["player_1"].x == 2  # Blocked by bomb

def test_move_out_of_placed_bomb():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_1", 1, 1)
    
    # Place bomb
    engine.step({"player_1": Action.PLACE_BOMB})
    assert engine.state.grid[1][1] == TileType.BOMB
    
    # Move out to the right
    engine.step({"player_1": Action.RIGHT})
    assert engine.state.agents["player_1"].x == 2
    assert engine.state.agents["player_1"].y == 1
    # Bomb remains at (1, 1)
    assert engine.state.grid[1][1] == TileType.BOMB

def test_item_pickup_single():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_1", 1, 1)
    
    # Place Item Radius at (2, 1)
    engine.state.grid[1][2] = TileType.ITEM_RADIUS
    
    # Move player_1 onto the item
    engine.step({"player_1": Action.RIGHT})
    assert engine.state.agents["player_1"].x == 2
    # Item picked up and range increased from 1 to 2
    assert engine.state.agents["player_1"].bomb_range == 2
    assert engine.state.grid[1][2] == TileType.EMPTY

def test_item_pickup_conflict():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_1", 1, 1)
    engine.add_agent("player_2", 3, 1)
    
    # Place Item Capacity at (2, 1)
    engine.state.grid[1][2] = TileType.ITEM_CAPACITY
    
    # Move both players onto (2, 1)
    engine.step({"player_1": Action.RIGHT, "player_2": Action.LEFT})
    
    # Item should be destroyed, neither player gets it
    assert engine.state.grid[1][2] == TileType.EMPTY
    assert engine.state.agents["player_1"].max_bombs == 1
    assert engine.state.agents["player_2"].max_bombs == 1

def test_bomb_placement_conflict():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_0", 1, 1)
    engine.add_agent("player_1", 1, 1)
    
    # Give player_1 a larger bomb range
    engine.state.agents["player_1"].bomb_range = 2
    
    # Both place bomb at (1, 1)
    engine.step({"player_0": Action.PLACE_BOMB, "player_1": Action.PLACE_BOMB})
    
    # Check that exactly one bomb is placed at (1, 1)
    assert len(engine.state.bombs) == 1
    placed_bomb = engine.state.bombs[0]
    
    # Prioritizes player_1 because of larger radius (2 > 1)
    assert placed_bomb.owner_id == "player_1"
    assert placed_bomb.range == 2
    
    # Check capacity changes
    assert engine.state.agents["player_0"].bombs_left == 1  # unchanged
    assert engine.state.agents["player_1"].bombs_left == 0  # decremented

def test_bomb_placement_id_priority():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_2", 1, 1)
    engine.add_agent("player_1", 1, 1)
    
    # Both place bomb at (1, 1), they have same range (1)
    engine.step({"player_1": Action.PLACE_BOMB, "player_2": Action.PLACE_BOMB})
    
    # Prioritizes player_1 because alphabetically "player_1" < "player_2"
    placed_bomb = engine.state.bombs[0]
    assert placed_bomb.owner_id == "player_1"
    assert engine.state.agents["player_1"].bombs_left == 0
    assert engine.state.agents["player_2"].bombs_left == 1

def test_chain_reaction_detonation():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_1", 1, 1)
    engine.add_agent("player_2", 4, 1) # out of range initially
    
    # Manually place bomb A at (2, 1) with timer 1, range 2 (can reach (4, 1))
    engine.state.grid[1][2] = TileType.BOMB
    bomb_a = BombState(x=2, y=1, owner_id="player_1", timer=1, range=2)
    engine.state.bombs.append(bomb_a)
    
    # Manually place bomb B at (4, 1) with timer 5, range 2 (can reach (6, 1))
    engine.state.grid[1][4] = TileType.BOMB
    bomb_b = BombState(x=4, y=1, owner_id="player_2", timer=5, range=2)
    engine.state.bombs.append(bomb_b)
    
    # Step simulation. Bomb A will detonate naturally because timer becomes 0.
    # Bomb B is in bomb A's blast zone, so it must detonate immediately in the same step.
    engine.step({"player_1": Action.STOP, "player_2": Action.STOP})
    
    # Both bombs should have detonated
    assert len(engine.state.bombs) == 0
    
    # Fire should propagate from both:
    # A's fire: (2, 1), (1, 1), (3, 1), (4, 1), (2, 0), (2, 2)
    # B's fire: (4, 1), (3, 1), (5, 1), (6, 1), (4, 0), (4, 2)
    # (6, 1) should contain explosion because of B's range 2
    assert (6, 1) in engine.state.explosions
    assert engine.state.grid[1][6] == TileType.EXPLOSION

def test_agent_elimination():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_1", 1, 1)
    engine.add_agent("player_2", 3, 1)
    
    # player_1 places bomb at (1, 1)
    engine.step({"player_1": Action.PLACE_BOMB, "player_2": Action.STOP})
    
    # Wait for detonation (7 steps total, we already did 1 step of placement, so 6 more)
    for _ in range(6):
        engine.step({"player_1": Action.STOP, "player_2": Action.STOP})
        
    # Detonation happens on this step. player_1 is at (1, 1), in the explosion.
    # player_2 is at (3, 1), which is out of range 1 of the bomb at (1, 1).
    assert not engine.state.agents["player_1"].is_alive
    assert engine.state.agents["player_2"].is_alive

def test_destroyed_brick_drops_item():
    engine = SimulationEngine(width=15, height=13)
    # Place a brick at (2, 1)
    engine.state.grid[1][2] = TileType.BRICK
    engine.add_agent("player_1", 1, 1)
    
    # Place bomb at (1, 1)
    engine.step({"player_1": Action.PLACE_BOMB})
    
    # Fast forward bomb to explosion
    for _ in range(6):
        engine.step({"player_1": Action.STOP})
        
    # Check that the brick at (2, 1) was destroyed and replaced with an item or empty
    # Since drop rate is 60% (30% radius + 30% capacity), let's ensure it's not a brick anymore
    assert engine.state.grid[1][2] != TileType.BRICK

def test_agent_direction_and_explosion_origins():
    engine = SimulationEngine(width=15, height=13)
    engine.add_agent("player_1", 1, 1)
    
    # 1. Test movement direction update
    # Move RIGHT
    engine.step({"player_1": Action.RIGHT})
    assert engine.state.agents["player_1"].direction == "right"
    
    # Move UP
    engine.step({"player_1": Action.UP})
    assert engine.state.agents["player_1"].direction == "up"

    # Move LEFT
    engine.step({"player_1": Action.LEFT})
    assert engine.state.agents["player_1"].direction == "left"

    # Move DOWN
    engine.step({"player_1": Action.DOWN})
    assert engine.state.agents["player_1"].direction == "down"

    # 2. Test explosion_origins population
    bx, by = engine.state.agents["player_1"].x, engine.state.agents["player_1"].y
    engine.step({"player_1": Action.PLACE_BOMB})
    
    # Fast forward to explosion
    for _ in range(6):
        engine.step({"player_1": Action.STOP})
        
    # On detonation, the origin of detonation should be recorded in explosion_origins
    assert [bx, by] in engine.state.explosion_origins
