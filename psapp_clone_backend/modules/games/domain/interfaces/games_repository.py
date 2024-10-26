from abc import ABC, abstractmethod


class IGamesRepository(ABC):
    @abstractmethod
    def get_games(self):
        pass

    @abstractmethod
    def get_trophy_groups(self, title_id: str):
        pass

    @abstractmethod
    def get_trophies_by_group(self, title_id: str, group_id: str):
        pass