from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.chats.domain.interfaces.chats_repository import IChatsRepository


class LeaveGroupChatUseCase:
    repo: IChatsRepository
    def __init__(self, repo: IChatsRepository) -> None:
        self.repo = repo
    
    def execute(self, chat_id: str):
        try:
            self.repo.leave_group_chat(chat_id)
        except Exception as e:
            return DataState(error=e)