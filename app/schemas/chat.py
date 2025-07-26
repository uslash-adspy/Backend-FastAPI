from typing import List, Optional
from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    chat: List[Message]
    content: str

class ChatResponse(BaseModel):
    content: str
    result: Optional[str]
