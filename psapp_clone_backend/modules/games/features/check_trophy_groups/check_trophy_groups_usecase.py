from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger
from psapp_clone_backend.modules.games.adapters.entities.trophy_group_entity import TrophyGroupEntity
from psapp_clone_backend.modules.games.domain.interfaces.games_repository import IGamesRepository


class CheckTrophyGroupsUseCase:
    repo: IGamesRepository
    logger = get_logger(__name__)
    def __init__(self, repo: IGamesRepository) -> None:
        self.repo = repo
    
    def execute(self, title_id: str) -> DataState[List[TrophyGroupEntity]]:
        try:
            groups = self.repo.get_trophy_groups(title_id)
            return DataState(data=groups)
        except Exception as e:
            return DataState(error=e)