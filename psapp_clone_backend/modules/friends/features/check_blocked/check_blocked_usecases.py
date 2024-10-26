from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.friends.adapters.entities.friend_entity import FriendEntity
from psapp_clone_backend.modules.friends.domain.interfaces.friends_repository import IFriendsRepository


class CheckBlockedUseCase:
    repo: IFriendsRepository

    def __init__(self, repo: IFriendsRepository) -> None:
        self.repo = repo
    
    def execute(self) -> List[DataState[FriendEntity]]:
        blocked = self.repo.get_blocked()
        return [DataState(data=FriendEntity(**x)) for x in blocked]