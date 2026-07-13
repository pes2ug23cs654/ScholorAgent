from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

def rewrite_query(query,tool=None):
    if tool == "arxiv":
        prompt = f"""
You are preparing search queries for arXiv.

Return ONLY the search query.
No bullet points.
No quotes.
No explanations.
One line only.

Remove words like:
- latest
- recent
- papers
- research
- show me

Examples:
latest papers on rag
→ retrieval augmented generation

recent transformer papers
→ transformer

Question:
{query}
"""
    else:
      prompt = f"""
You improve search queries.
Rewrite the user's question so it is more specific and clear, while keeping the original intent.
Rules:
- Do not change the meaning of the question.
- Make the question more specific and clear.
-Don't answer the question, just rewrite it.
-Return only rewritten query, no other text.

User's question: {query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = prompt,
    )
    
    return response.text.strip()