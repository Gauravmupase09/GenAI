import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Groq Chatbot")
st.write("Chat with the bot powered by **Groq + LLaMA-3.1**")

# Session state for storing messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Prepare assistant message container
    with st.chat_message("assistant"):
        bot_reply = st.empty()  # placeholder for live updates
        full_reply = ""

        # Stream response from Groq
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages,
            temperature=2,
            max_completion_tokens=1024,
            top_p=0.95,
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                full_reply += chunk.choices[0].delta.content
                bot_reply.markdown(full_reply)  # updates live

    # Save bot reply
    st.session_state.messages.append({"role": "assistant", "content": full_reply})
