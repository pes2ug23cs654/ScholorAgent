import os
import sys
import time

from dotenv import load_dotenv
from google import genai

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from tools.web_search import web_search

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("GEMINI_API_KEY not found in .env file.")
    sys.exit()

client = genai.Client(api_key=api_key)

if not os.path.exists("chroma_db"):
    print("Vector Database not found.")
    print("Please run 'index_documents.py' first.")
    sys.exit()

start = time.time()

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

collection = vectorstore.get()

print(f"Indexed Chunks: {len(collection['ids'])}")
print(f"Database loaded in {time.time() - start:.2f} sec")


retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 10
    }
)


def retrieve(query):
    return retriever.invoke(query)



print("=" * 60)
print("📚 ScholarAgent - Research Paper Assistant")
print("Type 'exit' to quit.")
print("=" * 60)

while True:
    choice = input(
    "Choose Search Mode:\n"
    "1. Web Search\n"
    "2. Local PDF Search\n\n"
    "Enter choice: "
)
    if choice == "1":
        results = web_search(query = input("\nYou: "))
        print(results)


    elif choice != "2":
        print("Invalid choice.")
        sys.exit()

    query = input("\nYou: ").strip()

    if query.lower() in ["exit", "quit"]:
        print("Exiting ScholarAgent...")
        break

    docs = retrieve(query)

    if not docs:
        print("\nNo relevant documents found.")
        continue

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(docs, start=1):
        print(f"\nChunk {i}")
        print("-" * 50)
        print(doc.page_content[:300])
        print(
            f"Page: {doc.metadata.get('page')} | "
            f"Source: {doc.metadata.get('source')}"
        )

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are ScholarAgent, an AI Research Assistant.

Rules:
1. Use ONLY the retrieved context.
2. Never fabricate information.
3. If the context is insufficient, clearly say so.
4. Explain concepts in beginner-friendly language.
5. Use bullet points.
6. Give examples whenever appropriate.
7. End with a short summary.

Context:
{context}

Question:
{query}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\nAssistant:\n")
        print(response.text)

    except Exception as e:
        print("\nError generating response:")
        print(e)
        continue

    sources = {
        (
            os.path.basename(doc.metadata["source"]),
            doc.metadata["page"]
        )
        for doc in docs
    }

    print("\nSources:")

    for i, (source, page) in enumerate(sorted(sources), start=1):
        print(f"({i}) {source} (Page {page})")