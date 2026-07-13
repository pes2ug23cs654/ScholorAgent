from tools.arxiv_search import arxiv_search

papers = arxiv_search(
    "Retrieval-Augmented Generation"
)

for paper in papers:
    print("-"*50)
    print(f"Title: {paper['title']}")
    print(f"Authors: {', '.join(paper['authors'])}")
    print(f"Published: {paper['published']}")
    print(f"Summary: {paper['summary']}")
    print(f"URL: {paper['url']}\n")

# Web search example (uncomment to test)
# from tools.web_search import web_search

# result = web_search("Latest LangGraph updates")

# print(result["context"])

# print(result["sources"])