from abc import ABC, abstractmethod
from typing import List

from psapp_clone_backend.modules.friends.adapters.entities.friend_entity import FriendEntity


class IFriendsRepository(ABC):
    @abstractmethod
    def get_friends(self) -> List[FriendEntity]:
        pass

    @abstractmethod
    def get_blocked(self) -> List[FriendEntity]:
        pass