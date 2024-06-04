from fastapi import HTTPException, Depends, APIRouter
from pydantic import BaseModel
from typing import Annotated
import models
from database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(
  prefix="/api/todos",
  tags=["todos"]
)

class TodoBase(BaseModel):
    title: str
    priority: int
    
class TodoUpdate(BaseModel):
  completed: bool

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]

@router.get("")
def get_todos(db: db_dependency):
  todos = db.query(models.TodosTable).order_by(models.TodosTable.id).all()
  if not isinstance(todos, list):
    return HTTPException(status_code=404)
  
  return todos

@router.patch("/{todo_id}")
def update_todo(todo_id: int, db: db_dependency, todo_data: TodoUpdate):
  db_todo = db.query(models.TodosTable).filter(models.TodosTable.id == todo_id).first()
  if db_todo is None:
    return HTTPException(status_code=404, detail="Todo not found")
  
  update_data = todo_data.model_dump(exclude_unset=True)
  
  for key, value in update_data.items():
      setattr(db_todo, key, value)

  db.add(db_todo)
  db.commit()
  db.refresh(db_todo)
  
  return db_todo

@router.post("")
def create_todo(todo: TodoBase,db: db_dependency):
  db_todo = models.TodosTable(title=todo.title, priority=todo.priority)
  db.add(db_todo)
  db.commit()
  db.refresh(db_todo)
  
  return db_todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: db_dependency):
  deleted_todo= db.query(models.TodosTable).filter(models.TodosTable.id == todo_id).first()

  if not deleted_todo:
    return HTTPException(status_code=404, detail="Todo doesn't deleted!")
  
  db.delete(deleted_todo)
  db.commit()

  return {"response": 200}