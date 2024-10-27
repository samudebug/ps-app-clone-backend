from psapp_clone_backend.domain.interfaces.psn_api_client import IPSNAPIClient
from psapp_clone_backend.modules.games.adapters.entities.game_entity import GameEntity
from psapp_clone_backend.modules.games.adapters.entities.trophy_entity import (
    TrophyEntity,
)
from psapp_clone_backend.modules.games.adapters.entities.trophy_group_entity import (
    TrophyGroupEntity,
)
from psapp_clone_backend.modules.games.domain.interfaces.games_repository import (
    IGamesRepository,
)


class GamesRepositoryPSN(IGamesRepository):
    client: IPSNAPIClient

    def __init__(self, client: IPSNAPIClient) -> None:
        super().__init__()
        self.client = client

    def get_games(self):
        games = self.client.get_my_games()
        return [GameEntity(**game) for game in games]

    def get_trophy_groups(self, title_id: str):
        groups = self.client.get_trophy_groups(title_id)
        return [TrophyGroupEntity(**group) for group in groups]

    def get_trophies_by_group(self, title_id: str, group_id: str):
        trophies = self.client.get_trophies_by_group(title_id, group_id)
        return [TrophyEntity(**trophy) for trophy in trophies]
