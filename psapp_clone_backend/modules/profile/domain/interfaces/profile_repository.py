from abc import ABC, abstractmethod
from typing import List

from psapp_clone_backend.modules.profile.adapters.entities.device_entity import DeviceEntity
from psapp_clone_backend.modules.profile.adapters.entities.profile_entity import ProfileEntity


class IProfileRepository(ABC):
    @abstractmethod
    def get_my_profile(self) -> ProfileEntity:
        pass

    @abstractmethod
    def get_my_devices(self) -> List[DeviceEntity]:
        pass
    