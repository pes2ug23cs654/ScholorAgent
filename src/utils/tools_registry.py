from tools.web_search import web_search
from tools.arxiv_search import arxiv_search
from utils.retriever import retrieve

TOOLS = {
    "pdf": retrieve,
    "web": web_search,
    "arxiv": arxiv_search
}