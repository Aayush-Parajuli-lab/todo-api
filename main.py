from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Counter, List, Optional

app = FastAPI(title="Todo Api")

todos = []
Counter = {"id": 1}


class TodoCreate(BaseModel):
    text: str


class TodoUpdate(BaseModel):
    text: Optional[str] = None
    completed: Optional[bool] = None


class Todo(BaseModel):
    id: int
    text: str
    completed: bool


@app.get("/")
def root():
    return {"message": "Todo API is running"}


@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos


@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo = Todo(id=Counter["id"], text=todo.text, completed=False)
    Counter["id"] += 1
    todos.append(new_todo.dict())
    return new_todo


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, update: TodoUpdate):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if update.text is not None:
        todo["text"] = update.text
    if update.completed is not None:
        todo["completed"] = update.completed
    return todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos = [t for t in todos if t["id"] != todo_id]
    return {"message": "Todo deleted"}
