from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.games.adapters.entities.game_entity import GameEntity
from psapp_clone_backend.modules.games.adapters.repositories.games_repository import GamesRepositoryPSN
from psapp_clone_backend.modules.games.features.check_games.check_games_usecase import CheckGamesUseCase


router = APIRouter(prefix="/games", tags=["games"])


@router.get("/", response_model=List[GameEntity])
def get_games(request: Request):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    games_repo = GamesRepositoryPSN(client)
    usecase = CheckGamesUseCase(games_repo)
    games = usecase.execute()
    return JSONResponse([x.data.model_dump() for x in games])
    
    