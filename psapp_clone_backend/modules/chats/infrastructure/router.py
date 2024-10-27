from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from psapp_clone_backend.adapters.clients.psn_awp_client import PSNAPIClient
from psapp_clone_backend.modules.chats.adapters.entities.chat_entity import ChatEntity
from psapp_clone_backend.modules.chats.adapters.repositories.chats_repository import ChatsRepository
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

@router.get("/{chat_id}")
def get_conversation_for_chat(request: Request, chat_id: str):
    client = PSNAPIClient(request.state.context_data.get("sso_code"))
    chats_repo = ChatsRepository(client)
    usecase = CheckConversationUseCase(chats_repo)
    response = usecase.execute(chat_id, limit=20)
    return JSONResponse([x.data.model_dump() for x in response])
    
