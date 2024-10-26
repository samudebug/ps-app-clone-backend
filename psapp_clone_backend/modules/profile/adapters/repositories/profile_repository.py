from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.profile.domain.interfaces.profile_repository import IProfileRepository


class ProfileRepositoryPSN(IProfileRepository):
    client: PSNAPIClient
    def __init__(self, client: PSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_my_profile(self):
        data = self.client.me()
        return data.get_profile_legacy()
    
    def get_my_devices(self):
        devices = self.client.get_account_devices()
        return devices