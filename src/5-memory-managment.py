from dotenv import load_dotenv
from langsmith import uuid7
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
#from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# This is the modern, non-deprecated way to handle transient chat history
# history = InMemoryChatMessageHistory()
# history.add_user_message("Hello!")
# print(history)

load_dotenv()

# llm = ChatOpenAI(model="gpt-5.5")
# response = llm.invoke("what is python language?")
# print("Test LLM Response: ")
# print(response.content)

store = {}

# Fetch Session History
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
            
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant"),
        MessagesPlaceholder(variable_name="history"),
        ("human","{input}"),
    ]
)
#print("final prompt: ")
#print(prompt)

chain = prompt | ChatOpenAI(model="gpt-5.5")
#print("chain")
#print(chain)

with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key = "input",
    history_messages_key = "history",
)
#print("with_message_history")
#print(with_message_history)

id = uuid7()

while True:
    print("-"*80)
    user_input = input("Enter : ")
    if user_input.lower() in ["exit","quit"]:
        print("Thanks for contacting us.Take care.")
        break

    response: AIMessage = with_message_history.invoke(
        {"input":user_input},
        config={
                    "configurable":{"session_id":id},
               },
    )
    print(response.content)    