from pydantic import BaseModel
from typing import Optional, List, Dict

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    user_message: str

class ChatResponse(BaseModel):
    session_id: str
    response: str
    history: List[Dict[str, str]]  # e.g. [{"role": "user", "content": "hi"}, ...]
