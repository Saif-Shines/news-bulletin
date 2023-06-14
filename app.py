import requests
import sys
from dotenv import dotenv_values

config = dotenv_values(".env")

news_api_key = config["NEWS_API_KEY"]
query = {
    "q": sys.argv[1],
}
endpoint = "https://newsapi.org/v2/everything"
headers = {
    "x-api-key": news_api_key,
}

if __name__ == '__main__':
    print(f"Fetching news")
    news_feed = requests.get(endpoint, headers=headers, params=query)
    news_feed = news_feed.json()
    posts = news_feed["articles"]
    count = 0
    for post in posts:
        count += 1
        print("ℹ", post["title"], "\n🔗", post["url"], "\n---")
        if count == 10:
            print("✅ Enjoy reading top 10 articles")
            break
