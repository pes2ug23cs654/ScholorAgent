## What is a vector database?
A vector database stores embeddings and allows us to search for similar vectors efficiently
## Why not use SQL?
Sql is based on keywords and embeddings allows model to understand the context and not only keywords
## What problem doees chromdb solve?
chromdb stores embeddings permanently instead of RAM and uses indexing methods to quickly find the nearest vectors and also allows us to store metadata along with the vector and this allows us to retrieve relevant chunks.It automates the manual work of finding the cosine similarity between the vectors and is efficient for large input data or documents.
## How does retrieval work?
firtsly it stores the documents and generates embeddings which are stored in vector dbs like chromadb and user asks questions which are again converted to embeddings and similarity search is done on these embeddings and sends the retrieved context to LLM.