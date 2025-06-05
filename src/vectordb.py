from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


"""
    Load PDF file 
"""

DATA_PATH = "data"

               
def load_pdf(data_path):
    loader = DirectoryLoader(
        data_path,
        glob = "*.pdf", 
        loader_cls = PyPDFLoader    
    )
    
    docs = loader.load()
    return docs

docs = load_pdf(DATA_PATH)


def create_chunk(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50,
    )
    
    text_chunk = text_splitter.split_documents(extracted_data)
    
    return text_chunk

text_chunk = create_chunk(docs)

def get_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    
    return embeddings

embedding_model = get_embeddings()

# FAISS Vectorstore

vector_db = FAISS.from_documents(text_chunk, embedding_model)
vector_db.save_local("faiss_db")
    
    
    
    


    