import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5.5")


config = Config()