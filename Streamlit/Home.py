import streamlit as st

st.set_page_config(
    page_title="introdução",
    page_icon="👋",
)

st.write("# Bem-vindo à demo de Streamlit! 👋")

st.sidebar.success("Selecione uma das demos acima.")

st.markdown(
    """
    Essa é uma demo realizada com base na documentação oficial do streamlit (https://docs.streamlit.io/get-started/tutorials/).

    Selecione uma das demos ao lado para visualizar funções do framework.
    """
)

st.markdown("## Central de Aprendizado não-supervisionado:")
st.page_link("pages/1_Clustering.py", label="1. Agrupamento")

st.markdown("## Central de Chatbots 🤖:")
st.page_link("pages/2_Basic_chat.py", label="1. Basic Chat")
st.page_link("pages/3_LLM_chat_OpenAI.py", label="2. OpenAI chat")
st.page_link("pages/4_LLM_chat_llma.py", label="3. Ollama Chat")