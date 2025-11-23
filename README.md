# User Registration System

A full-stack user registration system built with FastAPI (Backend) and React (Frontend).

## Features

- User Registration
- User Login (JWT Authentication)
- Profile View
- Secure Password Hashing (Argon2)
- Responsive UI

## Tech Stack

- **Backend**: FastAPI, SQLModel, Uvicorn, Passlib (Argon2), Pytest
- **Frontend**: React, Vite, React Router, Vanilla CSS
- **Tooling**: uv (Python), npm (Node.js)

## Setup

### Backend

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

3. Run the server:
   ```bash
   uv run uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

### Frontend

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:5173`.

## Testing

### Backend Tests

Run tests using `pytest`:
```bash
cd backend
PYTHONPATH=. uv run pytest
```
