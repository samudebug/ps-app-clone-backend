from abc import ABC, abstractmethod


class IGamesRepository(ABC):
    @abstractmethod
    def get_games(self):
        pass