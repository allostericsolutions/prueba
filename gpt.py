import streamlit as st
import openai

# Configurar la API key de OpenAI con los secretos de Streamlit
openai.api_key = st.secrets["my_proud"]["openai_api_key"]

def generar_respuesta(prompt):
    """Genera una respuesta de GPT-4."""
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

# Interfaz de Streamlit
st.title("Prueba sencilla de GPT-4")

# Crea el widget st.text_area una sola vez
prompt = st.text_area("Introduce tu pregunta o instrucción:") 

if st.button("Generar respuesta"):
    if prompt:
        respuesta = generar_respuesta(prompt)
        st.write("**Respuesta:**", respuesta)
    else:
        st.warning("Por favor, introduce una pregunta o instrucción.")
