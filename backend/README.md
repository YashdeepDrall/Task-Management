# Backend

FastAPI backend for the Project & Task Management System.

## Phase 1

- Loads configuration from `.env` with `pydantic-settings`
- Connects to MongoDB with Motor
- Creates the required user, project, and task indexes on startup
- Exposes Swagger UI at `/docs`

## Run

```bash
python -m uvicorn app.main:app --reload
```
