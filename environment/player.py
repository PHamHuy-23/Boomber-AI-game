"""Player definition for Bomberman."""
from configs.default_config import GameConfig

class Player:
    """Represents the main agent (player) controlled by the AI or keyboard."""

    def __init__(self, x: int, y: int, player_id: str = "player"):
        """
        Initialize the player.

        Args:
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
            player_id (str): Unique identifier for the player.
        """
        self.id = player_id
        self.x = x
        self.y = y
        self.lives = GameConfig.INITIAL_LIVES
        self.max_bombs = GameConfig.INITIAL_MAX_BOMBS
        self.bombs_left = GameConfig.INITIAL_MAX_BOMBS
        self.blast_radius = GameConfig.INITIAL_BLAST_RADIUS
        self.score = 0
        self.is_alive = True

    def move_to(self, x: int, y: int) -> None:
        """Update player position."""
        self.x = x
        self.y = y

    def lose_life(self) -> None:
        """Inflict damage, decreasing lives by 1, and mark dead if lives <= 0."""
        if self.is_alive:
            self.lives -= 1
            if self.lives <= 0:
                self.is_alive = False

    def collect_item(self, item_type) -> None:
        """
        Apply item power-up effects to player.
        
        Args:
            item_type (ItemType): The type of item collected.
        """
        from environment.item import ItemType
        if item_type == ItemType.BOMB_RANGE:
            self.blast_radius += 1
        elif item_type == ItemType.BOMB_CAPACITY:
            self.max_bombs += 1
            self.bombs_left += 1
        self.score += 50

    def add_score(self, amount: int) -> None:
        """Add points to the player's score."""
        self.score += amount

    def to_dict(self) -> dict:
        """Serialize player details to a dictionary."""
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "lives": self.lives,
            "max_bombs": self.max_bombs,
            "bombs_left": self.bombs_left,
            "blast_radius": self.blast_radius,
            "score": self.score,
            "is_alive": self.is_alive
        }
