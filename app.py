import requests
import sys
from dotenv import dotenv_values

config = dotenv_values(".env")

news_api_key = config["NEWS_API_KEY"]
query = {
    "q": "bard ai"
}
endpoint = "https://newsapi.org/v2/everything"
headers = {
    "x-api-key": news_api_key,
}

if __name__ == '__main__':
    print(f"Starting...")
    news_feed = requests.get(endpoint, headers=headers, params=query)
    print(f"Newsfeed {news_feed.json()}")
