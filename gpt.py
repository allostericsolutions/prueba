import streamlit as st
import openai

# Safeguard against missing secrets
if "my_proud" in st.secrets and "openai_api_key" in st.secrets["my_proud"]:
    openai.api_key = st.secrets["my_proud"]["openai_api_key"]
else:
    st.error("OpenAI API key is missing from secrets.")
    st.stop()  # Stop execution if the key is missing

# Test API key by making a simple request
def test_api_key():
    try:
        response = openai.ChatCompletion.create(  # Updated method call
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, how are you?"}  # Sample prompt
            ],
            max_tokens=5,  # Simple response
        )
        return response.choices[0].message['content'].strip()

    except Exception as e:  # Catch all exceptions for simplicity
        return f"Error en la API de OpenAI: {e}"

# Streamlit interface
st.title("Prueba de API Key de OpenAI")

if st.button("Probar API Key"):
    respuesta = test_api_key()
    st.write("**Respuesta del API:**", respuesta)
