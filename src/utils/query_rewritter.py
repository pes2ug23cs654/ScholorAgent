from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def rewrite_query(query):
    prompt = f"""
You improve search queries.

Rewrite the user's question so it is more specific and clear.

Rules:
- Do not change the meaning.
- Make it clearer.
- Do not answer the question.
- Return only the rewritten query.

User question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
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
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()