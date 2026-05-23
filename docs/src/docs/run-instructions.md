# Run Instructions

This file explains how to run the portfolio-safe backend sample for AYNEXT.

## Requirements

- Python 3.10 or later
- pip
- Git
- VS Code or any code editor

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/aynext-ai-smart-glasses.git
cd aynext-ai-smart-glasses
Install the required Python packages:

pip install -r requirements.txt
Run the Backend Sample

Start the FastAPI backend using Uvicorn:

uvicorn src.backend_sample:app --reload

The backend should start locally at:

http://127.0.0.1:8000
Test the Health Endpoint

Open this link in your browser:

http://127.0.0.1:8000/health

Expected response:

{
  "status": "running",
  "project": "AYNEXT",
  "mode": "portfolio_sample"
}
Test the Assistant Endpoint

You can test the assistant endpoint using this PowerShell command:

$body = @{
    user_id = 1
    question_text = "ساعدني أفهم الموقف"
    current_scene_text = "The user is in a meeting and needs a short response"
    recent_transcript = "The conversation is about project planning"
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/assistant/ask_text" -Body $body -ContentType "application/json"

Expected response example:

{
  "user_id": 1,
  "response_language": "ar",
  "response_text": "بناءً على السياق الحالي: The user is in a meeting and needs a short response، أقدر أساعدك بخطوة مناسبة.",
  "response_source": "sample_reasoning"
}
Notes

This repository contains a portfolio-safe sample, not the full private project code.

Private files, API keys, database files, model files, and sensitive project data are intentionally excluded.
