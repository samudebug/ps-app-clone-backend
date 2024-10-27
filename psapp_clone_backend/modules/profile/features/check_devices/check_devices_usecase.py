from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.modules.profile.adapters.entities.device_entity import (
    DeviceEntity,
)
from psapp_clone_backend.modules.profile.domain.interfaces.profile_repository import (
    IProfileRepository,
)
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger


class CheckDevicesUseCase:
    repo: IProfileRepository
    logger = get_logger(__name__)

    def __init__(self, repo: IProfileRepository) -> None:
        self.repo = repo

    def execute(self) -> DataState[List[DeviceEntity]]:
        try:
            devices = self.repo.get_my_devices()
            return DataState(data=devices)
        except Exception as e:
            return DataState(error=e)
