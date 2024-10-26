from abc import ABC, abstractmethod
from typing import List


class IFriendsRepository(ABC):
    @abstractmethod
    def get_friends(self) -> List[dict]:
        pass

    @abstractmethod
    def get_blocked(self) -> List[dict]:
        pass