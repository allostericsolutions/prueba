import streamlit as st
import openai

# Imprimir los contenidos de los secretos para verificar (quitar en producción)
st.write(st.secrets)

# Configurar la API key de OpenAI con los secretos de Streamlit
openai.api_key = st.secrets["my_proud"]["openai_api_key"]

def generar_respuesta(prompt):
    """Genera una respuesta de GPT-4."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    
    except openai.error.OpenAIError as e:
        return f"Error en la API de OpenAI: {e}"

# Interfaz de Streamlit
st.title("Prueba sencilla de GPT-4")

prompt = st.text_area("Introduce tu pregunta o instrucción:")

if st.button("Generar respuesta"):
    if prompt:
        respuesta = generar_respuesta(prompt)
        st.write("**Respuesta:**", respuesta)
    else:
        st.warning("Por favor, introduce una pregunta o instrucción.")
