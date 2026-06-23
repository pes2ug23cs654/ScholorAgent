from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/attention_is_all_you_need.pdf")

documents = loader.load()

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(
    documents
)

from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "all-MiniLM-L6-v2"
)

from langchain_chroma import Chroma

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k":3}
)

def ask_question(query):
    docs = retriever.invoke(query)

    print("\nRetrieved Chunks:\n")

    for doc in docs:
        print(doc.metadata)
        print(doc.page_content[:200])
        print("-" * 50)

ask_question(
    "What problem does Transformer solve?"
)