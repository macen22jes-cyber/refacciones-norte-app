import streamlit as st
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

# Configuración de la interfaz
st.set_page_config(page_title="Refacciones del Norte - Asistente IA", page_icon="🔧")
st.title("🔧 Refacciones del Norte")
st.caption("Asistente Virtual de Control y Validación de Compras")

# Datos de conexión de tu proyecto en Microsoft Foundry
ENDPOINT = "https://proyecto2adr-resource.services.ai.azure.com/api/projects/proyecto2adr"
AGENT_NAME = "RefaccionesNorte-AI"

project_client = AIProjectClient(
    endpoint=ENDPOINT,
    credential=DefaultAzureCredential(),
    allow_preview=True,
)
# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de chat del usuario
if prompt := st.chat_input("Escribe tu consulta sobre refacciones o sensores..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Envío de la consulta al agente en Azure
        openai_client = project_client.get_openai_client(agent_name=AGENT_NAME)
        conversation = openai_client.conversations.create()
        
        response = openai_client.responses.create(
            conversation_id=conversation.id,
            input=[{"role": "user", "content": prompt}]
        )
        
        reply_text = response.output[0].content[0].text.value
        st.markdown(reply_text)
        st.session_state.messages.append({"role": "assistant", "content": reply_text})
