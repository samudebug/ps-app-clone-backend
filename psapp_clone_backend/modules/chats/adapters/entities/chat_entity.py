from pydantic import BaseModel


class ChatEntity(BaseModel):
    id: str
    members: str