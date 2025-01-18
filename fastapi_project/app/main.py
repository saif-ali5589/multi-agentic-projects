import os
from fastapi import FastAPI
from app.routers import web_search_controller

app = FastAPI()

app.include_router(web_search_controller.router, prefix="/api", tags=["websearch Routes"])

@app.get("/")
def read_root():
    return {"message": f"Hello, World!"}
