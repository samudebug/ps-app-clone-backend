from abc import ABC, abstractmethod
from typing import List

from psapp_clone_backend.modules.chats.adapters.entities.chat_entity import ChatEntity
from psapp_clone_backend.modules.chats.adapters.entities.message_entity import MessageEntity


class IChatsRepository(ABC):
    @abstractmethod
    def get_chats(self) -> List[ChatEntity]:
        pass

    @abstractmethod
    def get_conversation_for_chat(self, chat_id: str, limit: int) -> List[MessageEntity]:
        pass

    @abstractmethod
    def change_conversation_name(self, chat_id: str, name: str):
        pass

    @abstractmethod
    def send_message(self, chat_id: str, message: str):
        pass

    @abstractmethod
    def create_group_chat(self, user_ids: List[str]) -> ChatEntity:
        pass