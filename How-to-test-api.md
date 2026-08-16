# 🧪 How to Test the API

## Prerequisites

- Python 3.10 or higher
- pip installed

---

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Health-Tech---Automated-PHI-PII
```

---

## Step 2: Checkout the Correct Branch

```bash
git checkout <branch-name>
```

Example:

```bash
git checkout member-1-api
```

---

## Step 3: Navigate to Backend

```bash
cd backend
```

---

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5: Start the Server

```bash
python -m uvicorn app.main:app --reload
```

If the server starts successfully, you should see:

```
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

---

## Step 6: Open Swagger UI

Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

---

## Step 7: Verify Endpoints

### GET /

Expected Response

```json
{
  "message": "Health Redaction API is running successfully"
}
```

---

### GET /health

Expected Response

```json
{
  "status": "healthy",
  "service": "Health Redaction API",
  "version": "1.0.0"
}
```

---

### POST /api/v1/redact

Request

```json
{
  "text": "John Smith visited AIIMS Delhi on 12/07/2026."
}
```

Expected Response

```json
{
  "original_text": "John Smith visited AIIMS Delhi on 12/07/2026.",
  "redacted_text": "John Smith visited AIIMS Delhi on 12/07/2026.",
  "status": "success"
}
```

---

### POST /api/v1/restore

Request

```json
{
  "text": "Patient_001 visited Hospital_001."
}
```

Expected Response

```json
{
  "restored_text": "Patient_001 visited Hospital_001.",
  "status": "success"
}
```

---

## Step 8: Validation Test

Send an empty request:

```json
{
  "text": ""
}
```

Expected Result:

- Validation error (400 or 422), depending on the configured exception handler.

---

## Test Checklist

- [ ] Server starts without errors
- [ ] Swagger UI opens
- [ ] GET `/` returns success
- [ ] GET `/health` returns healthy status
- [ ] POST `/api/v1/redact` returns expected JSON
- [ ] POST `/api/v1/restore` returns expected JSON
- [ ] Empty input is rejected
