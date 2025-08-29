# Frontend/frontend.py
import streamlit as st
import requests
import uuid

# Backend FastAPI URL
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Chatbot with Memory", page_icon="🤖", layout="centered")

st.title("🤖 Chatbot with FastAPI & Memory")

# User choice: Direct or Streaming
response_mode = st.radio(
    "Choose response type:",
    ["Direct", "Streaming"],
    horizontal=True
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "session_id" not in st.session_state:
    # Generate unique session_id for each user session
    st.session_state["session_id"] = str(uuid.uuid4())

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    # Add user message to history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    payload = {
        "session_id": st.session_state["session_id"],
        "user_message": user_input
    }

    bot_reply = ""

    try:
        if response_mode == "Direct":
            # Call normal /chat endpoint
            response = requests.post("http://127.0.0.1:8000/chat", json=payload)
            response.raise_for_status()
            bot_reply = response.json().get("response", "⚠️ No response from bot.")

            st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
            st.chat_message("assistant").markdown(bot_reply)

        else:  # Streaming
            response = requests.post("http://127.0.0.1:8000/chat/stream", json=payload, stream=True)
            message_placeholder = st.chat_message("assistant").markdown("...")
            for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                if chunk:
                    bot_reply += chunk
                    message_placeholder.markdown(bot_reply)

            st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        bot_reply = f"⚠️ Error: {str(e)}"
        st.chat_message("assistant").markdown(bot_reply)
