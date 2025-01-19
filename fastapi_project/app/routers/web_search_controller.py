from fastapi import APIRouter
from agents.web_agent import search_web, hacker_news_agent
from schemas.schema import Questions

router = APIRouter()

@router.post("/ask-question")
def web_search(question: Questions):
    print(question)
    if question.type == 'function':
        return hacker_news_agent(question.question)
    return search_web(question.question)