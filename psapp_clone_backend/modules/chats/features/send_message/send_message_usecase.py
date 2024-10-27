from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.chats.domain.interfaces.chats_repository import IChatsRepository


class SendMessageUseCase:
    repo: IChatsRepository
    def __init__(self, repo: IChatsRepository) -> None:
        self.repo = repo
    
    def execute(self, chat_id: str, message: str):
        try:
            self.repo.send_message(chat_id, message)
        except Exception as e:
            return DataState(error=e)