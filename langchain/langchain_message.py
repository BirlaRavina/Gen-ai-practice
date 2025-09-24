from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('HUGGINGFACE_API_KEY')
if not api_key:
    raise ValueError("api key is required")
os.environ['HUGGINGFACEHUB_API_TOKEN']  = api_key

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto", 
)

chat_model= ChatHuggingFace(llm = llm)

message = [
    HumanMessage(content = 'how i can take loan'),
    AIMessage(content='you are a AI agent of a Financial Company')
]

res = chat_model.invoke(message)

print(res.content)

