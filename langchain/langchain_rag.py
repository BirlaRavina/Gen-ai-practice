import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('HUGGINGFACE_API_KEY')
os.environ['HUGGINGFACEHUB_API_TOKEN'] = api_key

# load document
loader = PyPDFLoader('Python.pdf')
documents = loader.load()

# split documents in chunks
text_spliter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
chunks = text_spliter.split_documents(documents)

# intialize embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# store embedding chunks  in vector database
vectorstores = Chroma.from_documents(chunks, embeddings)

# define llm model
llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-R1-0528',
    task= 'conversational'
)

chat_model = ChatHuggingFace(llm = llm) 

# retrieve data from vector store
retriever = vectorstores.as_retriever()

prompt_template = PromptTemplate.from_template(
    """Answer the question based on the below context:\n\n{context}\n\nQuestion: {input}"""
)
combine_docs_chain = create_stuff_documents_chain(
    llm = chat_model, 
    prompt = prompt_template
)

qa_chain = create_retrieval_chain(
    retriever,
    combine_docs_chain
)

query = "What is the main topic in module 4 in this document"
response = qa_chain.invoke({'input': query})
print(response['answer'])
