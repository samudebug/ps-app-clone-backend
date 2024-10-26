from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.domain.interfaces.friends_repository import IFriendsRepository
from psapp_clone_backend.features.check_friends.friend_entity import FriendEntity
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger


class CheckFriendsUseCase:
    repo: IFriendsRepository
    logger = get_logger(__name__)

    def __init__(self, repo: IFriendsRepository) -> None:
        self.repo = repo
    
    def execute(self) -> List[DataState[FriendEntity]]:
        friends = self.repo.get_friends()
        return [DataState(data=FriendEntity(**x)) for x in friends] 