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

    def __init__(self, seed: Optional[int] = None, multi_agent: bool = False):
        """
        Initialize the environment.

        Args:
            seed (int, optional): Random seed for reproducibility.
            multi_agent (bool): Whether to enable 4-player multi-agent mode.
        """
        self.seed = seed
        self.multi_agent = multi_agent
        self.map: Optional[Map] = None
        self.player: Optional[Player] = None
        self.players: List[Player] = []
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
            dict: Initial state representation (or first player state if in multi-agent mode).
        """
        self.map = Map(seed=self.seed)
        self.current_step = 0
        self.bombs.clear()
        self.explosions.clear()
        self.items.clear()

        if self.multi_agent:
            self.enemies.clear()
            self.players.clear()
            for i, (px, py) in enumerate(self.map.spawns):
                self.players.append(Player(px, py, player_id=f"player_{i+1}"))
            self.player = self.players[0] if self.players else None
            return self.get_state_for_player(0)
        else:
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
            "bricks": list(self.map.bricks) if self.map else [],
            "items": {(x, y): item.item_type.value for (x, y), item in self.items.items()},
            "ammo": self.player.bombs_left if self.player else 0,
            "blast_radius": self.player.blast_radius if self.player else 0,
            "width": self.map.width if self.map else GameConfig.MAP_WIDTH,
            "height": self.map.height if self.map else GameConfig.MAP_HEIGHT,
            "time_remaining": max(0, self.max_steps - self.current_step)
        }

    def get_state_for_player(self, player_idx: int) -> dict:
        """
        Extract the environment state dictionary for a specific player.

        Args:
            player_idx (int): Index of the player (0 to 3).

        Returns:
            dict: State representation from the player's perspective.
        """
        player = self.players[player_idx]
        active_explosions = set()
        for exp in self.explosions:
            active_explosions.update(exp.tiles)

        return {
            "self_position": (player.x, player.y) if player.is_alive else (0, 0),
            "enemy_positions": [(p.x, p.y) for i, p in enumerate(self.players) if i != player_idx and p.is_alive],
            "bomb_positions": [(b.x, b.y, b.timer) for b in self.bombs],
            "explosions": list(active_explosions),
            "walls": list(self.map.walls) if self.map else [],
            "bricks": list(self.map.bricks) if self.map else [],
            "items": {(x, y): item.item_type.value for (x, y), item in self.items.items()},
            "ammo": player.bombs_left if player.is_alive else 0,
            "blast_radius": player.blast_radius if player.is_alive else 0,
            "width": self.map.width if self.map else GameConfig.MAP_WIDTH,
            "height": self.map.height if self.map else GameConfig.MAP_HEIGHT,
            "time_remaining": max(0, self.max_steps - self.current_step)
        }

    def is_done(self) -> bool:
        """
        Check if the game is over.

        Returns:
            bool: True if game has terminated, False otherwise.
        """
        if self.multi_agent:
            alive_count = sum(1 for p in self.players if p.is_alive)
            if alive_count <= 1:
                return True
            if self.current_step >= self.max_steps:
                return True
            return False

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

    def step_multi(self, actions: List[str]) -> Tuple[List[dict], List[float], bool, dict]:
        """
        Execute one step in multi-agent mode where all 4 agents act simultaneously.

        Args:
            actions (List[str]): Action strings for the 4 players.

        Returns:
            Tuple[List[dict], List[float], bool, dict]:
                - next_states: List of state dictionaries for all 4 players.
                - rewards: List of rewards for all 4 players.
                - done: Flag indicating game over.
                - info: Dictionary with auxiliary/game stats.
        """
        if self.is_done():
            next_states = [self.get_state_for_player(idx) for idx in range(len(self.players))]
            rewards = [0.0] * len(self.players)
            return next_states, rewards, True, {"msg": "Game already finished."}

        # Convert actions to Enum
        parsed_actions = []
        for i, act in enumerate(actions):
            if isinstance(act, str):
                try:
                    act = Action[act.upper()]
                except KeyError:
                    act = Action.WAIT
            parsed_actions.append(act)

        # Track events for rewards/stats
        bricks_destroyed_by = {p.id: 0 for p in self.players}
        kills_by = {p.id: 0 for p in self.players}
        items_collected_by = {p.id: 0 for p in self.players}
        player_damaged_this_turn = {p.id: False for p in self.players}

        # 1. Process player actions (movement and bomb placement)
        for i, player in enumerate(self.players):
            if not player.is_alive:
                continue

            action = parsed_actions[i]
            px, py = player.x, player.y

            # Movement
            nx, ny = px, py
            if action == Action.UP:
                ny = py - 1
            elif action == Action.DOWN:
                ny = py + 1
            elif action == Action.LEFT:
                nx = px - 1
            elif action == Action.RIGHT:
                nx = px + 1

            if action in [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]:
                if self.map.is_walkable(nx, ny):
                    bomb_on_tile = any(b.x == nx and b.y == ny for b in self.bombs)
                    if not bomb_on_tile:
                        player.move_to(nx, ny)

            # Bomb Placement
            if action == Action.BOMB:
                bomb_on_tile = any(b.x == px and b.y == py for b in self.bombs)
                if player.bombs_left > 0 and not bomb_on_tile:
                    new_bomb = Bomb(px, py, player.blast_radius, owner_id=player.id)
                    self.bombs.append(new_bomb)
                    player.bombs_left -= 1

        # 2. Update Bomb / Explosion timers
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
            explosion = Explosion(curr_bomb.x, curr_bomb.y, curr_bomb.blast_radius, curr_bomb.owner_id)

            dest_bricks, dest_items, chain_bombs = explosion.propagate(
                self.map.walls, self.map.bricks, bombs_dict, self.items
            )

            # Process brick destruction
            for bx, by in dest_bricks:
                if self.map.remove_brick(bx, by):
                    bricks_destroyed_by[curr_bomb.owner_id] = bricks_destroyed_by.get(curr_bomb.owner_id, 0) + 1
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

            # Restore player bomb capacity
            owner = next((p for p in self.players if p.id == curr_bomb.owner_id), None)
            if owner:
                owner.bombs_left = min(owner.max_bombs, owner.bombs_left + 1)

            self.explosions.append(explosion)

        # 3. Process Damage/Collisions
        explosion_tiles = set()
        for exp in self.explosions:
            explosion_tiles.update(exp.tiles)

        # Check player damage (only by explosions, no player-to-player touch damage)
        for player in self.players:
            if player.is_alive:
                if (player.x, player.y) in explosion_tiles:
                    player.lose_life()
                    player_damaged_this_turn[player.id] = True

                    # Award kill credit if the player was killed by someone else's bomb
                    if not player.is_alive:
                        for exp in self.explosions:
                            if (player.x, player.y) in exp.tiles:
                                if exp.owner_id != player.id:
                                    kills_by[exp.owner_id] = kills_by.get(exp.owner_id, 0) + 1
                                break

        # 4. Process Item Collection
        for player in self.players:
            if player.is_alive:
                pos = (player.x, player.y)
                if pos in self.items:
                    item = self.items[pos]
                    player.collect_item(item.item_type)
                    del self.items[pos]
                    items_collected_by[player.id] = items_collected_by.get(player.id, 0) + 1

        # 5. Calculate Rewards and Scores
        rewards = []
        for player in self.players:
            if not player.is_alive and not player_damaged_this_turn[player.id]:
                # Already dead and did not receive damage this turn
                rewards.append(0.0)
                continue

            r = 0.0
            pid = player.id

            bricks_count = bricks_destroyed_by.get(pid, 0)
            r += bricks_count * 10.0
            player.add_score(bricks_count * 10)

            kills_count = kills_by.get(pid, 0)
            r += kills_count * 100.0
            player.add_score(kills_count * 100)

            items_count = items_collected_by.get(pid, 0)
            r += items_count * 20.0

            if player_damaged_this_turn[pid]:
                r -= 200.0

            if player.is_alive:
                r -= 1.0  # Step penalty

            rewards.append(r)

        # Check if game is over
        done = self.is_done()
        if done:
            alive_players = [p for p in self.players if p.is_alive]
            if len(alive_players) == 1:
                winner = alive_players[0]
                winner_idx = self.players.index(winner)
                rewards[winner_idx] += 500.0
                winner.add_score(500)

        # Update next states
        next_states = [self.get_state_for_player(idx) for idx in range(len(self.players))]

        info = {
            "alive_players": [p.id for p in self.players if p.is_alive],
            "scores": {p.id: p.score for p in self.players},
            "lives": {p.id: p.lives for p in self.players}
        }

        return next_states, rewards, done, info

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

        # 5. Fill players / enemies
        if self.multi_agent:
            for i, p in enumerate(self.players):
                # Represent player as their index 1-4, or X if dead
                if p.is_alive:
                    grid[p.y][p.x] = str(i + 1)
                elif grid[p.y][p.x] not in ["1", "2", "3", "4"]:
                    grid[p.y][p.x] = "X"
        else:
            for e in self.enemies:
                if e.is_alive:
                    grid[e.y][e.x] = "E"
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
        if self.multi_agent:
            p_infos = []
            for i, p in enumerate(self.players):
                status = "ALIVE" if p.is_alive else "DEAD"
                p_infos.append(f"P{i+1}: {status} (L:{p.lives} S:{p.score} A:{p.bombs_left}/{p.max_bombs})")
            print(f"Step: {self.current_step}/{self.max_steps}")
            print(" | ".join(p_infos))
        else:
            if self.player:
                print(f"Step: {self.current_step}/{self.max_steps} | Lives: {self.player.lives} | "
                      f"Score: {self.player.score} | Ammo: {self.player.bombs_left}/{self.player.max_bombs} | "
                      f"Blast: {self.player.blast_radius}")
        print()
