"""
AYNEXT Backend Sample

This is a simplified portfolio-safe FastAPI sample inspired by the AYNEXT project.
It demonstrates the basic request/response flow for an AI smart glasses assistant.

Note:
- This is not the full production/demo backend.
- No API keys or private project data are included.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI(
    title="AYNEXT AI Smart Glasses Assistant",
    description="Portfolio-safe backend sample for an AI-powered smart glasses assistant.",
    version="0.1.0",
)


class AssistantRequest(BaseModel):
    user_id: int
    question_text: str
    current_scene_text: Optional[str] = None
    recent_transcript: Optional[str] = None


class AssistantResponse(BaseModel):
    user_id: int
    response_language: str
    response_text: str
    response_source: str


def generate_assistant_response(request: AssistantRequest) -> str:
    """
    Simplified reasoning function.

    In the full project, this layer can connect to:
    - Local LLMs
    - User profile data
    - Social recommendation logic
    - Scene/context understanding
    - Arabic-first response rules
    """

    question = request.question_text.lower()

    if "translate" in question or "ترجم" in question:
        return "أقدر أساعدك في الترجمة حسب السياق اللي قدامي."

    if "help" in question or "ساعدني" in question:
        return "أنا معاك. قلّي الموقف أو المشكلة وسأقترح عليك أفضل خطوة."

    if request.current_scene_text:
        return f"بناءً على السياق الحالي: {request.current_scene_text}، أقدر أساعدك بخطوة مناسبة."

    return "فهمت سؤالك. أقدر أساعدك بإجابة مختصرة وواضحة."


@app.get("/health")
def health_check():
    return {
        "status": "running",
        "project": "AYNEXT",
        "mode": "portfolio_sample",
    }


@app.post("/assistant/ask_text", response_model=AssistantResponse)
def ask_text(request: AssistantRequest):
    response = generate_assistant_response(request)

    return AssistantResponse(
        user_id=request.user_id,
        response_language="ar",
        response_text=response,
        response_source="sample_reasoning",
    )
