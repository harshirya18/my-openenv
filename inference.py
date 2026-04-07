import os
import requests

API_BASE_URL = os.getenv("API_BASE_URL", "https://api-inference.huggingface.co/models")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt2")
HF_TOKEN = os.getenv("HF_TOKEN")  # no default

headers = {}
if HF_TOKEN:
    headers["Authorization"] = f"Bearer {HF_TOKEN}"


def query(payload):
    response = requests.post(
        f"{API_BASE_URL}/{MODEL_NAME}",
        headers=headers,
        json=payload,
    )
    return response.json()


def predict(prompt: str):
    return query({"inputs": prompt})


if __name__ == "__main__":
    print(predict("Hello"))
