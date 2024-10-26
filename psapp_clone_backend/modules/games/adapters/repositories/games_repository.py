from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.games.domain.interfaces.games_repository import IGamesRepository


class GamesRepositoryPSN(IGamesRepository):
    client: PSNAPIClient

    def __init__(self, client: PSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_games(self):
        return self.client.get_my_games()