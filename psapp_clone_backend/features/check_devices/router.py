from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.adapters.repositories.profile_repository import ProfileRepositoryPSN
from psapp_clone_backend.features.check_devices.check_devices_usecase import CheckDevicesUseCase
from psapp_clone_backend.features.check_devices.device_entity import DeviceEntity


router = APIRouter(prefix="/profile", tags=["profile"])


@router.get("/devices", response_model=List[DeviceEntity])
def get_my_devices(request: Request):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    profile_repo = ProfileRepositoryPSN(client)
    usecase = CheckDevicesUseCase(profile_repo)
    response = usecase.execute()
    return JSONResponse([x.data.model_dump() for x in response])