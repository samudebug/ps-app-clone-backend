from pydantic import BaseModel


class SendMessageRequestEntity(BaseModel):
    message: str