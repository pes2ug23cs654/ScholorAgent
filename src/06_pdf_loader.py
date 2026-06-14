from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai
import os
import chromadb

load_dotenv()

client = chromadb.Client()
reader = PdfReader("data/attention_is_all_you_need.pdf")

text = ""

for page in reader.pages:
    text+= page.extract_text()

#print(text[:1000])

chunk_size = 500

chunks = [
    text[i:i+chunk_size]
    for i in range(
        0,
        len(text),
        chunk_size
    )
]

documents = chunks
collection = client.create_collection(name="Documents")
collection.add(documents=documents, ids=[f"doc{i}" for i in range(len(documents))])
query = input("\nAsk a question:\n")
results = collection.query(
    query_texts=[query],
    n_results=3
)

print("Retrieved Documents:")
print(results["documents"])

context = "\n".join(
    results["documents"][0] 
)
client1 = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
prompt = f"""
Answer using only the context below.

Context:
{context}

Question:
{query}
"""

response = client1.models.generate_content(
    model="gemini-2.5-flash",   
    contents=prompt
)

print("\nAnswer:\n",response.text)