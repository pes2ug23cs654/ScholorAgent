import chromadb
from click import prompt
from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()

documents = [
    "Python is a programing language",
    "Embeddings convert the text into vectors",
    "Vector databases store embeddings",
    "RAG combines retrieval and generation",
    "Langchain helps build LLM applications"
]

client = chromadb.Client()

collection = client.create_collection(name="Documents")

collection.add(
    documents=documents,
    ids = [f"doc{i}" for i in range(len(documents))]
)

query = "how does langchain work and help build LLM applications?"

results = collection.query(
    query_texts=[query],
    n_results=2
)

print("Retrieved Documents:")
print(results["documents"])

context = "\n".join(
    results["documents"][0]
)


    
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{query}
"""
response = client.models.generate_content(
    model="gemini-2.5-flash",   
    contents=prompt
)

print("\nAnswer:\n",response.text)