from fastapi import APIRouter, HTTPException
from schemas.chat import ChatRequest, ChatResponse
from services.chat import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
    responses={404: {"description": "Not found"}},
)

chat_service = ChatService()

@router.post("/{url}/", response_model=ChatResponse)
async def chat(url: str, request: ChatRequest):
    try:
        response = chat_service.chat(url, request.content)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
