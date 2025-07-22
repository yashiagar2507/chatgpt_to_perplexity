import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def summarize_text(text, api_key=None):
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing OpenAI API Key")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this conversation:\n\n{text}"
            }
        ],
        max_tokens=500,
        temperature=0.5,
    )
    return response.choices[0].message.content
