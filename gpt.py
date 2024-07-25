import streamlit as st
import openai

# Safeguard against missing secrets
if "my_proud" in st.secrets and "openai_api_key" in st.secrets["my_proud"]:
    openai.api_key = st.secrets["my_proud"]["openai_api_key"]
else:
    st.error("OpenAI API key is missing from secrets.")
    st.stop()  # Stop execution if the key is missing

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

    except openai.error.OpenAIError as e:  # Corrected class name
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
