# Understanding Prompt-Based AI Chatbots

## How This Project Works
This project builds an AI chatbot that generates structured responses using **LangChain** and **Hugging Face models**. It allows users to:
- **Create and use structured prompts** to guide AI responses.
- **Interact with the chatbot** through a command-line or a web interface.
- **Store and retrieve past conversations** for better context.
- **Use open-source language models** to generate responses without relying on proprietary solutions.

The chatbot is designed in **a structured manner**, and each file plays a role in different aspects of its functionality. Below is the **step-by-step explanation** of each file in a logical sequence for easy understanding.

---

## Step-by-Step Explanation of Files

### **1. Defining and Managing Prompts**
#### `template.json`
- This is a **predefined prompt template** that structures AI-generated summaries.
- It includes placeholders like `{paper}`, `{style}`, and `{length}` to guide the AI in producing the correct output.
- The AI fills these placeholders dynamically when generating responses.

#### `prompt_generator.py`
- This script **creates and saves** the `template.json` dynamically.
- It uses `PromptTemplate` to define a structured way for the AI to generate responses.
- Running this file ensures that the chatbot has a well-defined format for responses.

---

### **2. Handling Conversations & Messages**
#### `chat_prompt_template.py`
- Demonstrates how **ChatPromptTemplate** works.
- Uses placeholders `{domain}` and `{topic}` to generate **domain-specific** responses.
- This file helps in creating **customized responses** for different knowledge areas.

#### `messages.py`
- Uses **SystemMessage, HumanMessage, and AIMessage** to structure chatbot conversations.
- Helps format interactions in a structured manner, ensuring clarity and logical response generation.
- This is useful for chatbots where well-structured conversations are required.

---

### **3. Implementing the Chatbot in Different Modes**
#### `chatbot_history.py`
- Implements a **basic chatbot** in the command line.
- Allows users to type messages and receive AI-generated responses.
- Maintains a **chat history list**, allowing responses to be context-aware.

#### `chatbot_messages.py`
- Enhances the chatbot using structured messages like `SystemMessage`, `HumanMessage`, and `AIMessage`.
- Ensures that the AI understands its role (assistant) and provides structured responses.
- Useful when **context retention** is necessary for a conversation.

#### `chatbot_static.py`
- A **simplified chatbot** that runs in the command line.
- It does not store past interactions, making it suitable for simple one-time queries.
- Ideal for **quick testing of AI responses** without maintaining memory.

---

### **4. Creating an Interactive Chatbot Interface**
#### `chatbot_ui.py`
- Uses **Streamlit** to create a **web-based chatbot UI**.
- Allows users to interact with the chatbot through an easy-to-use interface.
- Maintains **session-based chat history**, so users can see past conversations.
- Best for **interactive chatbot deployment**.

---

### **5. Managing Chat History & Memory**
#### `chat_history.txt`
- Stores past **user queries and AI responses**.
- This helps in improving response relevance based on prior interactions.
- It acts as a simple memory storage for the chatbot.

#### `message_placeholder.py`
- Reads chat history from `chat_history.txt` and **dynamically integrates past messages** into new queries.
- Uses `MessagesPlaceholder` to structure conversations based on history.
- This allows AI to generate context-aware responses.

---

### **6. Setting Up API Keys and Environment Variables**
#### Creating a `.env` File
- The chatbot uses API keys and environment variables for authentication.
- Create a `.env` file in the project directory and add:
  ```sh
  HUGGINGFACE_API_KEY=your_api_key_here
  ```
- The `.env` file is automatically loaded by the chatbot scripts to authenticate API requests.

---

## How to Run the Project
### Running the CLI Chatbot
```sh
python chatbot_history.py
```

### Running the Streamlit Web Chatbot
```sh
streamlit run chatbot_ui.py
```

---

## Next Steps for Learning
- Modify `template.json` to experiment with different prompt structures.
- Replace the Hugging Face model in `chatbot_messages.py` to explore different AI capabilities.
- Expand prompt templates to **handle multiple tasks** beyond summarization.

## Future Improvements
- Integrate **OpenAI GPT models** for improved response quality.
- Expand chatbot functionality to **handle different user intents and topics**.


