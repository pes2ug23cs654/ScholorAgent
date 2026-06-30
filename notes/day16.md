## What is a tool?
A tool is a function or capability that an AI agent uses to interact with the outside world, perform actions, or retrieve external information.
## Why do AI agents need tools?
LLMs alone have limitations such as no real-time knowledge, poor mathematical accuracy, no access to external systems, and no ability to perform actions. Tools overcome these limitations by enabling agents to retrieve live data, execute computations, access databases, and interact with APIs.
## Why do we represent tools as Python functions?
Python functions provide a simple and structured way to define actions. They have well-defined inputs, processing logic, and outputs, making them easy for AI frameworks to call and manage.
## What are the inputs and outputs of a tool?
Input: The information or parameters required for the tool to perform its task (such as a query, file path, or numerical value).
Output: The result produced by the tool after executing the requested action, which is returned to the AI agent.
## How does a tool differ from an LLM?
A tool performs specific actions or retrieves external information, while an LLM is responsible for reasoning and generating natural language. The LLM decides when to use a tool, and the tool executes the requested action and returns the result.