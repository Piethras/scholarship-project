from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} as if I am a complete beginner."
)

messages = prompt.format_messages(topic="Artificial Intelligence")
print(messages)