from typing import List
from psapp_clone_backend.domain.interfaces.psn_api_client import IPSNAPIClient
from psapp_clone_backend.modules.friends.adapters.entities.friend_entity import FriendEntity
from psapp_clone_backend.modules.friends.domain.interfaces.friends_repository import IFriendsRepository


class FriendsRepositoryPSN(IFriendsRepository):
    client: IPSNAPIClient
    def __init__(self, client: IPSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_friends(self) -> List[FriendEntity]:
        friends = self.client.get_account_friends()
        return [FriendEntity(**friend) for friend in friends]
    

    def get_blocked(self) -> List[FriendEntity]:
        blocked = self.client.get_account_blocked()
        return [FriendEntity(**friend) for friend in blocked]
    