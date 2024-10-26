from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.profile.adapters.entities.profile_entity import (
    ProfileEntity,
)
from psapp_clone_backend.modules.profile.domain.interfaces.profile_repository import (
    IProfileRepository,
)
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger


class CheckProfileUseCase:
    repo: IProfileRepository
    logger = get_logger(__name__)

    def __init__(self, repo: IProfileRepository) -> None:
        self.repo = repo

    def execute(self) -> DataState[ProfileEntity]:
        profile = self.repo.get_my_profile()
        return DataState(data=ProfileEntity(**profile["profile"]))
