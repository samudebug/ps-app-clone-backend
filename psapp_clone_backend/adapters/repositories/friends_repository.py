from typing import List
from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.domain.interfaces.friends_repository import IFriendsRepository


class FriendsRepositoryPSN(IFriendsRepository):
    client: PSNAPIClient
    def __init__(self, client: PSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_friends(self) -> List[dict]:
        friends = self.client.get_account_friends()
        result = []
        for x in list(friends):
            presence = x.get_presence()
            profile_dict = x.profile()
            profile_dict['presence'] = presence['basicPresence']['primaryPlatformInfo']['onlineStatus']
            result.append(profile_dict)
        return result