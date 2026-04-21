import streamlit as st
from agente import LumiAgente

# Configuração visual da página
st.set_page_config(page_title="Lumi 🧼", page_icon="🧼")
st.title("🧼 Lumi: Higiene Financeira")
st.markdown("Sua mentora financeira para organizar o saldo e conquistar metas.")

# Inicializa o agente se ele ainda não existir na sessão
if "lumi" not in st.session_state:
    st.session_state.lumi = LumiAgente()

# Histórico de conversas
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens do chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada do usuário
if prompt := st.chat_input("Como organizar meu saldo hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta da Lumi
    with st.chat_message("assistant"):
        resposta = st.session_state.lumi.responder(prompt)
        st.markdown(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
