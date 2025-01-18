import os
from phi.agent import Agent
from phi.tools.serpapi_tools import SerpApiTools
from phi.model.google.gemini_openai import GeminiOpenAIChat
# from phi.model.huggingface import HuggingFaceChat


def search_web(text: str):
    agent = Agent(model=GeminiOpenAIChat(api_key=os.getenv('GOOGLE_API_KEY'),max_tokens=2000))
    # agent = Agent(tools=[SerpApiTools(api_key=os.getenv('SERPAPI_API_KEY'))],
    #                model=GeminiOpenAIChat(api_key=os.getenv('GOOGLE_API_KEY'),max_tokens=2000))
    # agent.print_response(text)
    response = agent.run(text)
    print("test"*10,response)
    return  str(response.content)
