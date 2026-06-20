from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (RecursiveCharacterTextSplitter)

loader = PyPDFLoader("data/attention_is_all_you_need.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)

chunks = splitter.split_documents(documents)

print("Number of chunks:", len(chunks))
print("\nChunk 0 metadata:", chunks[0].metadata)
print("\nChunk 0 content:", chunks[0].page_content[:500])
