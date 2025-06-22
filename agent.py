import os
import asyncio
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import openai
from google.adk.tools import FunctionTool  # Correct import
from google.adk.tools import google_search
from .search import google_search_grounding

collect_news_from_newspaper = LlmAgent(
    name="CollectNewsFromNewspaperAgent",
    description="An agent that collects news from a specific newspaper.",
    model='gemini-2.0-flash',
    instruction="You are an expert in collecting news from newspapers on a specific news. " \
                "When the user provides a topic, use the 'google_search' tool to find relevant details in various newspapers.",
    tools=[google_search_grounding],
    disallow_transfer_to_peers=False,
)

collect_news_from_social_media = LlmAgent(
    name="CollectNewsFromSocialMediaAgent",
    description="An agent that collects news from social media platforms.",
    model='gemini-2.0-flash',
    instruction="You are an expert in collecting news from social media platforms like facebook, twitter, X and so on for the specific news. " \
                "When the user provides a topic, use the 'google_search' tool to find relevant details in various social media platforms.",
    tools=[google_search_grounding],
    disallow_transfer_to_peers=False,
)

collect_news_from_recent_articles = LlmAgent(
    name="CollectNewsFromRecentArticlesAgent",
    description="An agent that collects news from recent articles.",
    model='gemini-2.0-flash',
    instruction="You are an expert in collecting news from recent articles on a specific news. " \
                "When the user provides a topic, use the 'google_search' tool to find relevant details in various recent articles.",
    tools=[google_search_grounding],
    disallow_transfer_to_peers=False,
)

collect_news_from_youtube = LlmAgent(
    name="CollectNewsFromYoutubeAgent",
    description="An agent that collects news from youtube.",
    model='gemini-2.0-flash',
    instruction="You are an expert in collecting news from youtube on a specific news. " \
                "When the user provides a topic, use the 'google_search' tool to find relevant details in various youtube videos.",
    tools=[google_search_grounding],
    disallow_transfer_to_peers=False,
)


root_agent = LlmAgent(
    name="NewsAggregatorAgent",
    description="An agent that gives update news on the user interested topics.",
    model='gemini-2.0-flash',
    instruction="Your role is to understand the user's request and route it to the most appropriate sub-agent. " \
                "Combine the results from different sources and provide a comprehensive update on the topic.",
    sub_agents=[
        collect_news_from_newspaper,
        collect_news_from_social_media,
        collect_news_from_recent_articles,
        collect_news_from_youtube,
    ],
)