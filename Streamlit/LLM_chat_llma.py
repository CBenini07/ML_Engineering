import streamlit as st
import requests

# --- CONFIG LLAMA MODEL -------------------------------------------------------------
OLLAMA_API_URL = "http://localhost:11434/api/chat"

if "llama_model" not in st.session_state:
    st.session_state["llama_model"] = "llama3.2"

# --- APLICAÇÃO -------------------------------------------------------------
st.markdown("# Cauã's AI ")
st.markdown(" Basic LLM chatbot based on Ollama's Llama model")

# Inicializar o histórico do chat
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
        # Faz a requisição ao Ollama
        payload = {
            "model": st.session_state["llama_model"],
            "messages": [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            "stream": False  # pode usar True se quiser streaming
        }
        response = requests.post(OLLAMA_API_URL, json=payload)

        if response.status_code == 200:
            data = response.json()
            # Ollama retorna a resposta em "message"
            reply = data.get("message", {}).get("content", "")
            st.markdown(reply)
            # Adiciona mensagem do assistente ao histórico
            st.session_state.messages.append({"role": "assistant", "content": reply})
        else:
            st.error("Erro ao conectar com Ollama.")
