import requests
from dotenv import load_dotenv
import os
load_dotenv()


API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

if not API_TOKEN:
    raise ValueError("HUGGINGFACE_API_KEY not found in .env")
print("API KEY LOADED:", bool(API_TOKEN))

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    print("STATUS CODE:", response.status_code)
    print("RESPONSE TEXT:", response.text)  # Show the actual response
    
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        raise ValueError("Response is not JSON. Something went wrong.")


data = query({
    "inputs": "Once upon a time,",
    "parameters": {"max_length": 50}
})

print(data)