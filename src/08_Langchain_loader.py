from langchain_community.document_loaders import PyPDFLoader
"""
    Load a PDF file and extract its documents.
    The PyPDFLoader class is used to load a PDF file and extract its documents.
    A Document loader is Langchain's way of loading data from various sources. It abstracts away the details of how the data is loaded and provides a consistent interface for accessing the data.
    Source                           Loader
    PDF                              PyPDFLoader
    Text                              TextLoader 
    CSV                               CSVLoader
    Website                           WebBaseLoader
    Directory                          DirectoryLoader
    The load method of the PyPDFLoader class returns a list of Document objects, where each Document object represents a page in the PDF file. Each Document object has two attributes: page_content and metadata. The page_content attribute contains the text content of the page, while the metadata attribute contains information about the page, such as its page number.
    Loaders are like convert raw files into Langchain's Document format, which is a standardized format that can be used by other components of the Langchain framework, such as vector stores and retrievers.
    """
loader = PyPDFLoader("data/attention_is_all_you_need.pdf") 
"""
The above code creates an object that knows where the PDF file is located and how to extract its content. The load method is then called to actually load the PDF file and extract its documents.
"""

documents = loader.load()
" This is where the pdf is actually loaded"
print("Pages:",len(documents))

print("\nMetadata:")
print(documents[0].metadata)

print("\nFirst 500 Character:")
print(documents[0].page_content[:500])