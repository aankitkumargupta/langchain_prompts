import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the Hugging Face model
llm = HuggingFaceEndpoint(repo_id="Qwen/QwQ-32B", task="text-generation")

# Create the chat model
model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.title("AI Chatbot with Hugging Face")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.chat_message("user").write(user_input)

    # Get AI response
    result = model.invoke(user_input)
    response = result.content

    # Display AI response
    st.chat_message("assistant").write(response)

    # Save conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response})
