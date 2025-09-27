import streamlit as st
import requests
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent


st.title("ESI-SBA Chatbot")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"


def load_messages():
    return st.session_state["messages"]


def save_messages(messages):
    st.session_state.messages = messages


if "messages" not in st.session_state:
    st.session_state.messages = []


# The sidebar
with st.sidebar:
    st.image(BASE_DIR / "logo.png")
    if st.button("Supprimer l'historique"):
        st.session_state.messages = []

# Display conversation
for message in st.session_state["messages"]:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("Vous voulez savoir quoi à propose de ESI-SBA ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        url = "https://esi-rag-chatbot-1.onrender.com/ask"
        payload = {"question": prompt}
        message_placeholder = st.empty()
        bot_response = ""
        message_placeholder.markdown("Entrain de chercher...")
        response = requests.post(url, json=payload)
        bot_response = response.json()["answer"]
        partial_response = ""
        for c in bot_response:
            partial_response += c
            message_placeholder.markdown(partial_response)
            time.sleep(0.02)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
