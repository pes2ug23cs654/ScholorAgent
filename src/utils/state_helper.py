def remove_duplicates(sources):

    seen = set()
    unique = []

    for source in sources:

        key = source["url"]

        if key not in seen:
            seen.add(key)
            unique.append(source)

    return unique


def update_state(state, result, merge=False):

    # -------------------------
    # Tool Information
    # -------------------------
    state["last_tool"] = result["tool"]
    state["tool_status"] = result["status"]
    state["execution_time"] = result["execution_time"]

    # -------------------------
    # Execution Timeline
    # -------------------------
    steps = state.get("execution_steps", [])

    tool_names = {
        "pdf": "📄 PDF Search",
        "web": "🌐 Web Search",
        "arxiv": "📚 arXiv Search"
    }

    steps.append(tool_names.get(result["tool"], result["tool"]))

    state["execution_steps"] = steps

    # -------------------------
    # Error Handling
    # -------------------------
    if result["status"] != "success":
        return state

    # -------------------------
    # Context
    # -------------------------
    if merge:

        state["context"] = f"""
========== LOCAL DOCUMENTS ==========
{state.get("context", "")}

========== WEB SEARCH ==========
{result["context"]}
"""

        state["sources"] = remove_duplicates(
            state.get("sources", []) + result["sources"]
        )

    else:

        state["context"] = result["context"]
        state["sources"] = result["sources"]

    return state