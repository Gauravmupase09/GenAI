import streamlit as st
import requests

st.set_page_config(page_title="FastAPI Chatbot", page_icon="🤖")
st.title("🤖 Chatbot with FastAPI & Streamlit (Streaming)")

FASTAPI_STREAM_URL = "http://127.0.0.1:8000/chat/stream"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Use placeholder for live bot response
    response_placeholder = st.empty()
    full_reply = ""

    try:
        with requests.post(FASTAPI_STREAM_URL, json={"message": prompt}, stream=True) as r:
            for chunk in r.iter_content(chunk_size=64, decode_unicode=True):
                if chunk:
                    full_reply += chunk
                    response_placeholder.markdown(full_reply)
    except requests.exceptions.ChunkedEncodingError:
        response_placeholder.markdown(full_reply + "\n\n⚠️ Stream ended prematurely.")

    st.session_state.messages.append({"role": "assistant", "content": full_reply})
