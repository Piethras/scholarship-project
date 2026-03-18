from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv("key.env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
prompt = ChatPromptTemplate.from_template("Answer this question: {question}")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({"question": "What is a large language model in one paragraph?"})
print(response)