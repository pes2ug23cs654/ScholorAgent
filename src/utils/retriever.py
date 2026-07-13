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
    docs =  retriever.invoke(query)
    context = "\n\n".join(
        doc.page_content for doc in docs
    )
    sources = [
        {
            "title": doc.metadata.get("source"),
            "url": f"Page {doc.metadata.get('page', 'Unknown')}"
        }
        for doc in docs
    ]
    return {
        "tool":"pdf",
        "context": context,
        "sources": sources
    }
    