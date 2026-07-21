from src.tools.web_search import web_search
from src.tools.arxiv_search import arxiv_search
from src.utils.retriever import retrieve

TOOLS = {
    "pdf": retrieve,
    "web": web_search,
    "arxiv": arxiv_search
}