import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load environment and token
load_dotenv()
token = os.getenv("HF_TOKEN")

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3.1", token=token)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-V3.1", token=token)
model.to("cuda" if torch.cuda.is_available() else "cpu")

# Prepare conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the FIFA World Cup in 2018?"}
]
inputs = tokenizer.apply_chat_template(
    messages, thinking=False, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

# Generate response
outputs = model.generate(**inputs, max_new_tokens=50)
response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

print("Assistant:", response)
