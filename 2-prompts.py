from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import FewShotPromptTemplate

# Prompt calling method-1
# Create a prompt template with an input variable "topic"
template = "Write a short poerm about {topic}."

# Create a PromptTemplate object using the template and specifying the input variable
prompt = PromptTemplate(input_variables=["topic"], template=template)

# Format the prompt by providing a value for the input variable "topic"
final_prompt = prompt.format(topic="the moon")
print(final_prompt)

# pass the input variable as a dictionary to the invoke method
final_prompt = prompt.invoke({"topic": "the sun"})
print(final_prompt)

# Using from_template to create a PromptTemplate object directly from the template string
prompt = PromptTemplate.from_template(template )
final_prompt = prompt.invoke({"topic": "the stars"})
print(final_prompt)

# prompt using multiple input variables
template = """
Translate the following text to {language}:
"{text}"
"""
prompt = PromptTemplate(input_variables=["language", "text"], template=template)
final_prompt = prompt.format(language="French", text="Hello, how are you?")
print(final_prompt)


# Prompt calling method-2
# prompt using chatprompttemplate 

# openai api messages-langchain messages
# system-system
# user-human
# assistant-ai

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates English to {language}."),
        ("human", "Translate the following text to {language}: '{text}'"),
    ]
)   

final_prompt = chat_template.format_messages(text="Hello, how are you?",language="Spanish")
print(final_prompt)

# Prompt calling method-3
# Few shot prompts usisng fewShotPromptTemplate
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
]

example_prompt = PromptTemplate(input_variables=["input", "output"], template="The antonym of {input} is {output}.")

few_shot_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Here are some examples of antonyms:",
    suffix="What is the antonym of {input}?",
    input_variables=["input"],
)

final_prompt = few_shot_template.format(input="big")
print(final_prompt)

llm = ChatOpenAI(model="gpt-5.5", temperature=0)

chain = few_shot_template | llm
response = chain.invoke({"input": "big"})
print("final response:"+response.content)



