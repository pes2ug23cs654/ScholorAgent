# Day 28 – Retrieval-First Architecture

## Why is retrieval-first better than routing-first?

A router makes decisions before seeing any evidence. Retrieval-first searches the local knowledge base first and decides whether more information is needed based on the retrieved context. This reduces incorrect routing and improves reliability.

## Why is arXiv treated separately?

arXiv is a specialized source for academic literature. It should only be used when users explicitly ask for research papers or publications, not for conceptual explanations.

## Why rename pdf_node to knowledge_search_node?

The node's responsibility is to search the local knowledge base, not specifically PDFs. This makes the design extensible to future sources such as DOCX, Markdown, CSV, or notes.

## Why evaluate retrieved context before searching the web?

Web search is slower and can introduce noisy or conflicting information. Evaluating the retrieved local context first allows the agent to avoid unnecessary web searches while still falling back when the local knowledge is insufficient.

## Why merge contexts instead of replacing them?

Local documents often provide foundational knowledge, while web search provides recent or supplementary information. Merging both contexts enables the language model to generate richer, more complete, and up-to-date answers.