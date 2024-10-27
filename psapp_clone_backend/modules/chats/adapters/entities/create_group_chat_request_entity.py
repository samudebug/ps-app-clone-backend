from typing import List
from pydantic import BaseModel


class CreateGroupChatRequestEntity(BaseModel):
    user_ids: List[str]