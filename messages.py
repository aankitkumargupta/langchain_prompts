from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the Hugging Face model
llm = HuggingFaceEndpoint(repo_id="Qwen/QwQ-32B", task="text-generation")

# Create the chat model
model = ChatHuggingFace(llm=llm)

# Initialize messages list (FIXED COMMA ERROR)
messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Everest"),
]

# Get AI response
result = model.invoke(messages)

# Append AI response to messages list
messages.append(AIMessage(content=result.content))

# Print conversation history
print(messages)
