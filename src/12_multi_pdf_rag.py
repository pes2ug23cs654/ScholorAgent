import os 
from langchain_community.document_loaders import PyPDFLoader

documents = []

folder_path = "data/"

for file in os.listdir(folder_path):
    
    if file.endswith(".pdf"):
        loader = PyPDFLoader(
            os.path.join(folder_path,file)
        )
        
        docs = loader.load()
        
        documents.extend(docs)

print(
    "Total Pages: ",len(documents)
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

from langchain_chroma import Chroma

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings    
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

query = input("\nAsk a question: ")
docs = retriever.invoke(query)
print("\nRetrieved Chunks:\n")

for i, doc in enumerate(docs):
    print(f"\nChunk {i+1}")
    print("-" * 50)
    print(doc.page_content[:300])
    
context = "\n\n".join(
    [doc.page_content for doc in docs]
)

prompt = f"""
You are a research assistant.

Answer the question using only the provided context.

If the answer is not present in the context,say:
"I could not find the answer in the retrieved context."

Context:
{context}

Question:
{query}
"""

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt
)

print("\nAnswer:\n")
print(response.text)

print("\nSources\n")

for doc in docs:
    print(
        f"Page: {doc.metadata.get('page')} | "
        f"Source: {doc.metadata.get('source')}"
    )

        