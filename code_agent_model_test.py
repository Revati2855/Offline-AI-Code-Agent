
from llama_cpp import Llama

MODEL_PATH = "local_models/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf"

print("Loading local AI model... Please wait.")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4,
    verbose=False
)

print("Model loaded successfully!")

response = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python coding assistant."
        },
        {
            "role": "user",
            "content": "Write a simple Python program to add two numbers."
        }
    ],
    max_tokens=200,
    temperature=0.2
)

print("\nAI Response:\n")
print(response["choices"][0]["message"]["content"])
