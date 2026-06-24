## What is multi-document retrieval?

Multi-document retrieval is a RAG technique where information is retrieved from multiple documents stored in the same vector database. Instead of searching a single PDF, the retriever searches across many documents and returns the most relevant chunks regardless of which document they come from.


## Why is multi-document retrieval useful?
Multi-document retrieval is useful because it allows the system to answer questions using information from multiple sources. This improves coverage, reduces missing information, and enables comparisons between documents. For example, a research assistant can search across several research papers instead of only one paper.

## How does the retriever decide which paper to search?
The retriever does not directly choose a paper first. It converts the query into an embedding and compares it with the embeddings of all chunks in the vector database. The chunks with the highest similarity scores are retrieved. The corresponding papers are identified from the metadata attached to those chunks.

## What information in metadata helps identify the source paper?
Metadata stores information about the source document, such as:

File name
Document title
Author
Source path
Page number
Publication date (if available)

This metadata helps us identify which paper and which page a retrieved chunk came from.