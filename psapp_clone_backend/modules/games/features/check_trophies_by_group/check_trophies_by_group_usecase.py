from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger
from psapp_clone_backend.modules.games.adapters.entities.trophy_entity import TrophyEntity
from psapp_clone_backend.modules.games.domain.interfaces.games_repository import IGamesRepository


class CheckTrophiesByGroupUseCase:
    repo: IGamesRepository
    logger = get_logger(__name__)
    def __init__(self, repo: IGamesRepository) -> None:
        self.repo = repo
    
    def execute(self, title_id: str, group_id: str) -> List[DataState[TrophyEntity]]:
        trophies = self.repo.get_trophies_by_group(title_id, group_id)
        return [DataState(data=TrophyEntity(**x)) for x in trophies]