from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger
from psapp_clone_backend.modules.chats.adapters.entities.chat_entity import ChatEntity
from psapp_clone_backend.modules.chats.domain.interfaces.chats_repository import IChatsRepository


class CheckChatsUseCase:
    repo: IChatsRepository
    logger = get_logger(__name__)

    def __init__(self, repo: IChatsRepository) -> None:
        self.repo = repo
    
    def execute(self) -> List[DataState[ChatEntity]]:
        chats = self.repo.get_chats()
        return [DataState(data=ChatEntity(**x)) for x in chats]