# PROJECT: IR Infotech REST API Challenge

## Objective

Build a production-ready REST API with **3 NLP endpoints** using **FastAPI** and the **Google Gemini API**.

---

# Scope

* **Framework:** FastAPI
* **LLM:** Google Gemini API (Free Tier)
* **Endpoints:** 3 (`summarize`, `translate`, `generate-email`)
* **Deployment:** Render.com or Railway.app

### Deliverables

* GitHub Repository
* Deployed API
* Video Explanation

---

# Requirements

## Functional Requirements

### `POST /summarize`

**Input**

```json
{
  "text": "Your text here"
}
```

**Output**

```json
{
  "summary": "Summarized text here"
}
```

**Logic**

* Use Gemini to summarize the input into **2–3 sentences**.

---

### `POST /translate`

**Input**

```json
{
  "text": "Your text here"
}
```

**Output**

```json
{
  "translated": "Texto traducido aquí"
}
```

**Logic**

* Translate the input text into **Spanish** (or any other language).

---

### `POST /generate-email`

**Input**

```json
{
  "text": "Meeting tomorrow at 10 AM regarding the project."
}
```

**Output**

```json
{
  "email": "Dear Team,\n\n..."
}
```

**Logic**

* Generate a **professional email** from the provided text.

---

# Non-Functional Requirements

* Request validation using **Pydantic models**
* Exception handling (`try/except`) for API errors
* Logging of all requests and responses
* Store API keys using **environment variables (`.env`)**
* Clean and organized project structure
* API documentation (`README.md` + inline comments)
* Deployment-ready (no localhost dependencies)

---

# Technical Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Language        | Python 3.9+           |
| Framework       | FastAPI               |
| LLM             | `google-generativeai` |
| Deployment      | Render / Railway      |
| Version Control | GitHub                |

---

# Deliverables

## GitHub Repository

Must include:

* Clean Python code
* `.env.example`
* `README.md` with setup instructions
* API documentation

## Deployment

* Live API URL

## Screen Recording (10–15 minutes)

Include:

1. Project overview
2. Code walkthrough
3. API testing demo
4. Local setup and execution

---

# Acceptance Criteria

* ✅ All 3 endpoints work correctly
* ✅ Error handling for invalid inputs
* ✅ API responses are valid JSON
* ✅ Code is readable and documented
* ✅ GitHub has a clean commit history
* ✅ Deployed URL is publicly accessible

---

# Success Metrics

* ✅ All endpoints functional
* ✅ No runtime errors
* ✅ Successfully deployed and accessible
* ✅ Clear video explanation
* ✅ Clean and well-documented GitHub repository
