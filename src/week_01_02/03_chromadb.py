import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="documents"
)

documents = [
    "Pythhon is a programming Language",
    "Machine learning uses algorithms",
    "Deep learning uses neural networks",
    "vector databases store embeddings",
    "RAG combines retrieval and generation"
]

collection.add(
    documents=documents,
    ids=[f"doc{i}" for i in range(len(documents))]
)

print("Documents added successfully!")

results = collection.query(
    query_texts=['tell me about databases'],
    n_results=2
)

print("\nresults:")
print(results["documents"])