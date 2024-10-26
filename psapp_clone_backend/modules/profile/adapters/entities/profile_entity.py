from typing import List
from pydantic import BaseModel, Field

class AvatarInfo(BaseModel):
    size: str
    avatar_url: str = Field(..., alias="avatarUrl")

class ProfileEntity(BaseModel):
    id: str = Field(..., alias="accountId")
    username:str = Field(..., alias="onlineId")
    np_id: str = Field(..., alias="npId")
    avatar_urls: List[AvatarInfo] = Field(..., alias="avatarUrls")
    about_me: str = Field(..., alias="aboutMe")
