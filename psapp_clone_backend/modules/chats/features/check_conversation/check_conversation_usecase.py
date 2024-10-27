from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.chats.adapters.entities.message_entity import MessageEntity
from psapp_clone_backend.modules.chats.domain.interfaces.chats_repository import IChatsRepository


class CheckConversationUseCase:
    repo: IChatsRepository
    
    def __init__(self, repo: IChatsRepository) -> None:
        self.repo = repo
    
    def execute(self, chat_id: str, limit: int) -> DataState[List[MessageEntity]]:
        try:
            conversations = self.repo.get_conversation_for_chat(chat_id, limit)
            return DataState(data=conversations)
        except Exception as e:
            return DataState(error=e)