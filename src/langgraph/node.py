from src.utils.query_rewritter import rewrite_query
from src.utils.router import choose_tool
from src.utils.tools_registry import TOOLS
from src.utils.prompt import build_prompt
from src.utils.query_rewritter import rewrite_arxiv_query
from src.utils.llm import ask_llm
from src.utils.context_evaluator import evaluate_context
from src.utils.paper_classifier import classify_paper
def rewrite_node(state):
    if state["query_type"] == "paper":
        state["rewritten_query"] = rewrite_arxiv_query(state["query"])
    else:
        state["rewritten_query"] = rewrite_query(state["query"])

    print(f"✓ {state['rewritten_query']}")
    return state

def router_node(state):
    state["tool"] = choose_tool(state["rewritten_query"])
    print(f"✓ Tool Selected: {state['tool']}")
    return state

def knowledge_search_node(state):
    result = TOOLS["pdf"](
        state["rewritten_query"]
    )
    state["context"]=result["context"]
    state["sources"]=result["sources"]
    print(f"✓ Retrieved {len(state['sources'])} sources")
    return state
def remove_duplicates(sources):

    seen = set()
    unique = []

    for source in sources:

        key = source["url"]

        if key not in seen:
            seen.add(key)
            unique.append(source)

    return unique

def web_node(state):

    pdf_context = state.get("context", "")
    pdf_sources = state.get("sources", [])

    result = TOOLS["web"](state["rewritten_query"])

    state["context"] = f"""
========== LOCAL DOCUMENTS ==========
{pdf_context}

========== WEB SEARCH ==========
{result["context"]}
"""

    state["sources"] = remove_duplicates(
        pdf_sources + result["sources"]
    )

    print(f"✓ Retrieved {len(result['sources'])} web sources")

    return state

def arxiv_node(state):
    query = rewrite_arxiv_query(state["query"])
    result = TOOLS["arxiv"](
        query
    )
    state["context"]=result["context"]
    state["sources"]=result["sources"]
    print(f"✓ Retrieved {len(state['sources'])} papers")
    return state

def answer_node(state):
    prompt = build_prompt(
        state["context"],
        state["query"]
    )
    state["answer"]=ask_llm(prompt)
    print("✓ Response generated")
    return state

def route(state):
    return state["tool"]

def check_context(state):

    if state["need_web"]:
        return "web"

    return "answer"
def check_query_type(state):
    return state["query_type"]

def paper_request_node(state):
    print("\n📄 Paper Request")
    query = state["query"]
    state["query_type"] = classify_paper(query)
    print("\n✓ Paper type classified as:", state["query_type"])
    return state

def evaluate_context_node(state):

    print("\n🧠 Evaluate Context")

    query = state["query"]
    context = state.get("context", "")

    decision = evaluate_context(query, context)

    if decision == "YES":
        state["need_web"] = False
        print("✓ Context sufficient")

    else:
        state["need_web"] = True
        print("⚠ Context insufficient")

    return state