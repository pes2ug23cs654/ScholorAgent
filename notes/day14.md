## What is indexing?
Indexing is building the searchable knowledge base where we load the pdfs,chunk,embed and store them in vector db.
## Why do we persist the vector database?
We persist the vector db which allows us to index once and query forever.Instead of indexing the knowledge base every time we run the program we persist the db and load them for querying.
## What is the difference between indexing and querying?
Querying is where we embed only the user's question and search the stored vectors,retrieve the most relevant chunks,and use them to answer.
Whereas,in indexing we build the searchable knowledge base and embed all the data.
## Why is this architecture better than recreating embeddings every run?
It seperates the expensive preprocessing step,i.e,indexing from fast retrieval step,i.e,querying making it much faster and scalable as document collection grows.