from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    title: str
    completed: bool
    priority: int

@app.get("/")
def get_todos():
    return {"message": "Hello World"}