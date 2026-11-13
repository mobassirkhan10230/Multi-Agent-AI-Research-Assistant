import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


def create_llm():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing from .env")

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
        api_key=api_key
    )

    return llm