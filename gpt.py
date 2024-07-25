import streamlit as st
import openai

# safeguard against missing secrets
if "my_proud" in st.secrets and "openai_api_key" in st.secrets["my_proud"]:
    openai.api_key = st.secrets["my_proud"]["openai_api_key"]
else:
    st.error("OpenAI API key is missing from secrets.")
    st.stop()  # stop execution if the key is missing

# test api key by making a simple request
def test_api_key():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, how are you?"}  # sample prompt
            ],
            max_tokens=5,  # simple response
        )
        return response.choices[0].message['content'].strip()

    except Exception as e:  # Corrected exception handling
        return f"Error en la API de OpenAI: {e}"

# streamlit interface
st.title("Prueba de API Key de OpenAI")

if st.button("Probar API Key"):
    respuesta = test_api_key()
    st.write("**Respuesta del API:**", respuesta)
