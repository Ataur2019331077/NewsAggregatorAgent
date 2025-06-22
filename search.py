from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from google.adk.tools import google_search

_search_agent = Agent(
    model="gemini-2.0-flash",
    name="GoogleSearchGrounding",
    description="An agent providing Google-search grounding capability",
    instruction=""",
    You are an expert in providing information using Google Search.
    Answer the user's question directly using the google_search grounding tool.
    You may need to provide data from youtube, newspapers, social media, and recent articles.
    Provide a brief but concise response.
    """,
    tools=[google_search],
)

google_search_grounding = AgentTool(agent=_search_agent)