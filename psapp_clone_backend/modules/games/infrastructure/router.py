from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.games.adapters.entities.game_entity import GameEntity
from psapp_clone_backend.modules.games.adapters.entities.trophy_entity import TrophyEntity
from psapp_clone_backend.modules.games.adapters.entities.trophy_group_entity import TrophyGroupEntity
from psapp_clone_backend.modules.games.adapters.repositories.games_repository import GamesRepositoryPSN
from psapp_clone_backend.modules.games.features.check_games.check_games_usecase import CheckGamesUseCase
from psapp_clone_backend.modules.games.features.check_trophies_by_group.check_trophies_by_group_usecase import CheckTrophiesByGroupUseCase
from psapp_clone_backend.modules.games.features.check_trophy_groups.check_trophy_groups_usecase import CheckTrophyGroupsUseCase


router = APIRouter(prefix="/games", tags=["games"])


@router.get("/", response_model=List[GameEntity])
def get_games(request: Request):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    games_repo = GamesRepositoryPSN(client)
    usecase = CheckGamesUseCase(games_repo)
    response = usecase.execute()
    if response is not None and response.error is not None:
        return JSONResponse(response.error.__str__(), status_code=400)
    return JSONResponse([x.model_dump() for x in response.data])
    
@router.get("/{title_id}/trophy_groups", response_model=List[TrophyGroupEntity])
def get_trophy_groups(request: Request, title_id: str):
    client = PSNAPIClient(request.state.context_data.get("sso_code"), request.headers.get("Accept-Language"))
    games_repo = GamesRepositoryPSN(client)
    usecase = CheckTrophyGroupsUseCase(games_repo)
    response = usecase.execute(title_id)
    if response is not None and response.error is not None:
        return JSONResponse(response.error.__str__(), status_code=400)
    return JSONResponse([x.model_dump() for x in response.data])

@router.get("/{title_id}/trophy_groups/{group_id}/trophies", response_model=List[TrophyEntity])
def get_trophies_by_group(request: Request, title_id: str, group_id: str):
    client = PSNAPIClient(request.state.context_data.get("sso_code"), request.headers.get("Accept-Language"))
    games_repo = GamesRepositoryPSN(client)
    usecase = CheckTrophiesByGroupUseCase(games_repo)
    response = usecase.execute(title_id, group_id)
    if response is not None and response.error is not None:
        return JSONResponse(response.error.__str__(), status_code=400)
    return JSONResponse([x.model_dump() for x in response.data])
    
