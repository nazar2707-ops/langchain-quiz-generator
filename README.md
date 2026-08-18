# Python AI Portfolio

A small Python project demonstrating use of Google Gemini via LangChain wrappers to build AI-powered portfolio utilities.

## Features
- Loads environment variables from `.env`
- Uses `langchain_google_genai` to interact with Gemini models
- Simple example script at `portfolio.py`

## Requirements
- Python 3.9+
- A Google Gemini API key
- Recommended virtual environment

## Installation
1. Clone the repo
2. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
3. Install dependencies:
   pip install -r requirements.txt

## Configuration
Create a `.env` file at the project root:
GEMINI_API_KEY=your_gemini_api_key_here

## Usage
Example (from `portfolio.py`):
```python
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)
print("LLM initialized successfully!")