from typing import List
from psapp_clone_backend.domain.interfaces.psn_api_client import IPSNAPIClient
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger
from psapp_clone_backend.modules.profile.adapters.entities.device_entity import DeviceEntity
from psapp_clone_backend.modules.profile.adapters.entities.profile_entity import ProfileEntity
from psapp_clone_backend.modules.profile.domain.interfaces.profile_repository import IProfileRepository


class ProfileRepositoryPSN(IProfileRepository):
    client: IPSNAPIClient
    logger = get_logger(__name__)
    def __init__(self, client: IPSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_my_profile(self) -> ProfileEntity:
        data = self.client.get_my_profile()
        self.logger.info(f"profile_data {data}")
        return ProfileEntity(**data)
    
    def get_my_devices(self) -> List[DeviceEntity]:
        devices = self.client.get_account_devices()
        return [DeviceEntity(**x) for x in devices]