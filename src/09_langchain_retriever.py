from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name = "all-MiniLM-L6-v2"
)

loader = PyPDFLoader("data/attention_is_all_you_need.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(
    documents
)

vectorstore = Chroma.from_documents(
    documents = chunks,
    embedding = embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs = {"k": 3}
)

query = "What problem does the Transformer solve?"

results = retriever.invoke(query)

for doc in results:
    print(doc.page_content[:300])
    print(doc.metadata)


