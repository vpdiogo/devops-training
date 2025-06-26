from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import os
from .config.settings import get_settings

app = FastAPI(
    title="DevOps Training API",
    description="Simple FastAPI application for DevOps practice",
    version="1.0.0"
)

settings = get_settings()

# Pydantic models for request/response
class HealthResponse(BaseModel):
    status: str
    message: str
    version: str

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    echo: str
    processed_message: str

@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint returning basic info"""
    return {
        "message": "DevOps Training API is running!",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint for monitoring"""
    return HealthResponse(
        status="healthy",
        message="Application is running properly",
        version="1.0.0"
    )

@app.post("/echo", response_model=MessageResponse)
async def echo_message(request: MessageRequest) -> MessageResponse:
    """Echo endpoint that processes and returns the message"""
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    return MessageResponse(
        echo=request.message,
        processed_message=f"Processed: {request.message.upper()}"
    )

@app.get("/info")
async def app_info() -> Dict[str, Any]:
    """Information about the application and environment"""
    return {
        "app_name": "DevOps Training",
        "framework": "FastAPI",
        "python_version": "3.11",
        "environment": settings.ENVIRONMENT,
        "debug": settings.DEBUG,
        "host": os.getenv("HOSTNAME", "unknown")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.app:app",
        host="0.0.0.0",
        port=8080,
        reload=settings.DEBUG
    )
