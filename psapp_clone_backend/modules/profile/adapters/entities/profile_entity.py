from typing import List
from pydantic import BaseModel, Field

class AvatarInfo(BaseModel):
    size: str
    avatar_url: str = Field(..., alias="avatarUrl")

class ProfileEntity(BaseModel):
    id: str 
    username:str 
    np_id: str 
    avatar_urls: List[AvatarInfo] 
    about_me: str
