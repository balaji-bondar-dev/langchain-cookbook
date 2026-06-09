#from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

file_path = "python-file.md"

# 1. Read the file content
with open(file_path, "r", encoding="utf-8") as f:
    file_content = f.read()

# 2. Create the Document object
doc = Document(
    page_content=file_content, 
    metadata={"source": file_path}
)

# Verify the result
print(f"Document content length: {len(doc.page_content)} characters")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)
splits = text_splitter.split_documents([doc])

print(f"Data split in to {len(splits)} chunks.")
print("Example chunk ",splits[0].page_content)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = Chroma(
    embedding_function= embeddings,
    collection_name= "dsa_data", #name your collection
    persist_directory= "chroma-db",
)

vector_store.add_documents(splits)
print("Vector Store created succesfully.")

retriever = vector_store.as_retriever(search_kwargs={"k":1})
test_query = "what is Python Interpreter?"
results = retriever.invoke(test_query)

print("test_query "+test_query)
print("result length",len(results))

for index,result in enumerate[Document](results) :
    print("-"*75)
    print(result.page_content)

