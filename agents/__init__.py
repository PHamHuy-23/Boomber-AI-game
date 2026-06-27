"""
Package Agents chứa lớp cơ sở BaseAgent và các lớp cài đặt cụ thể của nó.
"""
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Lớp cơ sở trừu tượng (Abstract Base Class) cho tất cả các agent Bomberman.
    """

    @abstractmethod
    def choose_action(self, state: dict) -> str:
        """
        Chọn một hành động từ không gian hành động dựa trên trạng thái game hiện tại.

        Args:
            state (dict): Từ điển biểu diễn trạng thái môi trường hiện tại.

        Returns:
            str: Chuỗi hành động được chọn ('UP', 'DOWN', 'LEFT', 'RIGHT', 'BOMB', 'WAIT').
        """
        pass
