from ingestion.pdf_loader import load_pdfs
from ingestion.text_splitter import split_documents
from vectorstore.faiss_store import create_vector_store,load_vector_store
from chains.qa_chain import get_qa_chain
from utils.logger import get_logger

logger = get_logger(__name__)

def process_documents(uploaded_files):
    """
    Handles the document ingestion pipeline.
    """
    logger.info("Starting document processing")
    #1.Loading the PDFs
    documents = load_pdfs(uploaded_files)
    logger.info(f"Loaded{len(documents)} pages")
    #2. Split documents into chunks
    split_docs=split_documents(documents)
    logger.info(f"Created {len(split_docs)} chunks")

    #3. Create vector store
    vector_store=create_vector_store(split_docs)
    logger.info("Vector store created successfully")
    return vector_store

def ask_question(question):
    logger.info(f"Received question:{question}")
    #1 Load the vector
    vector_store=load_vector_store()

    #2. Retrieve similar documents
    retriever = vector_store.as_retriever(
        search_kwargs={'k':4}
    )

    #3.Get QA Chain
    docs = retriever.invoke(question)
    logger.info(f"Retrieved {len(docs)} relevant chunks")
    #4.Generate answer
    chain = get_qa_chain()

    #Combine retrieved context
    context = "\n\n".join([doc.page_content for doc in docs])

    #4.Generating answer
    response = chain.invoke({
        "context":context,
        "question":question
    })

    answer=response.content
    sources=[]
    for doc in docs:
        source=doc.metadata.get("source")
        page=doc.metadata.get('page')
        sources.append(f"{source} - page {page}")

    sources = list(set(sources))

    return answer, sources