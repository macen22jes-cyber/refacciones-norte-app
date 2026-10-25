import streamlit as st
from azure.ai.projects import AIProjectClient
from azure.identity import ClientSecretCredential

# Configuración de la interfaz
st.set_page_config(
    page_title="Refacciones del Norte - Asistente IA", page_icon=""
)
st.title("Refacciones del Norte")
st.caption("Asistente Virtual de Control y Validación de Compras")

# Datos de conexión del proyecto en Microsoft Foundry
ENDPOINT = st.secrets["ENDPOINT"]
AGENT_NAME = "RefaccionesNorte-AI"

# Credenciales de Service Principal leídas desde Streamlit Secrets
credential = ClientSecretCredential(
    tenant_id=st.secrets["AZURE_TENANT_ID"],
    client_id=st.secrets["AZURE_CLIENT_ID"],
    client_secret=st.secrets["AZURE_CLIENT_SECRET"],
)

project_client = AIProjectClient(
    endpoint=ENDPOINT, credential=credential, allow_preview=True
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
    try:
      # Conexión al agente en Azure AI Foundry
      openai_client = project_client.get_openai_client(agent_name=AGENT_NAME)
      conversation = openai_client.conversations.create()

      response = openai_client.responses.create(
          conversation_id=conversation.id,
          input=[{"role": "user", "content": prompt}],
      )

      reply_text = response.output[0].content[0].text.value
      st.markdown(reply_text)
      st.session_state.messages.append(
          {"role": "assistant", "content": reply_text}
      )
    except Exception as e:
      st.error(f"Error al conectar con el agente de Azure: {e}")
