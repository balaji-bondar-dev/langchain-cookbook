import os
import types
from openai import OpenAI
from langchain_openai import ChatOpenAI

openai = ChatOpenAI(model_name="gpt-5.5")
print(type(openai))

response = openai.invoke("What is the capital of France?")
print(response.content)


