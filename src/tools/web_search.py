import os
import time
from src.utils.config import TOP_K
from dotenv import load_dotenv
from tavily import TavilyClient
import streamlit as st
load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    api_key = st.secrets["TAVILY_API_KEY"]

def web_search(query):

    start = time.time()
    try:
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=TOP_K
        )
    except Exception as e:
        return {
            "tool": "web",
            "status": "failed",
            "context": "",
            "sources": [],
            "execution_time": time.time() - start,
            "error": str(e)
        }

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
    execution_time = time.time() - start
    return {
        "tool": "web",
        "status": "success",
        "context": context,
        "sources": sources,
        "execution_time": execution_time
    }
