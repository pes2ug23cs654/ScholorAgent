import os
import time

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def web_search(query):

    start = time.time()

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    context_parts = []
    sources = []

    for i, result in enumerate(response["results"], 1):

        # Clean + trim content
        content = result["content"].replace("\n", " ").strip()
        content = content[:400]  # limit size

        block = f"""
[{i}] {result['title']}
Summary: {content}
Source: {result['url']}
"""

        context_parts.append(block)

        sources.append({
            "id": i,
            "title": result["title"],
            "url": result["url"]
        })

    context = "\n\n".join(context_parts)

    return {
        "tool": "web",
        "context": context,
        "sources": sources,
        "execution_time": time.time() - start
    }