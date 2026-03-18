from datetime import datetime, timezone

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import Boolean, Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


DATABASE_URL = "sqlite:///./todos.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def index(request: Request, db=Depends(get_db)):
    todos = db.query(Todo).order_by(Todo.created_at.desc()).all()
    return templates.TemplateResponse(request, "index.html", {"todos": todos})


@app.post("/todos", response_class=HTMLResponse)
def create_todo(request: Request, title: str = Form(""), db=Depends(get_db)):
    if title.strip():
        todo = Todo(title=title.strip())
        db.add(todo)
        db.commit()
    todos = db.query(Todo).order_by(Todo.created_at.desc()).all()
    return templates.TemplateResponse(request, "partials/todo_list.html", {"todos": todos})
