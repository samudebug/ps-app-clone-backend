from pydantic import BaseModel, Field


class DeviceEntity(BaseModel):
    device_id: str = Field(...)
    device_type: str = Field(...)
    activation_date: str = Field(...)