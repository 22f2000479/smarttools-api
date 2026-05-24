# SmartTools API

SmartTools API is a simple backend project built using FastAPI.  
The idea behind this project is to create a small API where users can explore different AI tools and apply filters, sorting, and pagination.

I built this project to understand:
- how APIs work
- how backend applications are structured
- how filtering and pagination are implemented
- the difference between quick coding vs structured development

This repository contains two branches:
- `sdd_submission`
- `vibe_coded_submission`

Both branches solve the same problem but using different development approaches.

---

## Features

- View AI tools data
- Filter tools by category
- Filter tools by pricing type
- Sort data
- Pagination support
- FastAPI Swagger documentation
- Health check endpoint

---

## Tech Used

- Python
- FastAPI
- Uvicorn
- Pydantic

---

## Project Structure

```text
app/
├── __init__.py
├── data.py
├── models.py
├── reports.py
└── main.py
```

### File Usage

- `models.py` contains the data models
- `data.py` contains sample dataset
- `reports.py` handles filtering and sorting logic
- `main.py` contains API routes

---

## API Endpoints

### Health Endpoint

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

---

### Tools Endpoint

```http
GET /tools
```

---

## Available Query Parameters

| Parameter | Purpose |
|---|---|
| category | Filter by tool category |
| pricing | Filter by pricing type |
| sort | Sort results |
| descending | Ascending/descending order |
| offset | Pagination offset |
| limit | Number of results |

---

## Example URLs

Get all tools:

```bash
http://127.0.0.1:8000/tools
```

Filter chatbot tools:

```bash
http://127.0.0.1:8000/tools?category=chatbot
```

Filter free tools:

```bash
http://127.0.0.1:8000/tools?pricing=free
```

Pagination example:

```bash
http://127.0.0.1:8000/tools?limit=5
```

---

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/22f2000479/smarttools-api.git
```

Go inside the folder:

```bash
cd smarttools-api
```

Create virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
python -m uvicorn app.main:app --reload --port 8000
```

---

## Swagger Documentation

After running the server open:

```text
http://127.0.0.1:8000/docs
```

---

## Branch Information

| Branch Name | Description |
|---|---|
| sdd_submission | Structured version with separated layers |
| vibe_coded_submission | Quick implementation version |

---

## What I Learned

Through this project I learned:
- FastAPI basics
- API routing
- Query parameters
- Pagination
- Git branching
- Difference between modular and quick implementations

---

## Author

Raunak Sen