from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

# Simple PromptTemplate with a single input variable
template = "Write a short poem about {topic}."

# Build the prompt template
prompt = PromptTemplate(input_variables=["topic"], template=template)

# Format it by filling in the input variable
final_prompt = prompt.format(topic="the moon")
print(final_prompt)

# Alternatively, pass inputs as a dict via .invoke()
final_prompt = prompt.invoke({"topic": "the sun"})
print(final_prompt)

# Simple ChatPromptTemplate with system + human messages
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a friendly assistant who answers concisely."),
        ("human", "{question}"),
    ]
)

final_prompt = chat_template.format_messages(question="What is the capital of France?")
print(final_prompt)
