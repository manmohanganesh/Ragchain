import streamlit as st
from services.rag_pipeline import process_documents,ask_question

st.set_page_config(page_title="RAG PDF Chatbot")
st.title("RAG PDF Chatbot")
st.write("Upload PDFs and ask questions about them")

uploaded_files = st.file_uploader(
    "Upload your files here",
    type=['pdf'],
    accept_multiple_files=True
)

if st.button("Process Documents"):
    if uploaded_files:
        with st.spinner("Processing your documents.."):
            process_documents(uploaded_files)
        st.success("Documents processed successfully!")
    else:
        st.warning("Please upload at least one PDF.")
    
question=st.text_input("Ask any question related to the document(s) uploaded")

if question:
    with st.spinner("Generating answer..."):
        answer, sources, retrieval_score, context_length, answer_quality = ask_question(question)

    st.write("### Answer")
    st.write(answer)

    st.write("### Sources")
    for source in sources:
        st.write(source)
    
    st.write("### Evaluation metrics")
    st.write(f"Retrieval Score:{retrieval_score:.2f}")
    st.write(f"Context Length:{context_length}")
    st.write(f"Answer Quality : {answer_quality}")