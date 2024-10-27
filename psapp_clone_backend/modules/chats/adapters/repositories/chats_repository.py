from typing import List
from psapp_clone_backend.domain.interfaces.psn_api_client import IPSNAPIClient
from psapp_clone_backend.modules.chats.adapters.entities.chat_entity import ChatEntity
from psapp_clone_backend.modules.chats.adapters.entities.message_entity import MessageEntity
from psapp_clone_backend.modules.chats.domain.interfaces.chats_repository import IChatsRepository


class ChatsRepository(IChatsRepository):
    client: IPSNAPIClient
    def __init__(self, client: IPSNAPIClient) -> None:
        super().__init__()
        self.client = client
    

    def get_chats(self):
        chats = self.client.get_chats()
        return [ChatEntity(**chat) for chat in chats]
    
    def get_conversation_for_chat(self, chat_id: str, limit: int):
        conversations = self.client.get_conversation_for_chat(chat_id, limit)
        return [MessageEntity(**message) for message in conversations]
    
    def change_conversation_name(self, chat_id: str, name: str):
        self.client.change_conversation_name(chat_id, name)
    
    def send_message(self, chat_id: str, message: str):
        self.client.send_message(chat_id, message)
    
    def create_group_chat(self, user_ids: List[str]):
        new_group = self.client.create_group_chat(user_ids)
        return ChatEntity(**new_group) 