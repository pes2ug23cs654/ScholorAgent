## What is StateGraph?

StateGraph is the main workflow class in LangGraph.
It manages the execution of nodes while passing a shared state between them.

## Why is State Shared?
Instead of passing many variables between nodes,langgraph stores everything in one shared state.

## Why don't nodes pass parameters?
Nodes use the state which already contains everything required for the execution which makes the ndoes loosely coupled and addition of new fields would be easy.Hence,Nodes read and update the shared state instead of passing many arguments.

## What does START mean?
START is the predefined entry point of a LangGraph,It tells the graph where execution begins.

## What does END mean?
END is the predefined exit point of the graph.It marks the completion of execution.When execution reaches end,LangGraph return the final state.

## What is compile()?
Compile converts the graph definition into an executable application.

## What is invoke()?
invoke() runs the compiled graph with an initial state.

