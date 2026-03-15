from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from config import Config

def get_qa_chain():
   prompt_template = """
    You are a helpful assistant that answers questions based on the provided context.

    Use only the information from the context to answer the question.

    If the answer is not present in the context, say:
    "The answer is not available in the provided documents."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
   prompt = PromptTemplate(
    template=prompt_template,
    input_variables=['context','question']
    )
   
   llm = ChatGoogleGenerativeAI(
   model=Config.LLM_MODEL,
   google_api_key=Config.GOOGLE_API_KEY,
   temperature =0.3)

   chain = prompt | llm
   return chain
