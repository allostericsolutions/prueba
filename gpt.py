import streamlit as st
import openai

# Salvaguardar contra secretos faltantes
if "my_proud" in st.secrets and "openai_api_key" in st.secrets["my_proud"]:
    openai.api_key = st.secrets["my_proud"]["openai_api_key"]
else:
    st.error("OpenAI API key is missing from secrets.")
    st.stop()  # Detener ejecución si la clave está faltando

# Probar la clave API haciendo una solicitud simple
def test_api_key():
    try:
        prompt = "You are a helpful assistant. User: Hello, how are you? Assistant:"
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=5,  # Respuesta simple
        )
        return response.choices[0].text.strip()

    except Exception as e:  # Manejo de excepciones
        return f"Error en la API de OpenAI: {e}"

# Interfaz de Streamlit
st.title("Prueba de API Key de OpenAI")

if st.button("Probar API Key"):
    respuesta = test_api_key()
    st.write("**Respuesta del API:**", respuesta)
