from abc import ABC, abstractmethod
from typing import Any, List


class IPSNAPIClient(ABC):
    @abstractmethod
    def me(self):
        pass

    @abstractmethod
    def get_my_profile(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_devices(self) -> List[dict[str, Any]]:
        pass

    @abstractmethod
    def get_account_friends(self) -> List[dict[str, Any]]:
        pass

    @abstractmethod
    def get_account_blocked(self) -> List[dict[str, Any]]:
        pass

    @abstractmethod
    def get_my_games(self) -> List[dict[str, Any]]:
        pass

    @abstractmethod
    def get_trophy_groups(self, title_id: str) -> List[dict[str, Any]]:
        pass

    @abstractmethod
    def get_trophies_by_group(self, title_id: str, group_id: str) -> List[dict[str, Any]]:
        pass

    @abstractmethod
    def get_chats(self) -> List[dict[str, Any]]:
        pass

    @abstractmethod
    def get_conversation_for_chat(self, chat_id: str, limit: int) -> List[dict[str, Any]]:
        pass

    @abstractmethod
    def change_conversation_name(self, chat_id: str, name: str):
        pass

    @abstractmethod
    def send_message(self, chat_id: str, message: str):
        pass
    
    @abstractmethod
    def create_group_chat(self, user_ids: List[str]) -> dict[str, Any]:
        pass

    @abstractmethod
    def leave_group_chat(self, chat_id: str):
        pass