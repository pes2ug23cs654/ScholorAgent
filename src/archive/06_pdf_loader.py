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
try:
    client.delete_collection("Documents")
except:
    pass

collection = client.create_collection(
    name="Documents"
)
metadatas = []

for i, chunk_size in enumerate(chunks):
    metadatas.append(
        {
            "source": "attention_is_all_you_need.pdf",
            "chunk": i,
        }
    )
collection.add(
    documents=chunks,
    ids=[
         f"Attention_chunk{i}"
         for i in range(len(chunks))
        ],
    metadatas=metadatas
)
query = input("\nAsk a question:\n")
results = collection.query(
    query_texts=[query],
    n_results=3
)

print("Retrieved Documents:")
print(results["metadatas"])

context = "\n".join(
    results["documents"][0] 
)
client1 = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
prompt = f"""
You are a research assistant.

Answer the question only using the provided context.

If the answer cannot be found in the context,
say:
"I could not find the answer in the provided context."

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
print("\nSources:")
for metadata in results["metadatas"][0]:
    print(metadata)