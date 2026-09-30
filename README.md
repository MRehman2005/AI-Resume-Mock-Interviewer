# AI-Resume-Mock-Interviewer
AI Resume Mock Interviewer

An AI-powered mock interview application that uses a candidate's resume to create personalized interview questions.

The system extracts information from the uploaded resume, converts it into embeddings, and stores them in PostgreSQL with pgvector. When an interview starts, RAG retrieves relevant resume information and provides it to the LLM to generate questions.

The candidate then answers the questions, and the LLM evaluates the answers and provides a score and feedback.

🔄 Workflow
Resume PDF
    ↓
Extract & Clean Text
    ↓
Create Chunks
    ↓
Generate Embeddings
    ↓
PostgreSQL + pgvector
    ↓
RAG Retrieval
    ↓
LLM Question Generation
    ↓
Candidate Answers
    ↓
LLM Evaluation
    ↓
Score & Feedback

🛠️ Tech Stack

Python

FastAPI

LangChain

PostgreSQL

pgvector

PyPDF

SQLAlchemy

LLM

✨ Features

Upload and process resume PDFs

Generate resume-based interview questions

RAG-based context retrieval

AI-powered answer evaluation

Scoring and personalized feedback

🚧 Status

Currently under development.

📄 License

For educational and development purposes.
