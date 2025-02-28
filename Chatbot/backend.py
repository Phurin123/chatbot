import os
import bs4
import getpass
from transformers import pipeline

def response(user_query):
    # Initialize the pipeline
    pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")

    # Prepare the message
    messages = [{"role": "user", "content": user_query}]

    # Generate the response
    response = pipe(messages)

    return response[0]['generated_text']