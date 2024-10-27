from pydantic import BaseModel, Field, field_serializer
message_types = {
    1: 'TEXT',
    3: 'IMAGE'
}

class MessageEntity(BaseModel):
    id: str
    body: str
    created_at: str = Field(..., alias="createdAt")
    message_type: int = Field(..., alias="messageType")
    sender: str

    @field_serializer('message_type')
    def serialize_message_type(self, message_type: int, _info):
        return message_types.get(message_type, 'UNKNOWN')