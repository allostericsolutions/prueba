import streamlit as st
import openai

# Configurar la API key de OpenAI con los secretos de Streamlit
openai.api_key = st.secrets["my_proud"]["openai_api_key"] 

# Configuración de cabeceras HTTPmport streamlit as st
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

prompt = st.text_area("Introduce tu pregunta o instrucción:")
if st.button("Generar respuesta"):
    if prompt:
        respuesta = generar_respuesta(prompt)
        st.write("**Respuesta:**", respuesta)
    else:
        st.warning("Por favor, introduce una pregunta o instrucción.")
headers = {
    "authorization": f"Bearer {st.secrets['my_proud']['openai_api_key']}",  # Formato correcto de autorización
    "content-type": "application/json"
}

def generar_respuesta(prompt):
    """Genera una respuesta de GPT-3.5 Turbo."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

# Interfaz de Streamlit
st.title("Prueba sencilla de GPT-3.5 Turbo")

prompt = st.text_area("Introduce tu pregunta o instrucción:")
if st.button("Generar respuesta"):
    if prompt:
        respuesta = generar_respuesta(prompt)
        st.write("**Respuesta:**", respuesta)
    else:
        st.warning("Por favor, introduce una pregunta o instrucción.")

# Interfaz de Streamlit
st.title("Prueba sencilla de GPT-3.5 Turbo")

prompt = st.text_area("Introduce tu pregunta o instrucción:")
if st.button("Generar respuesta"):
    if prompt:
        respuesta = generar_respuesta(prompt)
        st.write("**Respuesta:**", respuesta)
    else:
        st.warning("Por favor, introduce una pregunta o instrucción.")
