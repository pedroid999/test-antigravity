import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from main import app
from database import get_session

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

def test_register_user(client: TestClient):
    response = client.post(
        "/users/register",
        json={"email": "test@example.com", "password": "password123", "full_name": "Test User"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "password" not in data

def test_login_user(client: TestClient):
    # Register first
    client.post(
        "/users/register",
        json={"email": "test@example.com", "password": "password123"},
    )
    
    response = client.post(
        "/users/token",
        data={"username": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_read_users_me(client: TestClient):
    # Register
    client.post(
        "/users/register",
        json={"email": "test@example.com", "password": "password123"},
    )
    
    # Login
    login_response = client.post(
        "/users/token",
        data={"username": "test@example.com", "password": "password123"},
    )
    token = login_response.json()["access_token"]
    
    # Get Me
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
