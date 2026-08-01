from google import genai
from dotenv import load_dotenv
from src.utils.config import MODEL
import streamlit as st
import os

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(
    api_key=api_key
)

def evaluate_context(query, context):

    prompt = f"""
You are evaluating retrieved context for a RAG system.

Question:
{query}

Retrieved Context:
{context}

Task:

Determine whether the retrieved context contains enough relevant information
to answer the user's question accurately.

Return ONLY one word.

YES

or

NO

Do not explain.
"""

    response = client.models.generate_content(
        model = MODEL,
        contents=prompt
    )

    return response.text.strip().upper()