with open(
    "data/ai_notes.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()
print("Orginal text in the test document:\n",text)

chunk_size=100
chunks = [
    text[i:i+chunk_size]
    for i in range(
        0,
        len(text),
        chunk_size
    )
]

for idx,chunk in enumerate(chunks):
    print(f"\nChunk {idx+1}:\n{chunk}\n")
    
import chromadb
from click import prompt
from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()

documents = chunks

client = chromadb.Client()

collection = client.create_collection(name="Documents")

collection.add(
    documents=documents,
    ids = [f"doc{i}" for i in range(len(documents))]
)

query = input(
    "Ask a question: "
)
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