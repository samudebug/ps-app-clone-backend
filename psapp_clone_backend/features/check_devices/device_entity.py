from pydantic import BaseModel, Field


class DeviceEntity(BaseModel):
    device_id: str = Field(..., alias="deviceId")
    device_type: str = Field(..., alias="deviceType")
    activation_date: str = Field(..., alias="activationDate")