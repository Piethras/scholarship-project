from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv("key.env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

def ask_ai(role, question):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful {role}."),
        ("human", "{question}")
    ])
    chain = prompt | model | parser
    return chain.invoke({"role": role, "question": question})

print(ask_ai("doctor",  "What are the symptoms of malaria?"))
print(ask_ai("lawyer",  "What should I do if I steal a contract?"))
print(ask_ai("teacher", "How do I stay focused while studying?"))