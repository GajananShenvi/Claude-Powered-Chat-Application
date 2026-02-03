# Claude Chat Backend

FastAPI backend for the Claude Chat application.

Hear in backend you will have to create an .env file and add your,  
ANTHROPIC_API_KEY=your_claude_api_key_here
or (in case if you are using any other api)
GROQ_API_KEY = your_groq_api_key_hear

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Environment:
   Edit `.env` and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=sk-...
   ```

## Running

Start the server:
```bash
python -m app.main
```
Or with uvicorn directly:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000.
Docs available at http://localhost:8000/docs.

