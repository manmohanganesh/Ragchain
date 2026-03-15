from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import Config

def split_documents(documents):
    '''
    This method will split the documents into smaller chunks for better retrieval and context awarenes.
    '''
    text_splitter= RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP)
    
    split_docs=text_splitter.split_documents(documents)
    return split_docs