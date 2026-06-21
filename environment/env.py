"""Environment definition for Bomberman simulation."""
from enum import Enum
from typing import Dict, List, Tuple, Set, Optional
import numpy as np

from configs.default_config import GameConfig
from environment.map import Map
from environment.player import Player
from environment.enemy import Enemy
from environment.bomb import Bomb
from environment.explosion import Explosion
from environment.item import Item, ItemType

class Action(Enum):
    """Action space for the agent."""
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    BOMB = "BOMB"
    WAIT = "WAIT"

class Environment:
    """The Bomberman environment matching gym-like interface."""

    def __init__(self, seed: Optional[int] = None):
        """
        Initialize the environment.

        Args:
            seed (int, optional): Random seed for reproducibility.
        """
        self.seed = seed
        self.map: Optional[Map] = None
        self.player: Optional[Player] = None
        self.enemies: List[Enemy] = []
        self.bombs: List[Bomb] = []
        self.explosions: List[Explosion] = []
        self.items: Dict[Tuple[int, int], Item] = {}
        self.current_step = 0
        self.max_steps = GameConfig.MAX_STEPS
        
        self.reset()

    def reset(self) -> dict:
        """
        Reset the game state to initial configuration.

        Returns:
            dict: Initial state representation.
        """
        self.map = Map(seed=self.seed)
        self.current_step = 0
        self.bombs.clear()
        self.explosions.clear()
        self.items.clear()

        # Spawn player in the first spawn point (top-left)
        player_spawn = self.map.spawns[0]
        self.player = Player(player_spawn[0], player_spawn[1])

        # Spawn enemies in the remaining spawn points (corners)
        self.enemies.clear()
        enemy_spawns = self.map.spawns[1:1 + GameConfig.INITIAL_ENEMY_COUNT]
        for i, (ex, ey) in enumerate(enemy_spawns):
            self.enemies.append(Enemy(f"enemy_{i+1}", ex, ey))

        return self.get_state()

    def get_state(self) -> dict:
        """
        Extract the environment state dictionary for the agent.

        Returns:
            dict: State representation.
        """
        # Collect all active explosion tiles
        active_explosions = set()
        for exp in self.explosions:
            active_explosions.update(exp.tiles)

        return {
            "self_position": (self.player.x, self.player.y) if self.player else (0, 0),
            "enemy_positions": [(e.x, e.y) for e in self.enemies if e.is_alive],
            "bomb_positions": [(b.x, b.y, b.timer) for b in self.bombs],
            "explosions": list(active_explosions),
            "walls": list(self.map.walls) if self.map else [],
            "items": {(x, y): item.item_type.value for (x, y), item in self.items.items()},
            "ammo": self.player.bombs_left if self.player else 0,
            "blast_radius": self.player.blast_radius if self.player else 0,
            "time_remaining": max(0, self.max_steps - self.current_step)
        }

    def is_done(self) -> bool:
        """
        Check if the game is over.

        Returns:
            bool: True if game has terminated, False otherwise.
        """
        if self.player is not None and not self.player.is_alive:
            return True
        if all(not e.is_alive for e in self.enemies):
            return True
        if self.current_step >= self.max_steps:
            return True
        return False

    def step(self, action) -> Tuple[dict, float, bool, dict]:
        """
        Execute one step in the environment.

        Args:
            action (Action or str): The action to execute.

        Returns:
            Tuple[dict, float, bool, dict]:
                - next_state: State dictionary.
                - reward: Floating point scalar reward.
                - done: Flag indicating termination.
                - info: Debug/auxiliary information dictionary.
        """
        # Convert string actions to Enum
        if isinstance(action, str):
            try:
                action = Action[action.upper()]
            except KeyError:
                action = Action.WAIT

        if self.is_done():
            return self.get_state(), 0.0, True, {"msg": "Game already finished."}

        # Track events for rewards
        reward = 0.0
        bricks_destroyed_count = 0
        enemies_killed_count = 0
        items_collected_count = 0
        player_damaged = False

        # 1. Process player action
        if self.player.is_alive:
            px, py = self.player.x, self.player.y
            if action == Action.UP:
                nx, ny = px, py - 1
            elif action == Action.DOWN:
                nx, ny = px, py + 1
            elif action == Action.LEFT:
                nx, ny = px - 1, py
            elif action == Action.RIGHT:
                nx, ny = px + 1, py
            else:
                nx, ny = px, py

            # Check if movement target is valid
            # Cannot walk into walls or bricks
            if action in [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]:
                if self.map.is_walkable(nx, ny):
                    # Also cannot walk into a bomb (unless self-placed, but here we block all bomb walks)
                    bomb_on_tile = any(b.x == nx and b.y == ny for b in self.bombs)
                    if not bomb_on_tile:
                        self.player.move_to(nx, ny)

            # Process Bomb Placement
            if action == Action.BOMB:
                # Agent has ammo and no bomb is already on the tile
                bomb_on_tile = any(b.x == px and b.y == py for b in self.bombs)
                if self.player.bombs_left > 0 and not bomb_on_tile:
                    new_bomb = Bomb(px, py, self.player.blast_radius, owner_id=self.player.id)
                    self.bombs.append(new_bomb)
                    self.player.bombs_left -= 1

        # 2. Process Enemy actions
        walkable_cells = self.map.get_walkable_cells()
        # Remove cells currently occupied by bombs from walkable spaces for enemies
        bomb_coords = {(b.x, b.y) for b in self.bombs}
        enemy_walkable = walkable_cells - bomb_coords

        for enemy in self.enemies:
            if enemy.is_alive:
                next_pos = enemy.choose_move(enemy_walkable)
                enemy.move_to(next_pos[0], next_pos[1])

        # 3. Update Bomb / Explosion timers
        self.current_step += 1

        # Tick explosions and remove expired ones
        self.explosions = [exp for exp in self.explosions if not exp.tick()]

        # Tick bombs and find exploded ones
        bombed_this_turn = []
        remaining_bombs = []
        for bomb in self.bombs:
            if bomb.tick():
                bombed_this_turn.append(bomb)
            else:
                remaining_bombs.append(bomb)
        self.bombs = remaining_bombs

        # Resolve explosions (including chain reactions)
        bombs_dict = {(b.x, b.y): b for b in self.bombs + bombed_this_turn}
        
        while bombed_this_turn:
            curr_bomb = bombed_this_turn.pop(0)
            # Instantiate the explosion object
            explosion = Explosion(curr_bomb.x, curr_bomb.y, curr_bomb.blast_radius, curr_bomb.owner_id)
            
            # Propagate and get triggers
            dest_bricks, dest_items, chain_bombs = explosion.propagate(
                self.map.walls, self.map.bricks, bombs_dict, self.items
            )
            
            # Process brick destruction and potential item spawn
            for bx, by in dest_bricks:
                if self.map.remove_brick(bx, by):
                    bricks_destroyed_count += 1
                    # Spawn item with probability
                    if np.random.rand() < GameConfig.ITEM_SPAWN_CHANCE:
                        itype = np.random.choice([ItemType.BOMB_RANGE, ItemType.BOMB_CAPACITY])
                        self.items[(bx, by)] = Item(bx, by, itype)

            # Process items destroyed by explosion
            for ix, iy in dest_items:
                if (ix, iy) in self.items:
                    del self.items[(ix, iy)]

            # Chain reaction: trigger other bombs to explode this tick
            for cb_coords in chain_bombs:
                if cb_coords in bombs_dict:
                    cb = bombs_dict[cb_coords]
                    if cb in self.bombs:
                        self.bombs.remove(cb)
                        bombed_this_turn.append(cb)
                    elif cb in bombed_this_turn:
                        # Already in list to process
                        pass

            # Restore player bomb capacity
            if curr_bomb.owner_id == self.player.id:
                self.player.bombs_left = min(self.player.max_bombs, self.player.bombs_left + 1)

            # Save the explosion to environment
            self.explosions.append(explosion)

        # 4. Process Damage/Collisions
        # Collect all current explosion tiles
        explosion_tiles = set()
        for exp in self.explosions:
            explosion_tiles.update(exp.tiles)

        # Check player damage (explosions or touching enemies)
        if self.player.is_alive:
            # Check explosion
            in_explosion = (self.player.x, self.player.y) in explosion_tiles
            # Check enemy touch
            touched_enemy = any(e.is_alive and e.x == self.player.x and e.y == self.player.y for e in self.enemies)
            
            if in_explosion or touched_enemy:
                self.player.lose_life()
                player_damaged = True

        # Check enemy damage
        for enemy in self.enemies:
            if enemy.is_alive:
                if (enemy.x, enemy.y) in explosion_tiles:
                    enemy.lose_life()
                    enemies_killed_count += 1

        # 5. Process Item Collection
        if self.player.is_alive:
            pos = (self.player.x, self.player.y)
            if pos in self.items:
                item = self.items[pos]
                self.player.collect_item(item.item_type)
                del self.items[pos]
                items_collected_count += 1

        # 6. Calculate Rewards and Scores
        # Scores are recorded inside player object, but let's shape step rewards for AI
        reward += bricks_destroyed_count * 10.0
        reward += enemies_killed_count * 100.0
        reward += items_collected_count * 20.0
        
        if player_damaged:
            reward -= 200.0
        else:
            reward -= 1.0  # Time step penalty to encourage speed

        # Additional victory/loss rewards
        if self.player.is_alive and all(not e.is_alive for e in self.enemies):
            reward += 500.0  # Victory bonus
            self.player.add_score(500)
            
        if bricks_destroyed_count > 0:
            self.player.add_score(bricks_destroyed_count * 10)
        if enemies_killed_count > 0:
            self.player.add_score(enemies_killed_count * 100)

        # Check termination
        done = self.is_done()

        # Update next state
        next_state = self.get_state()
        
        info = {
            "bricks_destroyed": bricks_destroyed_count,
            "enemies_killed": enemies_killed_count,
            "items_collected": items_collected_count,
            "player_lives": self.player.lives,
            "player_score": self.player.score,
            "game_won": all(not e.is_alive for e in self.enemies) if not self.player.is_alive or done else False
        }

        return next_state, reward, done, info

    def render(self) -> None:
        """Render the environment state in ASCII format."""
        if not self.map:
            return

        w, h = self.map.width, self.map.height
        grid = [[" " for _ in range(w)] for _ in range(h)]

        # 1. Fill walkables and walls/bricks
        for y in range(h):
            for x in range(w):
                if (x, y) in self.map.walls:
                    grid[y][x] = "#"
                elif (x, y) in self.map.bricks:
                    grid[y][x] = "B"
                else:
                    grid[y][x] = "."

        # 2. Fill items
        for (ix, iy), item in self.items.items():
            if item.item_type == ItemType.BOMB_RANGE:
                grid[iy][ix] = "R"
            elif item.item_type == ItemType.BOMB_CAPACITY:
                grid[iy][ix] = "C"

        # 3. Fill explosions
        for exp in self.explosions:
            for ex, ey in exp.tiles:
                if self.map.is_in_bounds(ex, ey) and (ex, ey) not in self.map.walls:
                    grid[ey][ex] = "*"

        # 4. Fill bombs
        for bomb in self.bombs:
            grid[bomb.y][bomb.x] = "O"

        # 5. Fill enemies
        for e in self.enemies:
            if e.is_alive:
                grid[e.y][e.x] = "E"

        # 6. Fill player
        if self.player and self.player.is_alive:
            grid[self.player.y][self.player.x] = "P"
        elif self.player:
            grid[self.player.y][self.player.x] = "X"

        # Output the board
        border = "-" * (w * 2 + 3)
        print(border)
        for row in grid:
            print("| " + " ".join(row) + " |")
        print(border)
        
        # Metadata
        if self.player:
            print(f"Step: {self.current_step}/{self.max_steps} | Lives: {self.player.lives} | "
                  f"Score: {self.player.score} | Ammo: {self.player.bombs_left}/{self.player.max_bombs} | "
                  f"Blast: {self.player.blast_radius}")
        print()
