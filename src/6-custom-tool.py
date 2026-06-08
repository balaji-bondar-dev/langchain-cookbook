from langchain_core.tools import tool

@tool
def string_length_tool(text: str) -> int:
    """
        Useful for when you need to know the number of characters in a string.
    """
    return len(text)

# The tool is now ready to be passed to an agent
response = string_length_tool.invoke("Balaji")
print("Final Response : ")
print(response)

print(string_length_tool.name)
print(string_length_tool.description)



