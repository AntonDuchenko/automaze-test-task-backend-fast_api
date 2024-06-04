from fastapi import FastAPI
from router import router as todo_router
from database import engine
import models

app = FastAPI()
app.include_router(todo_router)
models.Base.metadata.create_all(bind=engine)