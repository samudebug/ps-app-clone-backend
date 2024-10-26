from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.games.adapters.entities.game_entity import GameEntity
from psapp_clone_backend.modules.games.domain.interfaces.games_repository import IGamesRepository


class CheckGamesUseCase:
    repo: IGamesRepository

    def __init__(self, repo: IGamesRepository) -> None:
        self.repo = repo
    
    def execute(self) -> List[DataState[GameEntity]]:
        games = self.repo.get_games()
        return [DataState(data=GameEntity(**x)) for x in games]