from typing import TypedDict

class GraphState(TypedDict):
    query:str
    tool:str
    rewritten_query:str
    context:str
    answer:str
    sources:list
    