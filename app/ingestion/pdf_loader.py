from PyPDF2 import PdfReader
from langchain_core.documents import Document

def load_pdfs(uploaded_files):
    '''
    This will convert the uploaded PDF files from streamlit into langchain document objects.
    '''
    documents=[]
    for uploaded_file in uploaded_files:
        pdf_reader =PdfReader(uploaded_file) #(uploaded_file)
        for page_number, page in enumerate(pdf_reader.pages):
            text=page.extract_text()
            if text: 
                document=Document(
                    page_content=text,
                    metadata={
                        "source":uploaded_file.name,
                        "page":page_number+1,
                    },
                )
                documents.append(document)
    return documents