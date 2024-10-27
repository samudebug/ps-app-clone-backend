from abc import ABC, abstractmethod
from typing import List

from psapp_clone_backend.modules.games.adapters.entities.game_entity import GameEntity
from psapp_clone_backend.modules.games.adapters.entities.trophy_entity import TrophyEntity
from psapp_clone_backend.modules.games.adapters.entities.trophy_group_entity import TrophyGroupEntity


class IGamesRepository(ABC):
    @abstractmethod
    def get_games(self) -> List[GameEntity]:
        pass

    @abstractmethod
    def get_trophy_groups(self, title_id: str) -> List[TrophyGroupEntity]:
        pass

    @abstractmethod
    def get_trophies_by_group(self, title_id: str, group_id: str) -> List[TrophyEntity]:
        pass