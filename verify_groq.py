
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv(dotenv_path="backend/.env")

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ GROQ_API_KEY not found in backend/.env")
    print("Please add GROQ_API_KEY=your_key_here to backend/.env")
    exit(1)

print("✅ Found GROQ_API_KEY")

try:
    client = Groq(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Hello, are you working?",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    print("✅ Groq API connection successful!")
    print("Response:", chat_completion.choices[0].message.content)
except Exception as e:
    print(f"❌ Error connecting to Groq API: {e}")
