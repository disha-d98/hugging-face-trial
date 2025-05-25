print("Hello Hugging Face")

from huggingface_hub import InferenceClient
from constants import HUGGINGFACE_API_TOKEN

client = InferenceClient(
    api_key=HUGGINGFACE_API_TOKEN,
)

result = client.zero_shot_classification(
    "house of spirits",
    model="facebook/bart-large-mnli",
    candidate_labels=["Fiction", "Non Fiction", "Poetry"],
)

print(result)
