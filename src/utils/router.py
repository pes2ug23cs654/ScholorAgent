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
    
    You have two tools:
    
    1.pdf
    Use for:
    -Research Papers
    -AI concepts
    -Questions answerable from local doucments
    
    2.Web
    Use for:
    -Latest news
    -Current events
    -Recent information
    -Today's updates
    
    Return only one word.
    pdf 
    or 
    web
    Question:
    {query}
    """
    response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
    return response.text.strip().lower()