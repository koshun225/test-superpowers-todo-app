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
