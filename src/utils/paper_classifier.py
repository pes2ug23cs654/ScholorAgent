def classify_paper(query):
    query = query.lower()

    paper_keywords = [
        "paper",
        "papers",
        "research",
        "survey",
        "publication",
        "publications",
        "arxiv",
    ]

    if any(keyword in query for keyword in paper_keywords):
        return "paper"

    return "normal"