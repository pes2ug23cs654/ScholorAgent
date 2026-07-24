from src.utils.query_rewritter import rewrite_query
from src.utils.router import choose_tool
from src.utils.tools_registry import TOOLS
from src.utils.prompt import build_prompt
from src.utils.query_rewritter import rewrite_arxiv_query
from src.utils.llm import ask_llm
from src.utils.context_evaluator import evaluate_context
from src.utils.paper_classifier import classify_paper
from src.utils.memory import (
    load_history,
    save_history,
    trim_history
)
from src.utils.state_helper import update_state

def rewrite_node(state):

    # Step 1: Resolve conversational references
    standalone_query = rewrite_query(
        state["query"],
        state["chat_history"]
    )

    # Step 2: Convert to arXiv keywords if needed
    if state["query_type"] == "paper":
        state["rewritten_query"] = rewrite_arxiv_query(
            standalone_query
        )
    else:
        state["rewritten_query"] = standalone_query

    print(f"✓ {state['rewritten_query']}")

    return state

def knowledge_search_node(state):
    result = TOOLS["pdf"](
        state["rewritten_query"]
    )
    state = update_state(state, result)
    print(f"✓ Retrieved {len(state['sources'])} sources")
    return state

def web_node(state):
    result = TOOLS["web"](state["rewritten_query"])
    print(f"✓ Retrieved {len(result['sources'])} web sources")
    return update_state(state, result,merge=True)


def arxiv_node(state):
    result = TOOLS["arxiv"](
        state["rewritten_query"]
    )
    state = update_state(state, result)
    print(f"✓ Retrieved {len(state['sources'])} papers")
    return state

def answer_node(state):
    if not state["context"]:
            state["answer"] = (
            "I couldn't retrieve information from my knowledge sources. "
            "Please try again later or rephrase your question."
            )
            return state
    prompt = build_prompt(
        state["context"],
        state["query"],
        chat_history = state["chat_history"]
    )
    state["answer"]=ask_llm(prompt)
    history = load_history(state)
    history.append(
        ("User", state["query"]),
    )
    history.append(
        ("Assistant", state["answer"])
    )
    history = trim_history(history)
    save_history(state, history)
    print(f"💾 Memory Updated ({len(history)} messages)")
    print("✓ Response generated")
    return state


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

def memory_node(state):
    print("\n💾 Memory Management")

    history = load_history(state)
    state["chat_history"] = history

    print(f"✓ Loaded {len(history)} chat history entries")

    return state

