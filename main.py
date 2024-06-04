from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router as todo_router
from database import engine
import models

app = FastAPI()
app.include_router(todo_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)