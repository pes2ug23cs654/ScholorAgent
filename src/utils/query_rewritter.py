from google import genai
from dotenv import load_dotenv
import os
from src.utils.config import MODEL
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def rewrite_query(query, chat_history):
    history_text = ""

    for role, message in chat_history:
        history_text += f"{role}: {message}\n"
    prompt = f"""
You rewrite questions for a Retrieval-Augmented Generation (RAG) system.

Your goal is to convert follow-up questions into standalone questions.

Previous Conversation

{history_text}

Current Question

{query}

Instructions:
- If the current question refers to previous messages using words like:
  - it
  - that
  - they
  - those papers
  - the first one
  - the second model
  resolve the reference using the conversation history.
- Produce a complete standalone question.
- Do not answer the question.
- Keep the original meaning.
- Return ONLY the rewritten question.
"""

    response = client.models.generate_content(
        model = MODEL,
        contents=prompt,
    )

    return response.text.strip()


def rewrite_arxiv_query(query):
    prompt = f"""
You generate search queries for the arXiv API.

Return ONLY a concise keyword query.

Rules:
- Keep only the main technical topic.
- Remove conversational words.
- Remove words like:
  latest
  recent
  paper
  papers
  research
  show me
- Use 2-5 keywords.
- No punctuation.
- No quotes.
- No explanations.

Examples:

Latest transformer papers
→ transformer

Recent papers on multimodal LLMs
→ multimodal large language models

What is RAG?
→ retrieval augmented generation

Research about diffusion models
→ diffusion models

Question:
{query}
"""

    response = client.models.generate_content(
        model = MODEL,
        contents=prompt,
    )

    return response.text.strip()