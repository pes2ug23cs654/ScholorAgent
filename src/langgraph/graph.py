from langgraph.graph import StateGraph
from langgraph.graph import START, END

from src.langgraph.state import GraphState
from src.utils.source_formatter import format_sources
from src.langgraph.node import (
    paper_request_node,
    rewrite_node,
    knowledge_search_node,
    web_node,
    arxiv_node,
    answer_node,
    evaluate_context_node,
    check_query_type,
    check_context,
    memory_node
)

graph = StateGraph(GraphState)
graph.add_node("paper_request",paper_request_node)
graph.add_node("rewrite", rewrite_node)
graph.add_node("knowledge_search", knowledge_search_node)
graph.add_node("evaluate_context", evaluate_context_node)
graph.add_node("web", web_node)
graph.add_node("arxiv", arxiv_node)
graph.add_node("answer", answer_node)
graph.add_node("memory",memory_node)
graph.add_edge(
    START,
    "memory"
)
graph.add_edge(
    "memory",
    "paper_request"
)

graph.add_edge(
    "paper_request",
    "rewrite"
)

graph.add_conditional_edges(
    "rewrite",
    check_query_type,
    {
        "paper": "arxiv",
        "normal": "knowledge_search"
    }
)

graph.add_edge(
    "knowledge_search",
    "evaluate_context"
)

graph.add_conditional_edges(
    "evaluate_context",
    check_context,
    {
        "web": "web",
        "answer": "answer"
    }
)

graph.add_edge(
    "web",
    "answer"
)

graph.add_edge(
    "arxiv",
    "answer"
)

graph.add_edge(
    "answer",
    END
)

app = graph.compile()

if __name__ == "__main__":
    chat_history = []
    while True:

        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        result = app.invoke(
            {
                "query": query,
                "chat_history": chat_history
            }
        )

        print("\nAssistant:")
        print(result["answer"])
        chat_history = result["chat_history"]
        print("\n📚 Sources")
        print(format_sources(result["sources"]))