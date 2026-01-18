import pandas as pd
from sentiment_model import predict_sentiment

df = pd.read_csv("data/cleaned_data.csv")

# Drop extremely long text (extra safety)
df = df[df["clean_text"].str.len() < 3000]

sentiments = df["clean_text"].apply(predict_sentiment)

df["sentiment"] = sentiments.apply(lambda x: x["label"])
df["confidence"] = sentiments.apply(lambda x: x["score"])

df.to_csv("data/sentiment_results.csv", index=False)

print("Sentiment analysis completed safely")
