from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic_core import PydanticUndefined

class AvatarInfo(BaseModel):
    size: str
    avatar_url: str = Field(..., alias="url")

class FriendEntity(BaseModel):
    username: str = Field(..., alias="onlineId")
    about_me: str = Field(..., alias="aboutMe")
    avatar_urls: List[AvatarInfo] = Field(..., alias="avatars")
    presence: Optional[str] = Field(None, alias="presence")
