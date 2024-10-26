from pydantic import BaseModel, Field


class TrophyEntity(BaseModel):
    id: str
    type: str
    name: str
    detail: str
    icon_url: str = Field(..., alias='iconUrl')
    earned: bool