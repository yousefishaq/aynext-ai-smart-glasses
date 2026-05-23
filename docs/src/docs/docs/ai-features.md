# AI Features

This document explains the main AI-related features in the AYNEXT project.

AYNEXT is designed as an AI-powered smart glasses assistant that combines speech AI, natural language processing, local LLM integration, user-context modeling, and recommendation logic.

## 1. Arabic-First AI Assistant

The assistant is designed to respond mainly in Arabic because the target user experience focuses on natural local interaction.

Main goals:

- Understand Arabic user requests
- Generate short and useful Arabic responses
- Avoid unnecessary long answers
- Support real-life spoken interaction
- Handle mixed Arabic-English technical phrases

## 2. Speech-to-Text Pipeline

AYNEXT uses a speech-to-text pipeline to convert user voice into text.

The pipeline is designed to:

- Capture user speech from the microphone
- Convert spoken Arabic into text
- Detect silence and stop recording automatically
- Reduce false transcripts
- Send clean text to the backend

In the prototype, faster-whisper is used as the main speech-to-text engine.

## 3. Text-to-Speech Output

The assistant can return responses as text or voice.

The TTS layer is useful because smart glasses should be hands-free and should not force the user to read long text from a screen.

Main goals:

- Speak assistant responses clearly
- Keep responses short enough for voice output
- Support Arabic voice output
- Avoid reading low-quality or incorrect responses

## 4. Local LLM Integration

AYNEXT uses local AI models through Ollama for experimentation.

The local LLM layer helps the assistant generate flexible responses instead of using only fixed rules.

Main benefits:

- Local testing
- Reduced cloud dependency
- Better privacy for prototype experiments
- Easier model iteration
- Arabic response experimentation

## 5. Context-Aware Reasoning

The assistant can use extra context to improve its response.

Example context types:

- Current scene description
- Recent conversation transcript
- User request
- Stored user profile
- Previous interaction patterns

This allows the assistant to respond based on the situation, not only the direct question.

## 6. User Profile and Memory

The system can store lightweight user information using SQLite.

This can support personalization features such as:

- Preferred response style
- User needs
- Previous interactions
- Important context
- Recommendation history

The goal is to make the assistant more useful over time.

## 7. Social Recommendation Prototype

AYNEXT includes a prototype idea for recommending relevant people or actions based on user context.

Example:

If the user needs help with a work-related problem, the system can suggest a person who is strongly connected to work topics.

The recommendation logic can use:

- Topic weights
- Relationship type
- Previous interactions
- Context category
- Suitability score

## 8. Daily User-State Dashboard Concept

The project includes a dashboard concept for tracking user state over time.

The dashboard idea is to show:

- Daily emotional or behavioral state
- Important events that affected the day
- Explanation of why a day was good or bad
- Suggestions for better decisions in similar future situations

## 9. AI Safety and Fallback Handling

The assistant should avoid giving random or low-confidence responses.

Planned safety behavior:

- Use fallback responses when the model is unavailable
- Avoid speaking unclear generated text
- Keep responses short in uncertain situations
- Ask for clarification when needed
- Avoid overconfident recommendations

## 10. Future AI Improvements

Future improvements may include:

- Better Arabic speech recognition
- Stronger Arabic NLP handling
- RAG-based knowledge retrieval
- Better user-state classification
- Improved recommendation scoring
- Real-time visual scene understanding
- More reliable local LLM response evaluation
