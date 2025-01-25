from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.profile.adapters.entities.trophy_summary_entity import TrophySummaryEntity
from psapp_clone_backend.modules.profile.domain.interfaces.profile_repository import IProfileRepository
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger

class GetTrophySummaryUseCase:
    repo: IProfileRepository
    logger = get_logger(__name__)

    def __init__(self, repo: IProfileRepository) -> None:
        self.repo = repo

    def execute(self) -> DataState[TrophySummaryEntity]:
        try:
            summary = self.repo.get_trophy_summary()
            return DataState(data=summary)
        except Exception as e:
            return DataState(error=e)
