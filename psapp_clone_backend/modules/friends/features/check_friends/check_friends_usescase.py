from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.friends.adapters.entities.friend_entity import FriendEntity
from psapp_clone_backend.modules.friends.domain.interfaces.friends_repository import IFriendsRepository
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger


class CheckFriendsUseCase:
    repo: IFriendsRepository
    logger = get_logger(__name__)

    def __init__(self, repo: IFriendsRepository) -> None:
        self.repo = repo
    
    def execute(self) -> DataState[List[FriendEntity]]:
        try:
            friends = self.repo.get_friends()
            return DataState(data=friends)
        except Exception as e:
            self.logger.error(e)
            return DataState(error=e)