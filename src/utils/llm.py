import os
from src.utils.config import MODEL
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(
    api_key=api_key
)


def ask_llm(prompt):
    response = client.models.generate_content(
        model = MODEL,
        contents=prompt
    )

    return response.text