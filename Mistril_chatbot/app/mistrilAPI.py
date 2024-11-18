# Use a pipeline as a high-level helper
from transformers import pipeline

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# print(pipe(messages))

def queryModel(message:list) -> str:
    pipe = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B", device='cuda')
    response = pipe(message)
    return response[0]['generated_text'][1]['content']