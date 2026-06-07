from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq()
completion = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[
      {
        "role": "user",
        "content": "What is python?"
      }
    ],
    temperature=1,
)

for chunk in completion:
    print(completion.choices[0].message.content)
