from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from chatbot import stream_chatbot_response

app = FastAPI()

@app.post("/chat/stream")
async def chat_stream(request: Request):
    data = await request.json()
    user_input = data.get("message", "")

    messages = [
        {"role": "system", "content": "You are a helpful chatbot."},
        {"role": "user", "content": user_input}
    ]

    # Generator to stream incremental chunks
    def event_stream():
        for chunk in stream_chatbot_response(messages):
            yield chunk

    return StreamingResponse(event_stream(), media_type="text/plain")
