import requests
import pandas as pd
from datetime import datetime
import time

headers = {
    "User-Agent": "PulseSentimentAnalyzer/1.0"
}

subreddits = [
    "stocks",
    "wallstreetbets",
    "investing",
    "StockMarket"
]

rows = []

for subreddit in subreddits:
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=50"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"⚠ Failed to fetch r/{subreddit}")
        continue

    data = response.json()

    for post in data["data"]["children"]:
        post_data = post["data"]
        text = post_data.get("title", "") + " " + post_data.get("selftext", "")

        if text.strip():
            rows.append([
                "reddit",
                subreddit,
                text,
                datetime.fromtimestamp(post_data["created_utc"])
            ])

    time.sleep(2)  # polite delay

df = pd.DataFrame(
    rows,
    columns=["platform", "source", "text", "timestamp"]
)

df.to_csv("data/reddit_raw_data.csv", index=False)

print(" Reddit JSON data collected successfully")
print(f"Total rows collected: {len(df)}")
