## What is an LLM router?
An LLM router is a component that uses a Large Language Model to decide which tool, workflow, or data source should handle a user's request. Instead of answering the question itself, it analyzes the query and routes it to the most appropriate tool.

## Why is an LLM better than keyword matching?
An LLM understands the meaning and intent behind a user's query rather than relying on exact keywords. This allows it to handle paraphrased questions, synonyms, and more complex requests, making routing much more accurate and flexible than simple keyword matching.

## Why should the router return structured output?
Returning structured output (such as JSON or predefined labels) makes the routing process reliable, predictable, and easy to parse programmatically. It also simplifies debugging, logging, and integrating the router with other components of the system.

## Why shouldn't router answer the question?
The router's responsibility is only to determine which tool or workflow should handle the request. The selected tool has the necessary knowledge or capabilities to generate the actual response. Keeping these responsibilities separate makes the system more modular, maintainable, and scalable.
## What happens if the router chooses the wrong tool?
If the router selects the wrong tool, the system may produce incorrect, incomplete, or irrelevant answers. This reduces response quality, increases unnecessary computation, and can lower the user's trust in the system. Therefore, accurate routing is essential for reliable AI agents.