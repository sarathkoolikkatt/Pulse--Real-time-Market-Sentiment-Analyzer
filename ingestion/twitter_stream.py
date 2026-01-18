import tweepy
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

if not BEARER_TOKEN:
    raise ValueError("Bearer token not found. Check .env file")

client = tweepy.Client(bearer_token=BEARER_TOKEN)

QUERY = "tesla OR aapl OR msft -is:retweet"
MAX_RESULTS = 10

response = client.search_recent_tweets(
    query=QUERY,
    max_results=MAX_RESULTS
)

rows = []

if response.data:
    for tweet in response.data:
        rows.append([
            "twitter",
            tweet.text,
            datetime.now()
        ])

df = pd.DataFrame(rows, columns=["platform", "text", "timestamp"])

os.makedirs("data", exist_ok=True)

file_path = "data/raw_data.csv"

if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=False, index=False)
else:
    df.to_csv(file_path, index=False)

print(" Twitter data collected successfully!")
