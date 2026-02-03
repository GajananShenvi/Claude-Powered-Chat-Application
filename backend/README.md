# Claude Chat Backend

FastAPI backend for the Claude Chat application.

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
