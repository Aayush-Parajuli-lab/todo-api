# Todo API

A REST API for managing todos built with Python and FastAPI.

## Tech Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic

## Features

- Full CRUD — create, read, update, delete todos
- Auto-generated Swagger docs at /docs
- In-memory storage

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open http://localhost:8000/docs
