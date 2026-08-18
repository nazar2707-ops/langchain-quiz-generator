from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutPutParser

#loading enviromental variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

#intialize LLM
llm = ChatGoogleGenerativeAi(model="gemini-1.5-flash", api_key=api_key)

print("LLM initialized successfully!")