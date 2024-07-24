   st.title("Prueba sencilla de GPT-3.5 Turbo")

   prompt = st.text_area("Introduce tu pregunta o instrucción:")
   if st.button("Generar respuesta"):
       if prompt:
           respuesta = generar_respuesta(prompt)
           st.write("**Respuesta:**", respuesta)
       else:
           st.warning("Por favor, introduce una pregunta o instrucción.")import streamlit as st
import openai

headers = {
    "authorization": st.secrets["my_proud"],
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
  return response.choices[0].message['content']

# Interfaz de Streamlit
st.title("Prueba sencilla de GPT-3.5 Turbo")

prompt = st.text_area("Introduce tu pregunta o instrucción:")
if st.button("Generar respuesta"):
  if prompt:
    respuesta = generar_respuesta(prompt)
    st.write("**Respuesta:**", respuesta)
  else:
    st.warning("Por favor, introduce una pregunta o instrucción.")
