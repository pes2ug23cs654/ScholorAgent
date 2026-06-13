## What is chunking?
Chunking is a process or technique of breaking down a large document into smaller chunks and these chunks are stored in the vector dbs after embedding and retrieval is optimised due to chunking.

## Why can't we embed an entire book?
If we embed an enitre book and store it in the db when we need only a part of the book or only one page we end up loading enitre book as its embedded into a single vector.

## What happens if chunks are too large>
If chunks are too large we may end up retireving unnecessary data which are not used and may end up taking more space and time.

## What happens if chunks are too small?

If chunks are too small it may not contain an enitre sentence or the context required to understand the meaning and may break the sentences in middle leading to meaning-less content.
