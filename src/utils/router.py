from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

def choose_tool(query):
    prompt = f"""
    You are a routing assistant.
    
    You have three tools:
    
    1.pdf
    Use for:
   - Questions answerable from my local documents 
   - Existing indexed PDFs
    
    2.Web
    Use for:
    -Latest news
    -Current events
    -Recent information
    -Today's updates
    
    3.arxiv
    Use for:
    -Research papers
    -Academic publications
    -Paper Recommendations
    -Scientific literature
    
    Return only one word.
    pdf 
    or 
    web
    or
    arxiv
    Question:
    {query}
    """
    response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
    return response.text.strip().lower()
