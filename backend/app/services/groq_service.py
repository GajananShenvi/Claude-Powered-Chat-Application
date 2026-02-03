import os
from groq import Groq
from app.core.config import settings

# Initialize the client only if the key is present
if settings.GROQ_API_KEY:
    client = Groq(api_key=settings.GROQ_API_KEY)
else:
    client = None

def get_groq_response(message: str) -> str:
    if not client:
        return "Error: Groq API Key not configured."
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="llama-3.3-70b-versatile", # Using a default reputable model suitable for general chat
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error talking to Groq: {str(e)}"
