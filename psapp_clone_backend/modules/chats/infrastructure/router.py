from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.chats.adapters.entities.change_chat_name_request_entity import ChangeChatNameRequestEntity
from psapp_clone_backend.modules.chats.adapters.entities.chat_entity import ChatEntity
from psapp_clone_backend.modules.chats.adapters.entities.message_entity import MessageEntity
from psapp_clone_backend.modules.chats.adapters.repositories.chats_repository import ChatsRepository
from psapp_clone_backend.modules.chats.features.change_chat_name.change_chat_name_usecase import ChangeChatNameUseCase
from psapp_clone_backend.modules.chats.features.check_chats.check_chats_usecase import CheckChatsUseCase
from psapp_clone_backend.modules.chats.features.check_conversation.check_conversation_usecase import CheckConversationUseCase


router = APIRouter(prefix="/chats", tags=["chats"])

@router.get("/", response_model=List[ChatEntity])
def get_chats(request: Request):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    chats_repo = ChatsRepository(client)
    usecase = CheckChatsUseCase(chats_repo)
    response = usecase.execute()
    return JSONResponse([x.data.model_dump() for x in response])

@router.get("/{chat_id}", response_model=List[MessageEntity])
def get_conversation_for_chat(request: Request, chat_id: str, limit: int = 20):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    chats_repo = ChatsRepository(client)
    usecase = CheckConversationUseCase(chats_repo)
    response = usecase.execute(chat_id, limit=limit)
    return JSONResponse([x.data.model_dump() for x in response])
    
@router.put("/{chat_id}")
def change_chat_name(request: Request, chat_id: str, change_name_request: ChangeChatNameRequestEntity):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    chats_repo = ChatsRepository(client)
    usecase = ChangeChatNameUseCase(chats_repo)
    response = usecase.execute(chat_id, change_name_request.name)
    if response.error is not None:
        return JSONResponse({"error": response.error.__str__()}, status_code=400)
    return JSONResponse({"message": "Chat name changed successfully"})
    
    