from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.output_parsers import JsonOutputParser

llm = ChatOpenAI(model="gpt-5.5")

# Method-1 Ouput parser with string output
prompt = ChatPromptTemplate.from_template("name 3 cities starting with '{letter}'")
prompt_text = prompt.format(letter="p")

parser = StrOutputParser()

response = llm.invoke(prompt_text)

result = parser.parse(response)
print(result)
print(result.content)
print(type(result.content))


# Method-2 Ouput parser with chaining and stringoutputparser
prompt = ChatPromptTemplate.from_template("name 3 cities starting with '{letter}'")
prompt_text = prompt.format(letter="p")

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke(prompt_text)
print("raw response:")
print(response)
print(type(response))

# method-2 CommaSeparatedListOutputParser
list_parser = CommaSeparatedListOutputParser()
format_instructions = list_parser.get_format_instructions()
print(format_instructions)

list_prompt = ChatPromptTemplate.from_template("List 3 {item_type}. \n\n{format_instructions}")
print(list_prompt)

list_prompt_partial = list_prompt.partial(format_instructions=format_instructions)
print(list_prompt_partial)

list_chain = list_prompt_partial | llm | list_parser

result_list = list_chain.invoke({"item_type":"unique ai models"})
print("List output ")
print(result_list)

# Method-3 json output parser with get_format_instructions



