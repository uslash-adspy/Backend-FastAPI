from typing import List
from pydantic import BaseModel

class ChatRequest(BaseModel):
    chat: List[str]
    content: str

class ChatResponse(BaseModel):
    response: str
