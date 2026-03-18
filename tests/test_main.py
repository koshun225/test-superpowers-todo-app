import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import Base, Todo


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    yield session
    session.close()


def test_create_todo(db):
    todo = Todo(title="Test task")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    assert todo.id is not None
    assert todo.title == "Test task"
    assert todo.completed is False
    assert todo.created_at is not None
