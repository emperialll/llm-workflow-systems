import os
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

def create_openai_client() -> OpenAI:
    load_dotenv(find_dotenv())
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

    return OpenAI(api_key=api_key)