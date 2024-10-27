from abc import ABC, abstractmethod
from typing import List


class IPSNAPIClient(ABC):
    @abstractmethod
    def me(self):
        pass

    @abstractmethod
    def get_account_devices(self):
        pass

    @abstractmethod
    def get_account_friends(self):
        pass

    @abstractmethod
    def get_account_blocked(self):
        pass

    @abstractmethod
    def get_my_games(self):
        pass

    @abstractmethod
    def get_trophy_groups(self, title_id: str):
        pass

    @abstractmethod
    def get_trophies_by_group(self, title_id: str, group_id: str):
        pass

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