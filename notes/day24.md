## What is LangGraph?

LangGraph is a framework for building stateful, multi-step AI agents and workflows. It lets you connect LLMs, tools, and custom functions as a graph, where the agent can make decisions, call multiple tools, and maintain state throughout the execution.

## What is a node?

A node is an individual unit of work in the graph. It can be an LLM call, a tool, a Python function, or any operation that processes the current state.

## What is an edge?

An edge is a connection between nodes that defines how execution moves from one node to another. Edges can be fixed or conditional based on the current state.

## What is a state?

A state is a shared data container that stores information throughout the workflow. Each node reads from the state, updates it, and passes the updated state to the next node.

## Why is LangGraph useful?
Builds multi-step AI agents instead of single LLM calls.
Manages shared state across multiple nodes.
Supports conditional routing and decision-making.
Makes it easy to integrate multiple tools (RAG, web search, calculators, databases, APIs, etc.).
Prevents complex agent logic from becoming messy by organizing it as a graph.
Supports loops, retries, and human-in-the-loop workflows.
Makes agent workflows easier to debug, extend, and maintain.