import time

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load persisted Chroma database
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# Create MMR retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 10
    }
)

# Retrieve relevant documents
def retrieve(query):
    start = time.time()
    try:
        docs =  retriever.invoke(query)
    except Exception as e:
        print(f"Error occurred while retrieving documents: {e}")
        return {
            "tool":"pdf",
            "status":"failed",
            "context": "",
            "sources": [],
            "execution_time": time.time() - start,
            "error": str(e)
        }
    context = "\n\n".join(
        doc.page_content for doc in docs
    )
    sources = [
        {
            "title": doc.metadata.get("source"),
            "url": None
        }
        for doc in docs
    ]
    execution_time = time.time() - start
    return {
        "tool":"pdf",
        "status":"success",
        "context": context,
        "sources": sources,
        "execution_time": execution_time
    }

    