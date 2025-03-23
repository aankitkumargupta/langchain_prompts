from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer supprot agent"),
        # message placeholder to get old messages
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),  # current query by user
    ]
)


chat_history = []

# load chat history
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt

prompt = chat_template.invoke(
    {"chat_history": chat_history, "query": "where is my order?"}
)
print(prompt)
