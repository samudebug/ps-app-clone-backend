from typing import List
from psapp_clone_backend.domain.interfaces.psn_api_client import IPSNAPIClient
from psapp_clone_backend.modules.friends.domain.interfaces.friends_repository import IFriendsRepository


class FriendsRepositoryPSN(IFriendsRepository):
    client: IPSNAPIClient
    def __init__(self, client: IPSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_friends(self) -> List[dict]:
        friends = self.client.get_account_friends()
        result = []
        for x in list(friends):
            presence = x.get_presence()
            profile_dict = x.profile()
            profile_dict['id'] = x.account_id
            profile_dict['presence'] = presence['basicPresence']['primaryPlatformInfo']['onlineStatus']
            result.append(profile_dict)
        return result
    

    def get_blocked(self) -> List[dict]:
        blocked = self.client.get_account_blocked()
        result = []
        for x in list(blocked):
            profile_dict = x.profile()
            result.append(profile_dict)
        return result
    