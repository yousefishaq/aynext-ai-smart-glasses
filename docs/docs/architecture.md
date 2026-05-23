# System Architecture

AYNEXT is built as a laptop-first AI assistant demo that connects voice input, backend reasoning, local AI models, and contextual user data.

The architecture focuses on building a practical prototype before moving to dedicated smart-glasses hardware.

## High-Level Architecture

```mermaid
flowchart TD
    A[User Voice Input] --> B[Voice Capture Module]
    B --> C[Speech-to-Text using faster-whisper]
    C --> D[FastAPI Backend]
    D --> E[Context & Reasoning Layer]
    E --> F[Local LLM using Ollama]
    E --> G[SQLite Database]
    F --> H[Arabic-First Assistant Response]
    G --> H
    H --> I[Text / Voice Output]
Main Components
1. Voice Input Layer

This layer captures the user's speech and prepares it for transcription.

Main responsibilities:

Capture microphone audio
Detect speech and silence
Reduce false triggers
Send clean audio to the speech-to-text module
2. Speech-to-Text Layer

This layer converts spoken input into text using faster-whisper.

Main responsibilities:

Transcribe user speech
Support Arabic voice input
Handle low-confidence transcripts
Prepare the final text request for the backend
3. Backend Layer

The backend is built using Python and FastAPI.

Main responsibilities:

Receive user questions
Receive optional scene/context information
Connect to the AI reasoning layer
Return structured assistant responses
Manage API endpoints for the demo
4. AI Reasoning Layer

This layer decides how the assistant should respond based on the user request and available context.

Main responsibilities:

Understand user intent
Apply assistant behavior rules
Generate Arabic-first responses
Use local LLM output when available
Use fallback responses when needed
5. Local LLM Layer

The project uses local AI models through Ollama for privacy-friendly and offline-capable experimentation.

Main responsibilities:

Generate assistant responses
Support Arabic interaction
Reduce dependency on cloud APIs
Allow local testing and iteration
6. Database Layer

SQLite is used to store lightweight project data.

Main responsibilities:

Store user profiles
Store social contacts
Store context and recommendation data
Support prototype personalization features
7. Output Layer

The assistant returns the response to the user as text or voice.

Main responsibilities:

Display assistant response
Speak the response using TTS when enabled
Keep responses useful, short, and context-aware
Request Flow
User speaks to the assistant.
The voice module records the audio.
faster-whisper converts speech into text.
The text is sent to the FastAPI backend.
The backend checks context, user profile, and reasoning rules.
Ollama generates an AI response when available.
The backend returns an Arabic-first assistant response.
The response is shown or spoken to the user.
Design Decisions
Laptop-First Demo

The project is currently designed to run on a laptop first.
This makes testing faster and avoids early hardware complexity.

Local AI Model Integration

Using local models allows the project to test AI behavior without depending completely on cloud APIs.

Arabic-First Interaction

The assistant is designed with Arabic responses as a main priority, especially for real-life local usage.

Modular Development

The system is divided into layers so each part can be improved separately:

Voice pipeline
Backend API
AI reasoning
Database
Dashboard
Future hardware integration
Future Architecture Improvements
Add real camera input for scene understanding
Add better dashboard analytics
Improve Arabic speech recognition accuracy
Add stronger user-state tracking
Optimize response latency
Prepare Raspberry Pi or smart-glasses hardware integration
