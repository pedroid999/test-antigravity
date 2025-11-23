# User Registration System API

This is the backend for the User Registration System, built with [FastAPI](https://fastapi.tiangolo.com/). It provides endpoints for user registration, authentication, and profile retrieval.

## Features

- **User Registration**: Create new user accounts.
- **Authentication**: Secure login using OAuth2 with Password flow (email as username) and JWT tokens.
- **User Profile**: Retrieve authenticated user details.
- **Database**: SQLite database using SQLModel (SQLAlchemy + Pydantic).

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) (fast Python package installer and resolver)

## Setup

1.  **Navigate to the backend directory:**

    ```bash
    cd backend
    ```

2.  **Install dependencies:**

    This project uses `uv` for dependency management.

    ```bash
    uv sync
    ```

## Running the Server

To start the development server with hot-reloading:

```bash
uv run uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, you can access it at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

### General

- `GET /`: Welcome message.

### Users

- `POST /users/register`: Register a new user.
    - **Body**: JSON object with `email`, `password`, and optional `full_name`.
    - **Returns**: Created user details (excluding password).

- `POST /users/token`: Login to get an access token.
    - **Body**: Form data with `username` (email) and `password`.
    - **Returns**: JSON object with `access_token` and `token_type`.

- `GET /users/me`: Get current user profile.
    - **Headers**: `Authorization: Bearer <access_token>`
    - **Returns**: Current user details.

## Project Structure

- `main.py`: Entry point of the application. Configures FastAPI and CORS.
- `database.py`: Database connection and session management.
- `models.py`: SQLModel database models and Pydantic schemas.
- `auth.py`: Authentication logic (password hashing, token creation/verification).
- `routers/`: Directory for API route definitions.
    - `users.py`: User-related endpoints.
- `tests/`: Directory for tests.

## Testing

To run the tests:

```bash
uv run pytest
```
