from abc import ABC, abstractmethod


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