from pydantic import BaseModel, Field, field_serializer
from datetime import datetime
import json

class TrophyEntity(BaseModel):
    id: str
    type: str
    name: str
    detail: str
    icon_url: str = Field(..., alias='iconUrl')
    earned: bool
    hidden: bool
    earned_date: datetime | None = Field(default=None, alias='earnedDate')

    @field_serializer('earned_date')
    def serialize_earned_date(self, value: datetime, _info) -> str:
        if value is None:
            return None
        return value.isoformat()
