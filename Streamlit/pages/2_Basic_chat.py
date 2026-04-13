import streamlit as st
import numpy as np
import time
import random

st.set_page_config(page_title="Basic chat (random)")

# --- FUNÇÕES -------------------------------------------------------------
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",            
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# --- APLICAÇÃO -------------------------------------------------------------
st.markdown("# Cauã's AI ")
st.markdown(" Chatbot básico baseado em respostas aleatórias de uma lista pré-definida.")

# with st.chat_message(name="user", avatar="🦖"): #Pode-se trocar a imagem também por ícones disponíveis em https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
#     st.write("Hello! 👋")
#     # st.bar_chart(np.random.randn(30,2))

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
    # response = f"Bot: {prompt}"
    with st.chat_message("assistant"):
        # Simula extra de tempo de processamento
        with st.spinner("Thinking..."): 
            time.sleep(1.5)
        # st.markdown(f"Bot: {prompt}")
        response = st.write_stream(response_generator())

    #Adiciona mensagem do bot ao histórico
    st.session_state.messages.append({"role":"assistant",
                                      "content":response})