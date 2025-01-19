import json
import httpx
import os
from phi.agent import Agent
from phi.tools.serpapi_tools import SerpApiTools
from phi.model.google import Gemini
from phi.model.huggingface import HuggingFaceChat

def search_web(text: str):
    # agent = Agent(model=GeminiOpenAIChat(api_key=os.getenv('GOOGLE_API_KEY'),max_tokens=2000))
    agent = Agent(tools=[SerpApiTools()],
                   model=Gemini())
    response = agent.run(text)
    return  str(response.content)


def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)


def hacker_news_agent(text):
    agent = Agent(tools=[get_top_hackernews_stories], show_tool_calls=True, markdown=True, model=HuggingFaceChat(
        id="meta-llama/Meta-Llama-3-8B-Instruct",
        max_tokens=4096
        ))
    response = agent.run(text)
    print(response)
    return  str(response.content)



