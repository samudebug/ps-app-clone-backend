
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.friends.adapters.entities.friend_entity import FriendEntity
from psapp_clone_backend.modules.friends.adapters.repositories.friends_repository import FriendsRepositoryPSN
from psapp_clone_backend.modules.friends.features.check_friends.check_friends_usescase import CheckFriendsUseCase


router = APIRouter(prefix="/friends", tags=["friends"])

@router.get("/", response_model=FriendEntity)
def get_my_friends(request: Request):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    friends_repo = FriendsRepositoryPSN(client)
    usecase = CheckFriendsUseCase(friends_repo)
    response = usecase.execute()
    return JSONResponse([x.data.model_dump() for x in response])