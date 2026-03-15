import os
from dotenv import load_dotenv

#Load environment variable from .env
load_dotenv()  

class Config:
    '''
    Central configuration for the RAG system
    '''
    #API Keys
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    #LLM Configuration
    LLM_MODEL = 'models/gemini-2.5-flash'
    
    #Embedding model
    EMBEDDING_MODEL = "models/gemini-embedding-001"
    #Text Splitting
    CHUNK_SIZE=1000
    CHUNK_OVERLAP=200

    #Vector Store
    VECTOR_DB_PATH = 'faiss_index'
