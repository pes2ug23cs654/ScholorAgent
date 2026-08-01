import time

import arxiv

from src.utils.config import TOP_K

def arxiv_search(query):
    start = time.time()
    client = arxiv.Client()
    print(f"Searching arXiv for: {query}")
    try:
        search = arxiv.Search(
            query=query,
            max_results=TOP_K,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
 
        context = ""
        sources = []

        for result in client.results(search):
            summary = result.summary.replace("\n", " ")

            context += f"""
Title: {result.title}
Authors: {', '.join(a.name for a in result.authors)}
Published: {result.published.date()}
Summary: {summary[:400]}
URL: {result.entry_id}

"""

            sources.append({
            "url": result.entry_id,
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "published": str(result.published.date()),
            "summary": summary
        })
    except Exception as e:
         return {
                "tool": "arxiv",
                "status": "failed",
                "context": "",
                "sources": [],
                "execution_time": time.time() - start,
                "error": str(e)
            }
    return {
        "tool": "arxiv",
        "status": "success",
        "context": context,
        "sources": sources,
        "execution_time": time.time() - start
    }