from pydantic import BaseModel, Field
from psapp_clone_backend.modules.games.adapters.entities.trophy_group_entity import TrophyCountInfoEntity


class TrophySummaryEntity(BaseModel):
    total: int
    bronze: int
    silver: int
    gold: int
    platinum: int


