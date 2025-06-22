# 🗞️ News Aggregator Agents

A modular and intelligent agent-based system designed to collect and summarize news content across multiple platforms including newspapers, social media, recent articles, and YouTube using Google's **ADK** (`google.adk`) and **Gemini models**.

---

## 🤖 Agents Overview

### 📰 1. CollectNewsFromNewspaperAgent
- **Purpose:** Fetches news stories from online newspapers
- **Tool Used:** `google_search_grounding`

### 💬 2. CollectNewsFromSocialMediaAgent
- **Purpose:** Gathers trending news from social media platforms like Facebook, Twitter, and X
- **Tool Used:** `google_search_grounding`

### 📝 3. CollectNewsFromRecentArticlesAgent
- **Purpose:** Searches for the latest articles related to a given topic
- **Tool Used:** `google_search_grounding`

### 📺 4. CollectNewsFromYoutubeAgent
- **Purpose:** Identifies relevant YouTube content based on a news topic
- **Tool Used:** `google_search_grounding`

### 🧠 5. NewsAggregatorAgent (Root Agent)
- **Purpose:** Delegates user queries to appropriate sub-agents and combines responses for aggregated news insight

---

## 📁 File Structure

```
project/
├── __init__.py
├── search.py              # Contains search configuration and tool logic
├── agent.py               # Defines the agents and their orchestration
├── .env                   # Environment variable configuration
└── README.md              # Project documentation
```

---

## 🛠️ Installation

Ensure you have Python 3.10+ and install required packages:

```bash
pip install google-adk google.generativeai openai
```

📘 First time using ADK? Follow the [Google ADK Quick Start Guide](https://google.github.io/adk-docs/get-started/quickstart/).

---

## ⚙️ Environment Variables

Create a `.env` file with your credentials:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_REGION=your_region
GOOGLE_CLOUD_LOCATION=your_location
```

---

## 🚀 Usage

Import and execute the root agent with a query topic:

```python
from . import agent

response = root_agent.run("Latest updates on climate change")
print(response)
```

✅ Ensure `google_search_grounding` is properly configured in `search.py`.

---

## 🔐 License

This project is licensed under the [MIT License](./LICENSE.md).