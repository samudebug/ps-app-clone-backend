from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.chats.adapters.entities.chat_entity import ChatEntity
from psapp_clone_backend.modules.chats.domain.interfaces.chats_repository import IChatsRepository


class CreateGroupChatUseCase:
    repo: IChatsRepository
    def __init__(self, repo: IChatsRepository) -> None:
        self.repo = repo
    

    def execute(self, user_ids: List[str]) -> DataState[ChatEntity]:
        try:
            new_group = self.repo.create_group_chat(user_ids)
            return DataState(data=new_group)
        except Exception as e:
            return DataState(error=e)