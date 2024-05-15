from fastapi import FastAPI
from .routers import health_check


app = FastAPI(
    title = "Assistente IA"
)


app.include_router(health_check.router)