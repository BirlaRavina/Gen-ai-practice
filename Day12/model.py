import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Your Hugging Face API Key
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

if not API_KEY:
    raise ValueError("HUGGINGFACE_API_KEY not found in .env")
print("API KEY LOADED:", bool(API_KEY)) 
model = "gpt2"

prompt = "Once upon a time"

API_URL = f"https://api-inference.huggingface.co/models/{model}"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 50,
        "temperature": 0.7
    }
}

response = requests.post(API_URL, headers=headers, json=payload, timeout=30)

if response.status_code == 200:
    generated_text = response.json()[0]['generated_text']
    print("Generated Text:\n", generated_text)
else:
    print("Error:", response.status_code, response.text)
