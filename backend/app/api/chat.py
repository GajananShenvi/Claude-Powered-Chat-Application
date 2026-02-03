from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.claude_service import get_claude_response
from app.services.groq_service import get_groq_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    # OLD CODE: using Claude
    # response_text = get_claude_response(request.message)
    
    # NEW CODE: using Groq
    response_text = get_groq_response(request.message)
    
    return ChatResponse(reply=response_text)
