"""
GroceryBot - AI Customer Support Chatbot

TODO: Build the chat API endpoint.
The flow is:
1. User sends a message
2. We search the knowledge base for relevant info (RAG retrieval)
3. We send the relevant info + user question to the LLM
4. Return the LLM's response
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="GroceryBot - AI Customer Support")
app.mount("/static", StaticFiles(directory="static"), name="static")


class ChatMessage(BaseModel):
    message: str
    conversation_id: str = "default"


class ChatResponse(BaseModel):
    response: str
    sources: list[str] = []


# In-memory conversation history (simple approach)
conversations: dict[str, list] = {}


@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html") as f:
        return f.read()


@app.post("/api/chat", response_model=ChatResponse)
async def chat(msg: ChatMessage):
    """
    TODO: Implement the RAG chat pipeline.

    Steps:
    1. Get conversation history for this conversation_id
    2. Search knowledge base for relevant info (use rag/retriever.py)
    3. Build prompt with: system message + relevant knowledge + conversation history + user question
    4. Call the LLM (use rag/generator.py)
    5. Save the exchange to conversation history
    6. Return the response + sources used
    """
    # YOUR CODE HERE
    return ChatResponse(
        response="I'm GroceryBot! I'm not fully implemented yet. Teach me about produce!",
        sources=[]
    )


@app.post("/api/clear")
async def clear_conversation(conversation_id: str = "default"):
    """Clear conversation history."""
    conversations.pop(conversation_id, None)
    return {"status": "cleared"}


@app.get("/api/health")
async def health():
    return {"status": "healthy", "knowledge_loaded": False}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
