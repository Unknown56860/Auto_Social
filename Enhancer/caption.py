import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Explicitly load environment variables from venv/.env file
env_path = Path(__file__).parent.parent.parent / "venv" / ".env"
load_dotenv(dotenv_path=env_path)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat()

def enhance_caption(caption, upscale=False):
    prompt = (
        "Enhance this caption for a social media post. "
        "Only return the enhanced caption with a word limit between 20 to 80 words as per the requiredment, and with a simple english terms."
    )
    if upscale:
        prompt += "Make it suitable for a high-impact influencer, maximizing engagement and reach. "
    prompt += f"\n\n{caption}"
    try:
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
