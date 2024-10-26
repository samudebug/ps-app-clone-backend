from pydantic import BaseModel, Field

class DurationEntity(BaseModel):
    hours: int
    minutes: int


class GameEntity(BaseModel):
    id: str
    name: str
    image_url: str = Field(..., alias="imageUrl")
    duration: DurationEntity
    