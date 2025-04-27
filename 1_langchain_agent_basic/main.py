from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from dotenv import load_dotenv

if __name__ == "__main__":
    print("Welcome to Langchain !!")

    load_dotenv()

import src.demo_001_langchain

# import src.agents.linkedin_lookup_agent
