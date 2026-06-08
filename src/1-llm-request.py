#sample comment updates
import os
import types
from openai import OpenAI
from langchain_openai import ChatOpenAI
#from dotenv import load_dotenv
#load_dotenv()

# You can use the ChatOpenAI class from langchain_openai to make a request to the OpenAI API:
llm = ChatOpenAI(model_name="gpt-5.5")
response = llm.invoke("How much is the addition of 1 and 2?")
print(response.content)
print(type(response))

# Alternatively, you can use the OpenAI client directly using the OpenAI Python SDK:
# Get OpenAI API key from the environment variable and create a client instance
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(openai.api_key)
response = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {"role": "user", "content": "How much is the addition of 1 and 2?"}
    ]
)
print(response.choices[0].message.content)



