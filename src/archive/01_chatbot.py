from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
print("ScholarAgent Chatbot")
print("Type 'exit' to quit\n")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=prompt
        )
    
        print("\nBot:\n",response.text)
        print()

    except Exception as e:
        print("\nError:",e)
        print()