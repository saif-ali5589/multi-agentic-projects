import os
from fastapi import FastAPI,Request
from routers import web_search_controller
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files

# Template directory
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/chat")
async def get_chat_page(request: Request):
    """Serve the chat page."""
    return templates.TemplateResponse("chat.html", {"request": request})

app.include_router(web_search_controller.router, prefix="/api", tags=["websearch Routes"])

@app.get("/")
def read_root():
    return {"message": f"Hello, World!"}
