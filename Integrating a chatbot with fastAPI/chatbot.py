import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def stream_chatbot_response(messages: list):
    """
    Stream response from Groq API.
    Yields small incremental chunks as they arrive.
    """
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=1.0,
        max_completion_tokens=1024,
        top_p=0.95,
        stream=True
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content  # yield only new content each time
