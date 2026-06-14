## How do we read a pdf in python?

We can use libraries such as pypdf to load a PDF and extract text page by page. The extracted text can then be processed, chunked, embedded, and stored for retrieval.

## What is a document loader?
A document loader is a component that reads documents from different formats such as PDF, TXT, DOCX, HTML, or Excel files and converts them into a format that can be processed by an AI pipeline.
## Why do we chunk PDFs?
We chunk PDFs because embedding an entire document into a single vector reduces retrieval precision. Chunking allows us to retrieve only the relevant sections, reducing token usage and improving answer quality.
## What challenges can Pdf create?
PDFs can create challenges such as:

Poor text extraction
Broken formatting
Tables and figures being lost
Scanned PDFs requiring OCR
Chunking without losing context