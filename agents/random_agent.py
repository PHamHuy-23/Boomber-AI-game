"""
Agent chọn hành động ngẫu nhiên cho game Bomberman.
"""
import random
from agents import BaseAgent
from environment.env import Action

class RandomAgent(BaseAgent):
    """
    Agent này chọn hành động hoàn toàn ngẫu nhiên ở mỗi lượt di chuyển.
    Không có tính toán, không tìm kiếm đường đi hay né bom.
    """

    def __init__(self, seed: int = None):
        """
        Khởi tạo RandomAgent.

        Args:
            seed (int, optional): Hạt giống ngẫu nhiên để tái lập kết quả thử nghiệm.
        """
        if seed is not None:
            random.seed(seed)

    def choose_action(self, state: dict) -> str:
        """
        Chọn một hành động ngẫu nhiên từ không gian hành động có sẵn.

        Args:
            state (dict): Trạng thái game hiện tại.

        Returns:
            str: Chuỗi hành động được chọn ngẫu nhiên ('UP', 'DOWN', 'LEFT', 'RIGHT', 'BOMB', 'WAIT').
        """
        # Chọn ngẫu nhiên một trong các hành động khả thi từ Enum Action
        action = random.choice(list(Action))
        return action.value
