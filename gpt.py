import streamlit as st
import openai

# Uncomment to see contents of secrets (remove or comment out in production)
# st.write(st.secrets)

# Configure the OpenAI API key with Streamlit secrets
try:
    openai.api_key = st.secrets["my_proud"]["openai_api_key"]
except KeyError:
    st.error("Missing OpenAI API key in secrets.")
    st.stop()  # Stop further execution if the key is missing

def generar_respuesta(prompt):
    """Genera una respuesta de GPT-4."""
    try:
        response = openai.ChatCompletion.create(  # Correct method name
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()

    except openai.error.OpenAIError as e:  # Use proper casing for OpenAIError
        return f"Error en la API de OpenAI: {e}"

# Streamlit interface
st.title("Prueba sencilla de GPT-4")

prompt = st.text_area("Introduce tu pregunta o instrucción:")

if st.button("Generar respuesta"):
    if prompt:
        respuesta = generar_respuesta(prompt)
        st.write("**Respuesta:**", respuesta)
    else:
        st.warning("Por favor, introduce una pregunta o instrucción.")
