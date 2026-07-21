from typing import TypedDict

class GraphState(TypedDict):
    query:str
    rewritten_query:str
    query_type:str
    context:str
    answer:str
    sources:list
    need_web:bool