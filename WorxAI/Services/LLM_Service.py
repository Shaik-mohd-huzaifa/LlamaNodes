import os
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


class LLM:
    def __init__(self, model, max_token, temperature):
        self.model = model
        self.max_token = max_token or 3000
        self.temperature = temperature or 0

    def get_llm(self):
        # Using Together Inference
        return ChatOpenAI(
            base_url=os.getenv("TOGETHER_INFERENCE_ENDPOINT"),
            api_key=os.getenv("TOGETHER_INFERENC_API_KEY"),
            max_tokens=self.max_token,
            temperature=self.temperature,
            model=self.model,
        )
