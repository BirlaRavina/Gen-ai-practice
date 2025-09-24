from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv
import os
import torch

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not API_KEY:
    raise ValueError("HUGGINGFACE_API_KEY not found in .env")
print("API KEY LOADED:", bool(API_KEY)) 

model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

tokenizer = AutoTokenizer.from_pretrained(model, token = API_KEY)
model = AutoModelForCausalLM.from_pretrained(model, torch_type = torch.float16, device_map="auto", token=API_KEY)

prompt = "### Instruction:\nExplain how neural networks work.\n\n### Response:"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(output[0], skip_special_tokens=True))
