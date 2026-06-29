## What is a similarity search?

Similarity search is a retrieval technique that finds and returns the document chunks whose embeddings are most similar to the embedding of the user's query.

## What is MMR retrieval?

MMR (Maximal Marginal Relevance) is a retrieval technique that balances relevance and diversity. It selects chunks that are relevant to the query while avoiding redundant or highly similar chunks, providing the LLM with a broader range of useful information.

## Why isn't a higher k always better?

A higher k retrieves more chunks, but it can also introduce irrelevant or redundant information. This increases the amount of context the LLM must process, which may reduce answer quality, increase latency, and consume more tokens.

## What is fetch_k?

fetch_k is used in MMR retrieval. It specifies how many of the most similar chunks are initially retrieved before MMR selects the final k diverse and relevant chunks.

fetch_k = 10 → Retrieve the top 10 most similar chunks.
k = 5 → From those 10, MMR chooses the best 5 by balancing relevance and diversity.

## Why do we retrieve multiple chunks?

Retrieving multiple chunks provides the LLM with more context than a single chunk. Information relevant to a question may be spread across different parts of one or more documents, so multiple chunks help the LLM generate more accurate, complete, and well-supported answers.