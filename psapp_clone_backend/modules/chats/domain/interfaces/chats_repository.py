from abc import ABC, abstractmethod


class IChatsRepository(ABC):
    @abstractmethod
    def get_chats(self):
        pass