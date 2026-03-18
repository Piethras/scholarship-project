from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional translator."),
    ("human", "Translate this text into {language}: {text}")
])

# Translate into French
result1 = prompt.format_messages(text="Good morning, how are you?", language="French")
print(result1)

# Translate into Cameroonian Pidgin English
result2 = prompt.format_messages(text="Good morning, how are you?", language="Cameroonian Pidgin English")
print(result2)