import anthropic
from app.core.config import settings

# Initialize the client only if the key is present (handled by dotenv mostly, but good to be safe)
if settings.ANTHROPIC_API_KEY:
    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
else:
    client = None

def get_claude_response(message: str) -> str:
    if not client:
        return "Error: Claude API Key not configured."
    
    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Error talking to Claude: {str(e)}"
