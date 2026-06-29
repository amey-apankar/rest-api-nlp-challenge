# IR Infotech REST API Challenge

A production-ready REST API built with FastAPI and the Google Gemini API to handle three NLP tasks: summarization, translation, and professional email generation.

## Features
* Framework: FastAPI
* Validation: Pydantic models for request and response validation
* Integration: Google Gemini API (gemini-2.5-flash)
* Logging: Request and response logging middleware
* Exception Handling: Global exception and configuration error handling

## Project Structure
```
REST API/
├── app/
│   ├── config.py
│   ├── main.py
│   ├── schemas.py
│   └── services.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone or navigate to the repository directory.

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables. Copy `.env.example` to `.env` and fill in your API key:
   ```bash
   cp .env.example .env
   ```
   Add your Gemini API key in `.env`:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_MODEL=gemini-2.5-flash
   PORT=8000
   ```

## Running the Application

Start the development server using uvicorn:
```bash
uvicorn app.main:app --reload
```
The API documentation will be available at:
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

### 1. POST /summarize
Summarizes the provided text into 2 to 3 sentences.

* Request Body:
  ```json
  {
    "text": "Your long text here..."
  }
  ```
* Response Body:
  ```json
  {
    "summary": "Summarized text..."
  }
  ```

### 2. POST /translate
Translates the text into Spanish.

* Request Body:
  ```json
  {
    "text": "Text to translate..."
  }
  ```
* Response Body:
  ```json
  {
    "translated": "Translated text..."
  }
  ```

### 3. POST /generate-email
Generates a professional email from brief notes.

* Request Body:
  ```json
  {
    "text": "Meeting tomorrow at 10 AM regarding the project."
  }
  ```
* Response Body:
  ```json
  {
    "email": "Dear Team,\n\n..."
  }
  ```
