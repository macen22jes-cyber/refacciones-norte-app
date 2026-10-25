from openai import AzureOpenAI
import streamlit as st

# Configuración de la interfaz
st.set_page_config(
    page_title="Refacciones del Norte - Asistente IA", page_icon=""
)
st.title("Refacciones del Norte")
st.caption("Asistente Virtual de Control y Validación de Compras")

# Inicializar cliente de Azure OpenAI directamente con la Clave API
client = AzureOpenAI(
    api_key=st.secrets["AZURE_OPENAI_API_KEY"],
    azure_endpoint=st.secrets["ENDPOINT"],
    api_version="2024-02-15-preview",
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
      response = client.chat.completions.create(
          model="gpt-4o",  # <--- Asegúrate de que este sea exactamente el nombre de tu despliegue en Azure OpenAI
          messages=[
              {
                  "role": "system",
                  "content": (
                      "Eres un asistente virtual de control y validación de"
                      " compras para Refacciones del Norte."
                  ),
              },
              {"role": "user", "content": prompt},
          ],
      )
      reply_text = response.choices[0].message.content
      st.markdown(reply_text)
      st.session_state.messages.append(
          {"role": "assistant", "content": reply_text}
      )
    except Exception as e:
      st.error(f"Error al conectar con la API: {e}")
