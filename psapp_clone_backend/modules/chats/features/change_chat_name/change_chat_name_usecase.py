from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.chats.domain.interfaces.chats_repository import IChatsRepository


class ChangeChatNameUseCase:
    repo: IChatsRepository
    def __init__(self, repo: IChatsRepository) -> None:
        self.repo = repo
    
    def execute(self, chat_id: str, name: str):
        try:
            self.repo.change_conversation_name(chat_id, name)
        except Exception as e:
            return DataState(error=e)