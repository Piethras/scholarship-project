from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv
load_dotenv("key.env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful study assistant."),
    MessagesPlaceholder(variable_name="history"),  # past messages go here
    ("human", "{input}")
])

chain = prompt | model | parser

# Turn 1 (no history yet)
response1 = chain.invoke({"history": [], "input": "What is Python?"})
print("AI:", response1)

# Turn 2 (pass Turn 1 as history) 
response2 = chain.invoke({
    "history": [
        HumanMessage(content="What is Python?"),
        AIMessage(content=response1)
    ],
    "input": "What can I build with it?"
})
print("AI:", response2)

# Turn 3 (pass Turns 1 & 2 as history)
response3 = chain.invoke({
    "history": [
        HumanMessage(content="What is Python?"),
        AIMessage(content=response1),
        HumanMessage(content="What can I build with it?"),
        AIMessage(content=response2)
    ],
    "input": "How long does it take to learn?"
})
print("AI:", response3)