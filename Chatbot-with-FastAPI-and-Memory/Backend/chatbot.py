import os
from typing import Generator, List, Dict, Optional
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
_api_key = os.getenv("GROQ_API_KEY")
if not _api_key:
    raise RuntimeError("GROQ_API_KEY not found in .env")

client = Groq(api_key=_api_key)

MODEL = "llama-3.1-8b-instant"  # pick the model you prefer

def generate_reply(messages: List[Dict[str, str]]) -> str:
    """
    Non-streaming completion. Returns full assistant message.
    """
    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.4,
    )
    # Groq SDK returns .choices[0].message.content
    return completion.choices[0].message.content

def stream_reply(messages: List[Dict[str, str]]) -> Generator[str, None, None]:
    """
    Streaming completion. Yields text chunks as they arrive.
    """
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.4,
        stream=True,
    )
    # Iterate streaming chunks
    for chunk in stream:
        delta: Optional[str] = None
        try:
            delta = chunk.choices[0].delta.content
        except Exception:
            delta = None
        if delta:
            yield delta
