from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import FAISS
from src.load_llm import llm 
from src.prompt_temp import prompt
from src.vectordb import embedding_model
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_FAISS_PATH = "faiss_db"

db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization = True )

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm = llm, 
    chain_type = "stuff",
    retriever = db.as_retriever(search_kwargs = {"k": 3}),
    return_source_documents = True,
    chain_type_kwargs = {"prompt": prompt}
)






