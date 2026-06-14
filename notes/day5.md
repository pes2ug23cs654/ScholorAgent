## What is chunking?
Chunking is the process of breaking a large document into smaller meaningful pieces before creating embeddings. These chunks are stored in a vector database, allowing the retrieval system to find only the relevant parts of a document instead of searching the entire document at once.
## Why can't we embed an entire book?
Embedding an entire book into a single vector causes loss of retrieval granularity. When a user asks a question about one specific topic, the system retrieves the entire book instead of the relevant section, leading to inefficient retrieval, increased token usage, and lower answer quality.

## What happens if chunks are too large>
Large chunks may contain a lot of irrelevant information. Even if the chunk contains the answer, the LLM receives extra context, which increases token usage, retrieval noise, latency, and can reduce answer accuracy.

## What happens if chunks are too small?
Very small chunks may lose important context because sentences or ideas get split across multiple chunks. As a result, the retrieved chunk may not contain enough information for the LLM to generate a correct answer.
