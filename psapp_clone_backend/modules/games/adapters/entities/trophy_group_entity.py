from pydantic import BaseModel, Field

class TrophyCountEntity(BaseModel):
    total: int
    earned: int

class TrophyCountInfoEntity(BaseModel):
    bronze: TrophyCountEntity
    silver: TrophyCountEntity
    gold: TrophyCountEntity
    platinum: TrophyCountEntity



class TrophyGroupEntity(BaseModel):
    id: str
    name: str
    detail: str
    icon_url: str = Field(..., alias='iconUrl')
    trophy_count_info: TrophyCountInfoEntity = Field(..., alias="trophyCountInfo")

