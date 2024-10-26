from typing import List
from psapp_clone_backend.adapters.entities.data_state import DataState
from psapp_clone_backend.domain.interfaces.profile_repository import IProfileRepository
from psapp_clone_backend.features.check_devices.device_entity import DeviceEntity
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger


class CheckDevicesUseCase:
    repo: IProfileRepository
    logger = get_logger(__name__)

    def __init__(self, repo: IProfileRepository) -> None:
        self.repo = repo
    

    def execute(self) -> List[DataState[DeviceEntity]]:
        devices = self.repo.get_my_devices()
        return [DataState(data=DeviceEntity(**x)) for x in devices]