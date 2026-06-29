from langchain_chroma import Chroma
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from google import genai
from dotenv import load_dotenv

def retrieve(query):
    docs = retriever.invoke(query)
    return docs

if not os.path.exists("chroma_db"):
    print("Vector Database not found. Please run 'index_documents.py' first to create the vector database.")
    exit()
import time

start = time.time()   

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

collection = vectorstore.get()

print(
    f"Indexed Chunks: {len(collection['ids'])}"
) 

print(
    f"Database loaded in {time.time()-start:.2f} sec"
)

retriever = vectorstore.as_retriever(
   search_type="mmr", #Maximal Marginal Relevance
   search_kwargs={
       "k":5,
       "fetch_k":10
   }
)


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
print("=" * 60)
print("📚 ScholarAgent - Research Paper Assistant")
print("Type 'exit' to quit.")
print("=" * 60)
while True:   
   
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting...")
        break
    docs = retrieve(query)

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}")
        print("-" * 50)
        print(doc.page_content[:300])
        print(
            f"Page: {doc.metadata.get('page')} | "
            f"Source: {doc.metadata.get('source')}"
        )
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
        You are ScholarAgent, an AI Research Assistant.

        Rules:

        1. Use ONLY the retrieved context.

        2. Never fabricate information.

        3. If context is insufficient,
           say so clearly.

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
            model = "gemini-2.5-flash",
            contents = prompt
        )
    
        print("\nAssistant:\n")
        print(response.text)
    except Exception as e:
        print("Error generating response:", )
        print(e)

    sources = set()

    for doc in docs:
        sources.add(
            (
            os.path.basename(
                doc.metadata["source"]
            ),
            doc.metadata["page"]
            )
        )

    print("\nSources:")

    for i,(source,page) in enumerate(sources, start=1):
        print(f"({i}). {source} (Page {page})")
    

