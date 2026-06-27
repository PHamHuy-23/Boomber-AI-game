import random
from typing import Dict, List, Set, Tuple, Optional, Any
from app.models import GameState, AgentState, BombState, TileType, Action

class SimulationEngine:
    def __init__(self, width: int = 15, height: int = 13, grid: Optional[List[List[int]]] = None, tracker: Optional[Any] = None):
        self.width = width
        self.height = height
        self.tracker = tracker
        
        if grid is not None:
            # Deep copy the grid to avoid side effects
            self.grid = [row[:] for row in grid]
            self.height = len(self.grid)
            self.width = len(self.grid[0]) if self.height > 0 else 0
        else:
            self.grid = self._generate_default_grid()
            
        self.state = GameState(
            width=self.width,
            height=self.height,
            grid=self.grid,
            agents={},
            bombs=[],
            explosions=set(),
            step_count=0
        )

    def _generate_default_grid(self) -> List[List[int]]:
        grid = [[TileType.EMPTY for _ in range(self.width)] for _ in range(self.height)]
        
        # Define spawn locations (to protect their neighborhoods)
        spawns = [
            (1, 1),
            (self.width - 2, 1),
            (1, self.height - 2),
            (self.width - 2, self.height - 2)
        ]
        spawn_protection = set()
        for sx, sy in spawns:
            spawn_protection.add((sx, sy))
            spawn_protection.add((sx + 1, sy))
            spawn_protection.add((sx - 1, sy))
            spawn_protection.add((sx, sy + 1))
            spawn_protection.add((sx, sy - 1))
            
        # 1. Place border walls and pillars
        for y in range(self.height):
            for x in range(self.width):
                if y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1:
                    grid[y][x] = TileType.WALL
                elif y % 2 == 0 and x % 2 == 0:
                    grid[y][x] = TileType.WALL
                    
        # 2. Collect all grass cells eligible for bricks
        eligible_cells = []
        for y in range(self.height):
            for x in range(self.width):
                is_border_or_pillar = (y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1) or (y % 2 == 0 and x % 2 == 0)
                if not is_border_or_pillar and (x, y) not in spawn_protection:
                    eligible_cells.append((x, y))
                    
        # 3. Deterministically place bricks on 40% of the grass cells using seed 42
        r = random.Random(42)
        r.shuffle(eligible_cells)
        target_bricks = int(len(eligible_cells) * 0.40)
        
        for i in range(target_bricks):
            bx, by = eligible_cells[i]
            grid[by][bx] = TileType.BRICK
            
        return grid

    def add_agent(self, agent_id: str, x: int, y: int, lives: int = 1) -> bool:
        """
        Spawns an agent at the specified coordinates.
        """
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        if self.state.grid[y][x] in (TileType.WALL, TileType.BRICK):
            return False
        
        self.state.agents[agent_id] = AgentState(
            id=agent_id,
            x=x,
            y=y,
            lives=lives,
            max_bombs=1,
            bomb_range=1,
            bombs_left=1,
            is_alive=True,
            direction="down"
        )
        return True

    def step(self, actions: Dict[str, int]) -> bool:
        """
        Executes one step of the simulation.
        Returns True if game continues, False if game is over.
        """
        # 0. Clear previous step's explosions from the grid
        for y in range(self.height):
            for x in range(self.width):
                if self.state.grid[y][x] == TileType.EXPLOSION:
                    self.state.grid[y][x] = TileType.EMPTY
        self.state.explosions.clear()
        self.state.explosion_origins.clear()

        # Increment step count
        self.state.step_count += 1

        # 1. Collect Actions (Only for alive agents)
        valid_actions = {}
        for agent_id, agent in self.state.agents.items():
            if agent.is_alive:
                # Default to STOP if no action provided or action is invalid
                act_val = actions.get(agent_id, Action.STOP)
                if act_val not in Action.__members__.values():
                    act_val = Action.STOP
                valid_actions[agent_id] = act_val

        # 2. Process Movement
        # Compute next positions
        next_positions = {}
        for agent_id, act in valid_actions.items():
            agent = self.state.agents[agent_id]
            nx, ny = agent.x, agent.y
            if act == Action.LEFT:
                nx -= 1
                agent.direction = "left"
            elif act == Action.RIGHT:
                nx += 1
                agent.direction = "right"
            elif act == Action.UP:
                ny -= 1
                agent.direction = "up"
            elif act == Action.DOWN:
                ny += 1
                agent.direction = "down"

            # Validate target coordinates
            if 0 <= nx < self.width and 0 <= ny < self.height:
                target_tile = self.state.grid[ny][nx]
                # Cannot walk into WALL or BRICK
                if target_tile in (TileType.WALL, TileType.BRICK):
                    nx, ny = agent.x, agent.y
                # Cannot walk into a BOMB from previous steps
                # Note: any bomb currently in self.state.bombs was placed in a previous step
                elif target_tile == TileType.BOMB:
                    nx, ny = agent.x, agent.y
            else:
                nx, ny = agent.x, agent.y

            next_positions[agent_id] = (nx, ny)

        # Update positions
        for agent_id, (nx, ny) in next_positions.items():
            agent = self.state.agents[agent_id]
            agent.x = nx
            agent.y = ny

        # Resolve Item Pickup
        for y in range(self.height):
            for x in range(self.width):
                tile = self.state.grid[y][x]
                if tile in (TileType.ITEM_RADIUS, TileType.ITEM_CAPACITY):
                    # Find alive agents on this tile
                    agents_on_tile = [
                        a for a in self.state.agents.values()
                        if a.is_alive and a.x == x and a.y == y
                    ]
                    if len(agents_on_tile) == 1:
                        # Exactly one agent gets the item
                        collector = agents_on_tile[0]
                        if tile == TileType.ITEM_RADIUS:
                            collector.bomb_range = min(5, collector.bomb_range + 1)
                        elif tile == TileType.ITEM_CAPACITY:
                            collector.max_bombs = min(5, collector.max_bombs + 1)
                            # Increment bombs_left as capacity increased
                            collector.bombs_left = min(collector.max_bombs, collector.bombs_left + 1)
                        self.state.grid[y][x] = TileType.EMPTY
                        if self.tracker:
                            self.tracker.record_item_pickup(collector.id)
                    elif len(agents_on_tile) >= 2:
                        # Destroyed, no one gets it
                        self.state.grid[y][x] = TileType.EMPTY

        # 3. Place Bomb
        bomb_requests = {}  # (x, y) -> list of (agent_id, bomb_range)
        for agent_id, act in valid_actions.items():
            if act == Action.PLACE_BOMB:
                agent = self.state.agents[agent_id]
                x, y = agent.x, agent.y
                # Check: agent has bombs left, and there is no bomb on the tile from previous steps
                if agent.bombs_left > 0 and self.state.grid[y][x] != TileType.BOMB:
                    if (x, y) not in bomb_requests:
                        bomb_requests[(x, y)] = []
                    bomb_requests[(x, y)].append((agent_id, agent.bomb_range))

        # Handle duplicate bomb placements
        for (x, y), requests in bomb_requests.items():
            # Sort by bomb_range descending, then agent_id ascending (alphabetical)
            # Since Python sorts are stable and sort comparisons are tuple-based, we negate bomb_range for descending order
            requests.sort(key=lambda item: (-item[1], item[0]))
            selected_agent_id, selected_range = requests[0]
            
            # Place the bomb
            selected_agent = self.state.agents[selected_agent_id]
            selected_agent.bombs_left -= 1
            
            new_bomb = BombState(
                x=x,
                y=y,
                owner_id=selected_agent_id,
                timer=7,
                range=selected_range
            )
            self.state.bombs.append(new_bomb)
            self.state.grid[y][x] = TileType.BOMB

        # 4. Decrease Bomb Timer
        for bomb in self.state.bombs:
            bomb.timer -= 1

        # 5. Resolve Explosion
        detonated_bombs = []
        exploded_tiles = set()
        destroyed_bricks = set()
        explosions_owners = {}
        
        # Queue-based chain explosion
        detonation_queue = [b for b in self.state.bombs if b.timer <= 0]
        queued_bombs_coords = {(b.x, b.y) for b in detonation_queue}
        
        while detonation_queue:
            bomb = detonation_queue.pop(0)
            if bomb in detonated_bombs:
                continue
            detonated_bombs.append(bomb)
            exploded_tiles.add((bomb.x, bomb.y))
            explosions_owners[(bomb.x, bomb.y)] = bomb.owner_id
            
            # Propagate explosion in 4 directions
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dx, dy in directions:
                for d in range(1, bomb.range + 1):
                    tx, ty = bomb.x + dx * d, bomb.y + dy * d
                    # Out of bounds check
                    if not (0 <= tx < self.width and 0 <= ty < self.height):
                        break
                    
                    tile = self.state.grid[ty][tx]
                    
                    if tile == TileType.WALL:
                        # Blocked completely
                        break
                    elif tile == TileType.BRICK:
                        # Blocked and destroyed
                        exploded_tiles.add((tx, ty))
                        destroyed_bricks.add((tx, ty))
                        explosions_owners[(tx, ty)] = bomb.owner_id
                        break
                    elif tile == TileType.BOMB:
                        # Add the bomb at (tx, ty) to detonation queue if not already queued
                        exploded_tiles.add((tx, ty))
                        explosions_owners[(tx, ty)] = bomb.owner_id
                        other_bomb = next((b for b in self.state.bombs if b.x == tx and b.y == ty), None)
                        if other_bomb and other_bomb not in detonated_bombs and (tx, ty) not in queued_bombs_coords:
                            detonation_queue.append(other_bomb)
                            queued_bombs_coords.add((tx, ty))
                        # Note: a bomb does not block the explosion from propagating further
                    else:
                        # Empty, Item, or existing Explosion
                        exploded_tiles.add((tx, ty))
                        explosions_owners[(tx, ty)] = bomb.owner_id

        # Remove detonated bombs and restore capacity
        for bomb in detonated_bombs:
            self.state.bombs.remove(bomb)
            owner = self.state.agents.get(bomb.owner_id)
            if owner:
                owner.bombs_left = min(owner.max_bombs, owner.bombs_left + 1)
            # Remove BOMB type from grid (will be set to EXPLOSION)
            self.state.grid[bomb.y][bomb.x] = TileType.EMPTY

        # Record brick destructions
        if self.tracker:
            for bx, by in destroyed_bricks:
                killer_id = explosions_owners.get((bx, by))
                if killer_id:
                    self.tracker.record_brick_destroyed(killer_id)

        # Clear destroyed bricks on grid
        for bx, by in destroyed_bricks:
            self.state.grid[by][bx] = TileType.EMPTY

        # Apply explosion fire to grid
        self.state.explosions = exploded_tiles
        self.state.explosion_origins = [[b.x, b.y] for b in detonated_bombs]
        for ex, ey in exploded_tiles:
            self.state.grid[ey][ex] = TileType.EXPLOSION

        # 6. Eliminate Agent
        for agent in self.state.agents.values():
            if agent.is_alive and (agent.x, agent.y) in self.state.explosions:
                agent.lives -= 1
                if agent.lives <= 0:
                    agent.is_alive = False
                    if self.tracker:
                        killer_id = explosions_owners.get((agent.x, agent.y))
                        self.tracker.record_death(agent.id, killer_id, self.state.step_count)

        # 7. Spawn Items
        # Spawn from destroyed bricks
        for bx, by in destroyed_bricks:
            # Determine item drop
            roll = random.random()
            if roll < 0.3:
                self.state.grid[by][bx] = TileType.ITEM_RADIUS
            elif roll < 0.6:
                self.state.grid[by][bx] = TileType.ITEM_CAPACITY
            # Else 40% chance of nothing (remain EMPTY)

        # Auto-spawn on grass tiles
        p_auto_spawn = 0.0003 * (self.state.step_count / 165.0)
        for y in range(self.height):
            for x in range(self.width):
                # Grass tile is TileType.EMPTY (no walls, bricks, bombs, items, explosions)
                if self.state.grid[y][x] == TileType.EMPTY:
                    # Check if an agent is standing here (so we don't spawn right under an agent)
                    agent_here = any(a.is_alive and a.x == x and a.y == y for a in self.state.agents.values())
                    if not agent_here:
                        if random.random() < p_auto_spawn:
                            self.state.grid[y][x] = TileType.ITEM_RADIUS if random.random() < 0.5 else TileType.ITEM_CAPACITY

        # 8. Check Game Over
        alive_count = sum(1 for a in self.state.agents.values() if a.is_alive)
        if alive_count <= 1 or self.state.step_count >= 300:
            return False

        return True

    def get_state(self) -> GameState:
        return self.state
