from src.utils.config import MAX_HISTORY

def load_history(state):
    return state.get("chat_history", [])

def save_history(state, history):
    state["chat_history"] = history
    return state

def trim_history(history):
    if len(history) > MAX_HISTORY:
        return history[-MAX_HISTORY:]
    return history