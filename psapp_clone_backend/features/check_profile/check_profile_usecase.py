import logging
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.domain.interfaces.profile_repository import IProfileRepository


class CheckProfileUseCase:
    repo: IProfileRepository
    logger = logging.getLogger(__name__)
    def __init__(self, repo: IProfileRepository) -> None:
        self.repo = repo
    
    def execute(self):
        profile = self.repo.get_my_profile()
        self.logger.info(f"Profile Data profile {profile}")
        return DataState(data=profile)