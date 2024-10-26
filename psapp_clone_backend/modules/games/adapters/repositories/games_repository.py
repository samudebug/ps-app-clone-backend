from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.games.domain.interfaces.games_repository import IGamesRepository


class GamesRepositoryPSN(IGamesRepository):
    client: PSNAPIClient

    def __init__(self, client: PSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_games(self):
        return self.client.get_my_games()
    
    def get_trophy_groups(self, title_id: str):
        groups = self.client.get_trophy_groups(title_id)
        return groups
    
    def get_trophies_by_group(self, title_id: str, group_id: str):
        trophies = self.client.get_trophies_by_group(title_id, group_id)
        return trophies