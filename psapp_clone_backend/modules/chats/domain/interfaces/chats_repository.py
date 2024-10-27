from abc import ABC, abstractmethod
from typing import List


class IChatsRepository(ABC):
    @abstractmethod
    def get_chats(self):
        pass

    @abstractmethod
    def get_conversation_for_chat(self, chat_id: str, limit: int):
        pass

    @abstractmethod
    def change_conversation_name(self, chat_id: str, name: str):
        pass

    @abstractmethod
    def send_message(self, chat_id: str, message: str):
        pass

    @abstractmethod
    def create_group_chat(self, user_ids: List[str]):
        pass