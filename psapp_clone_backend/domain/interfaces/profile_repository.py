from abc import ABC, abstractmethod


class IProfileRepository(ABC):
    @abstractmethod
    def get_my_profile(self):
        pass