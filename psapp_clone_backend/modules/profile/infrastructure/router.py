
from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from zope.component import getUtility
from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.profile.adapters.entities.device_entity import DeviceEntity
from psapp_clone_backend.modules.profile.adapters.entities.profile_entity import ProfileEntity
from psapp_clone_backend.modules.profile.adapters.repositories.profile_repository import ProfileRepositoryPSN
from psapp_clone_backend.modules.profile.features.check_devices.check_devices_usecase import CheckDevicesUseCase
from psapp_clone_backend.modules.profile.features.check_profile.check_profile_usecase import CheckProfileUseCase


router = APIRouter(prefix="/profile", tags=["profile"])



@router.get("/", response_model=ProfileEntity)
def get_my_profile(request: Request):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    profile_repo = ProfileRepositoryPSN(client)
    usecase = CheckProfileUseCase(profile_repo)
    response = usecase.execute()
    if response is not None and response.error is not None:
        return JSONResponse(response.error.__str__(), status_code=400)
    return JSONResponse(response.data.model_dump())



@router.get("/devices", response_model=List[DeviceEntity])
def get_my_devices(request: Request):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    profile_repo = ProfileRepositoryPSN(client)
    usecase = CheckDevicesUseCase(profile_repo)
    response = usecase.execute()
    if response is not None and response.error is not None:
        return JSONResponse(response.error.__str__(), status_code=400)
    return JSONResponse([x.model_dump() for x in response.data])