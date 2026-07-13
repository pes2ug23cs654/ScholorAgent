import arxiv

def arxiv_search(query):
    client = arxiv.Client()
    print(f"Searching arXiv for: {query}")
    search = arxiv.Search(
        query=query,
        max_results=5,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    context = ""
    sources = []

    for result in client.results(search):

        context += f"""
Title: {result.title}
Authors: {', '.join(a.name for a in result.authors)}
Published: {result.published.date()}
Summary: {result.summary.replace('\n', ' ')[:250]}...
URL: {result.entry_id}

"""

        sources.append({
            "url": result.entry_id,
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "published": str(result.published.date()),
            "summary": result.summary.replace('\n', ' ')
        })

    return {
        "tool": "arxiv",
        "context": context,
        "sources": sources
    }