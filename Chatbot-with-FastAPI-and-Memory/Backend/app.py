from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
import uuid
from typing import Iterator

from .models import ChatRequest, ChatResponse
from .memory import start_session, get_history, save_history, trim_history
from .chatbot import generate_reply, stream_reply

app = FastAPI(title="Chatbot with FastAPI + Memory + Streaming")

@app.get("/health")
def health():
    return {"status": "ok"}

def _ensure_session(session_id: str | None) -> str:
    if not session_id:
        new_id = str(uuid.uuid4())
        start_session(new_id)
        return new_id
    if not get_history(session_id):
        start_session(session_id)
    return session_id

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """
    Non-streaming chat: returns full JSON with response + updated history.
    """
    session_id = _ensure_session(req.session_id)
    history = get_history(session_id)

    history.append({"role": "user", "content": req.user_message})
    history = trim_history(history)

    assistant_text = generate_reply(history)
    history.append({"role": "assistant", "content": assistant_text})

    save_history(session_id, history)

    return ChatResponse(
        session_id=session_id,
        response=assistant_text,
        history=history
    )

@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    """
    Streaming chat endpoint. Streams plain text chunks.
    At the end, it saves the full assistant message to memory.
    """
    session_id = _ensure_session(req.session_id)
    history = get_history(session_id)

    history.append({"role": "user", "content": req.user_message})
    history = trim_history(history)

    def token_generator() -> Iterator[bytes]:
        buffer = []
        for chunk in stream_reply(history):
            buffer.append(chunk)
            yield chunk.encode("utf-8")
        # after stream finishes, persist assistant message
        assistant_text = "".join(buffer)
        history.append({"role": "assistant", "content": assistant_text})
        save_history(session_id, history)

    # text/plain chunked streaming keeps client simple (no SSE parsing)
    return StreamingResponse(token_generator(), media_type="text/plain")
