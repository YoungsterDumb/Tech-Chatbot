import os 
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"

def load_llm(huggingface_repo_id):
    llm = HuggingFaceEndpoint(
        endpoint_url=f"https://api-inference.huggingface.co/models/{huggingface_repo_id}",
        huggingfacehub_api_token = HUGGINGFACE_API_KEY,
        temperature = 0.1,
        max_new_tokens = 512,
    )
    return llm

llm = load_llm(HUGGINGFACE_REPO_ID)