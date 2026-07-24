from typing import TypedDict

class GraphState(TypedDict):
    query:str
    rewritten_query:str
    query_type:str
    context:str
    answer:str
    sources:list
    need_web:bool
    chat_history:list
    last_tool: str
    tool_status: str
    execution_time: float
    error: str