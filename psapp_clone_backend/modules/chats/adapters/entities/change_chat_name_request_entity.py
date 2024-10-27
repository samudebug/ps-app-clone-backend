from pydantic import BaseModel


class ChangeChatNameRequestEntity(BaseModel):
    name: str