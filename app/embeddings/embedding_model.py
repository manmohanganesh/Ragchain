from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import Config

def get_embedding_model():
    embeddings = GoogleGenerativeAIEmbeddings(
        model=Config.EMBEDDING_MODEL,
        google_api_key=Config.GOOGLE_API_KEY
    )
    return embeddings