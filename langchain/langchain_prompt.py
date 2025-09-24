import os
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('HUGGINGFACE_API_KEY')
if not api_key:
    raise ValueError("Api key is required")
os.environ['HUGGINGFACEHUB_API_TOKEN'] = api_key

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-R1-0528",
    task= 'conversational',
    max_new_tokens= 100,
    top_k= None,
    top_p= .6,
    temperature= .2
)  

model = ChatHuggingFace(llm = llm)

question = 'solve (3*6)/2'
template = """ Question: {question}
            Answer: Explain step by step        
            """
prompt = PromptTemplate.from_template(template)

llm_chain = prompt | model

# or use instead 
# llm_chain = LLMChain(
#     prompt = prompt, 
#     llm = model
# )
result = llm_chain.invoke({'question': question})
print(result.content)