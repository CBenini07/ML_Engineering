import streamlit as st
import numpy as np
import time
import random
from openai import OpenAI

st.set_page_config(page_title="LLM chat (OpenAI)")

# --- CONFIG GPT MODEL -------------------------------------------------------------
CLIENT = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# --- APLICAÇÃO -------------------------------------------------------------
st.markdown("# Cauã's AI ")
st.markdown(" Chatbot básico baseado nos modelos GPTs (OpenAI).")


# Inicializar o histórico do chat (Como o Streamlit fica em costante 
# loop, é importante para não reescrever as mensagens)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Apresenta mensagens do histórico na reexecução do app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Pls, send a message to Cauã's AI.")
if prompt:
    # --- Reação ao input do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    # Adiciona mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", 
                                      "content": prompt})   

    # --- Reação do bot
    with st.chat_message("assistant"):
        stream = CLIENT.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream = True
        )
        response = st.write_stream(stream)

        # Adiciona mensagem do usuário ao histórico
        st.session_state.messages.append({"role": "assistant",
                                          "content": response})  