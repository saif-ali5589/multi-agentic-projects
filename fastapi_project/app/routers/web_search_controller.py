from fastapi import APIRouter
from app.agents.web_agent import search_web

router = APIRouter()

@router.get("/websearch")
def web_search(text):
    return search_web(text)