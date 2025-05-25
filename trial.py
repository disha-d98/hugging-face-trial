print("Hello Hugging Face")

from constants import HUGGINGFACE_API_TOKEN
import requests

# Set your Hugging Face API token
api_token = HUGGINGFACE_API_TOKEN

#API_URL
API_URL = "https://router.huggingface.co/hyperbolic/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_response(prompt):
    return query({
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "model": "deepseek-ai/DeepSeek-R1"
})

def process_response(response):
    content = response["choices"][0]["message"]["content"]

    # extracting thought process
    thought_start = content.index("<think>") 
    thought_end = content.index("</think>") 
    thought = content[thought_start + len("</think>") :thought_end]

    answer = content[thought_end + len("</think>"):]

    return answer, thought

# user_input = "Hello, what's your name?"
# response = get_response(user_input)
# print(response)

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = get_response(user_input)
    answer, thought = process_response(response)

    print("Chatbot:", answer)
    print("Thought:", thought)