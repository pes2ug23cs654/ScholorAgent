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

    state["last_tool"] = result["tool"]
    state["tool_status"] = result["status"]
    state["execution_time"] = result["execution_time"]

    if result["status"] != "success":
        return state

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