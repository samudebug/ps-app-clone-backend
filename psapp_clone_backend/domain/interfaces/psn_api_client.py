from abc import ABC, abstractmethod


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