from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from zope.component import getUtility
from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.adapters.repositories.profile_repository import ProfileRepositoryPSN
from psapp_clone_backend.features.check_profile.check_profile_usecase import CheckProfileUseCase


router = APIRouter(prefix="/profile", tags=["profile"])



@router.get("/")
def get_my_profile(request: Request):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    profile_repo = ProfileRepositoryPSN(client)
    usecase = CheckProfileUseCase(profile_repo)
    response = usecase.execute()
    return JSONResponse(response.data)