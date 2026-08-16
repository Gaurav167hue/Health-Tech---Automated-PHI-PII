# 🏥 Health-Tech – Automated PHI/PII Redaction API

Backend API for the **Health-Tech – Automated PHI/PII Redaction** project.

This backend is built using **FastAPI** and provides REST APIs for redacting and restoring Protected Health Information (PHI) / Personally Identifiable Information (PII) from clinical text.

---

# 🚀 Features

- FastAPI Framework
- REST API Endpoints
- Pydantic Request & Response Validation
- Swagger API Documentation
- CORS Middleware
- Logging Support
- Global Exception Handling
- Environment Configuration
- Modular Project Structure
- Ready for NLP/Regex Integration

---

# 🛠 Tech Stack

- Python 3.14+
- FastAPI
- Uvicorn
- Pydantic
- Python-dotenv

---

# 📂 Project Structure

backend/
│
├── app/
│ ├── routes/
│ │ └── redaction.py
│ │
│ ├── schemas/
│ │ ├── request_response.py
│ │ └── **init**.py
│ │
│ ├── services/
│ │ ├── redaction_service.py
│ │ ├── nlp_service.py
│ │ └── **init**.py
│ │
│ ├── config.py
│ ├── logger.py
│ ├── exceptions.py
│ ├── exception_handler.py
│ ├── main.py
│ └── **init**.py
│
├── .env
├── requirements.txt
└── README.md

---

# ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into backend folder

```bash
cd backend
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Server

```bash
python -m uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# 📌 API Endpoints

## GET /

Returns API status.

Response

```json
{
  "message": "Health Redaction API is running successfully"
}
```

---

## GET /health

Health check endpoint.

Response

```json
{
  "status": "healthy",
  "service": "Health Redaction API",
  "version": "1.0.0"
}
```

---

## POST /api/v1/redact

Redacts PHI/PII from clinical text.

Request

```json
{
  "text": "John Smith visited AIIMS Delhi on 12/07/2026."
}
```

Current Response

```json
{
  "original_text": "John Smith visited AIIMS Delhi on 12/07/2026.",
  "redacted_text": "John Smith visited AIIMS Delhi on 12/07/2026.",
  "status": "success"
}
```

> Currently returns placeholder output.
> NLP/Regex implementation will be integrated in future.

---

## POST /api/v1/restore

Restores previously redacted text.

Request

```json
{
  "text": "Patient_001 visited Hospital_001."
}
```

Response

```json
{
  "restored_text": "Patient_001 visited Hospital_001.",
  "status": "success"
}
```

---

# 📖 Request Models

## RedactRequest

```json
{
  "text": "string"
}
```

## RestoreRequest

```json
{
  "text": "string"
}
```

---

# 📖 Response Models

## RedactResponse

```json
{
  "original_text": "string",
  "redacted_text": "string",
  "status": "success"
}
```

## RestoreResponse

```json
{
  "restored_text": "string",
  "status": "success"
}
```

---

# ❌ Error Handling

Example Validation Error

```json
{
  "status": "error",
  "message": "Validation failed",
  "details": []
}
```

Example Empty Request

```json
{
  "detail": "Input text cannot be empty."
}
```

---

# 📝 Logging

The application logs

- Incoming API requests
- Validation errors
- Server startup
- Runtime events

---

# 🔒 Security

Current Version

- Request Validation
- Exception Handling
- Input Validation

Future Version

- Authentication
- JWT Authorization
- Rate Limiting
- HTTPS
- Audit Logging

---

# 🔄 Future Integration

This API layer is designed for seamless integration with upcoming modules.

Planned integrations include

- Regex Engine
- Microsoft Presidio
- spaCy NLP
- Token Vault
- Redis Cache
- Pseudonymization Engine

---

# 👨‍💻 Development

Start development server

```bash
python -m uvicorn app.main:app --reload
```

Generate requirements

```bash
pip freeze > requirements.txt
```

---

# 🧪 Testing

Swagger UI

```
http://127.0.0.1:8000/docs
```

Health Check

```
GET /health
```

Redaction API

```
POST /api/v1/redact
```

Restore API

```
POST /api/v1/restore
```

---

# 👥 Team Responsibilities

## Member 1

- FastAPI Setup
- API Layer
- REST Endpoints
- Request/Response Handling

## Member 2

- Regex Detection
- Microsoft Presidio
- spaCy Integration

## Member 3

- Token Vault
- Redis
- Pseudonym Mapping

## Member 4

- Testing
- Documentation
- Integration
- Deployment

---

# 📄 License

This project is developed as part of an internship project for educational purposes.

---

# ✨ Author

Backend API Layer

**Abhimanyu Dubey**

Member 1 – FastAPI & API Layer
