from fastapi import FastAPI
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"

PARAMS = {
    "q": "stock market",
    "language": "en",
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY,
    "pageSize": 10
}

# developing

@app.get("/fetch-news")
def fetch_news():
    response = requests.get(NEWS_API_URL, params=PARAMS)
    data = response.json()

    # Timestamp for versioning
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"news_{timestamp}.json"

    # Save news content to JSON file
    with open(file_path, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return {"status": "success", "file": file_path, "total_articles": len(data.get("articles", []))}


# developing

@app.get("/latest-news")
def latest_news():
    # Load most recent news file (simplified for now)
    try:
        with open("latest_news.json", "r", encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"error": "No news file found. Please call /fetch-news first."}
