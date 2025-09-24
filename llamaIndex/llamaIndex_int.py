# worked with open api

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface import HuggingFaceLLM
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('HUGGINGFACE_API_KEY')
if not api_key:
    raise ValueError("api key is required")
os.environ['HIGGINGFACEHUB_API_TOKEN'] = api_key


documents = SimpleDirectoryReader('data').load_data()

llm = HuggingFaceLLM(
    model_name="tiiuae/falcon-7b-instruct",  # you can use llama-2, mistral, etc.
    tokenizer_name="tiiuae/falcon-7b-instruct",
    context_window=4096,
    max_new_tokens=512,
    generate_kwargs={"temperature": 0.7, "do_sample": True},
    device_map="auto",   # for local GPU usage
)

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(llm=llm)

responce = query_engine.query("explain modulfrom llama_index.llms.huggingface import HuggingFaceLLLMe 1")

print(responce)
