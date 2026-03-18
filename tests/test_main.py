import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import Base, Todo, app, get_db


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    yield session
    session.close()


@pytest.fixture
def client():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    TestSession = sessionmaker(bind=engine)

    def override_get_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


def test_create_todo(db):
    todo = Todo(title="Test task")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    assert todo.id is not None
    assert todo.title == "Test task"
    assert todo.completed is False
    assert todo.created_at is not None


def test_get_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "todo-list" in response.text


def test_create_todo_via_api(client):
    response = client.post("/todos", data={"title": "New task"})
    assert response.status_code == 200
    assert "New task" in response.text


def test_create_todo_empty_title(client):
    response = client.post("/todos", data={"title": ""})
    assert response.status_code == 200
    assert "0 items" in response.text


def test_toggle_todo(client):
    client.post("/todos", data={"title": "Toggle me"})
    response = client.put("/todos/1/toggle")
    assert response.status_code == 200
    assert "completed" in response.text


def test_delete_todo(client):
    client.post("/todos", data={"title": "Delete me"})
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert "Delete me" not in response.text
    assert "0 items" in response.text
