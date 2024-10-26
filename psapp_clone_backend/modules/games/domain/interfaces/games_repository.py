from abc import ABC, abstractmethod


class IGamesRepository(ABC):
    @abstractmethod
    def get_games(self):
        pass

    @abstractmethod
    def get_trophy_groups(self, game_id: str):
        pass