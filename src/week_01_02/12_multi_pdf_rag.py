import os 
from langchain_community.document_loaders import PyPDFLoader

documents = []

folder_path = "data/"

for file in os.listdir(folder_path):
    print(f"Loading {file}...")
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


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

while True:   
    print("=" * 60)
    print("📚 ScholarAgent - Research Paper Assistant")
    print("Type 'exit' to quit.")
    print("=" * 60)
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting...")
        break
    docs = retriever.invoke(query)

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
        You are an AI Research Assistant.
    
        Use only the retrieved context.
    
        If information is missing,
        say that the context is insufficient to answer the question.
    
        Explain the concepts in beginner-friendly terms, and provide examples where possible.
    
        Use bullet points whenever possible, and provide a summary at the end.
    
        Do not invent information or make assumptions. If the answer is not in the context, say "The context is insufficient to answer the question."
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

    for source, page in sources:
        print(f"{source} (Page {page})")
    

        