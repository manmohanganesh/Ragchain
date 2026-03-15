from langchain_community.vectorstores import FAISS
from embeddings.embedding_model import get_embedding_model
from config import Config

def create_vector_store(documents):
    """
    Creates a FAISS vector store from document chunks and saves it locally.
    """
    embeddings = get_embedding_model()
    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )
    vector_store.save_local(Config.VECTOR_DB_PATH)

    return vector_store

def load_vector_store():
    """
    Loads the FAISS vector store from the disk
    """
    embeddings= get_embedding_model()
    vector_store=FAISS.load_local(
        Config.VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store 