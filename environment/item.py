"""Item / Power-up definitions for Bomberman."""
from enum import Enum

class ItemType(Enum):
    """Types of items that players can pick up."""
    BOMB_RANGE = "BOMB_RANGE"        # Increases player's bomb blast radius
    BOMB_CAPACITY = "BOMB_CAPACITY"  # Increases player's max simultaneous bombs

class Item:
    """Represents an item placed on the grid."""

    def __init__(self, x: int, y: int, item_type: ItemType):
        """
        Initialize an item.

        Args:
            x (int): x-coordinate of the item.
            y (int): y-coordinate of the item.
            item_type (ItemType): Type of the item.
        """
        self.x = x
        self.y = y
        self.item_type = item_type

    def to_dict(self) -> dict:
        """Serialize item details to a dictionary."""
        return {
            "x": self.x,
            "y": self.y,
            "type": self.item_type.value
        }
