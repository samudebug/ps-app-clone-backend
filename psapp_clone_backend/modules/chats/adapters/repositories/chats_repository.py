from psapp_clone_backend.domain.interfaces.psn_api_client import IPSNAPIClient
from psapp_clone_backend.modules.chats.domain.interfaces.chats_repository import IChatsRepository


class ChatsRepository(IChatsRepository):
    client: IPSNAPIClient
    def __init__(self, client: IPSNAPIClient) -> None:
        super().__init__()
        self.client = client
    

    def get_chats(self):
        chats = self.client.get_chats()
        return chats
    
    def get_conversation_for_chat(self, chat_id: str, limit: int):
        conversations = self.client.get_conversation_for_chat(chat_id, limit)
        return conversations