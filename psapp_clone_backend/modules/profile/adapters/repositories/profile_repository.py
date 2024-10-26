from psapp_clone_backend.domain.interfaces.psn_api_client import IPSNAPIClient
from psapp_clone_backend.modules.profile.domain.interfaces.profile_repository import IProfileRepository


class ProfileRepositoryPSN(IProfileRepository):
    client: IPSNAPIClient
    def __init__(self, client: IPSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_my_profile(self):
        data = self.client.me()
        return data.get_profile_legacy()
    
    def get_my_devices(self):
        devices = self.client.get_account_devices()
        return devices