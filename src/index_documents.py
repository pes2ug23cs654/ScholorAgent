from langchain_community.document_loaders import PyPDFLoader
import os
from langchain_chroma import Chroma
import shutil
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


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


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap = 100
)

chunks = splitter.split_documents(documents)


embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


if os.path.exists("chroma_db"):
    shutil.rmtree("chroma_db")
vectorstore = Chroma.from_documents(
    documents=chunks,  
    embedding=embeddings,
    persist_directory="chroma_db"
)
