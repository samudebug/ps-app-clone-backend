from pydantic import BaseModel, field_serializer
type_map = {
    0: 'DM',
    1: 'GROUP'
}

class ChatEntity(BaseModel):
    id: str
    members: str
    type: int
    name: str

    @field_serializer('type')
    def serialize_type(self, type: int, _info):
        print(f"Type of group is {type} for group {self.id}")
        return type_map.get(type, 'UNKNOWN')