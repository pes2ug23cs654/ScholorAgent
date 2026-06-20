## What is Langchain?

Langchain is a framework that helps to build applications using llms by providing tools such as Document Loaders,Text Splitters,Embedding Models,Vector Databases,Retrieval Systems,Chains and agents.

## What does PyPdfLoader do?
Reads a PDF file and converts into a Langchain Document Objects.

Each page in a pdf becomes one document and langchain stores page_content and metadata of each document.

## What does a RecursiveCharacterTextSplitter do?

This breaks large texts into smaller chunks,i.e,it's one of the chunking strategies and it's called recursive because it tries to split intelligently based on paragraphs,lines,sentences,spaces,characters instead of cutting words randomly.

## What is chunk overlap?
It's a way to preserve context  in the chunks by copying x characters from previous chunk to the next chunk.

