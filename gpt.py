import openai
import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants
API_DOCS_URL = "https://docs.streamlit.io/library/api-reference"

# No necesitas recuperar la clave API aquí
# OPENAI_API_KEY = st.secrets["openai"]["OPENAI_API_KEY"]  

# Crea el objeto client sin pasar la clave API
client = openai.OpenAI() 

def initialize_conversation():
    """
    Initialize the conversation history with system and assistant messages.

    Returns:
    - list: Initialized conversation history.
    """
    assistant_message = "Hello! How can I assist you today?"

    conversation_history = [
        {"role": "system", "content": "You are a helpful and informative AI assistant."},
        {"role": "system", "content": "You were created by OpenAI and trained on a massive dataset."},
        {"role": "system", "content": "Refer to conversation history to provide context to your response."},
        {"role": "assistant", "content": assistant_message}
    ]
    return conversation_history

def get_chat_response(user_input, conversation_history):
    """
    Gets a response from the OpenAI API.

    Parameters:
    - user_input (str): The user's input.
    - conversation_history (list): The current conversation history.

    Returns:
    - str: The AI's response.
    """
    conversation_history.append({"role": "user", "content": user_input})

    try:
        model_engine = "gpt-4o-mini"
        response = client.chat.completions.create(
            model=model_engine,
            messages=conversation_history
        )
        assistant_reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply
    except OpenAIError as e:
        logging.error(f"Error occurred: {e}")
        return f"Error: {str(e)}"

def main():
    """
    Main function to handle chat interactions.
    """
    conversation_history = initialize_conversation()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = get_chat_response(user_input, conversation_history)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
