from fastapi import FastAPI
from routers import words


app = FastAPI(servers=[{"url": "http://127.0.0.1:8080", "description": "dev"}])
app.include_router(words.router)
