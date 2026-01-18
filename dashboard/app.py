import streamlit as st
import pandas as pd
import time
from nltk.corpus import stopwords
from collections import Counter

# Page Configuration
st.set_page_config(
    page_title="Pulse – Market Sentiment Analyzer",
    layout="wide"
)


st.title("📊 Pulse: Market Sentiment Analyzer")

# Load Data
df = pd.read_csv("data/sentiment_results.csv")

# E3: Sentiment Spike Alert
RECENT_WINDOW = 50
NEGATIVE_THRESHOLD = 0.5

recent_df = df.tail(RECENT_WINDOW)
negative_ratio = recent_df["sentiment"].value_counts(normalize=True).get("negative", 0)

if negative_ratio > NEGATIVE_THRESHOLD:
    st.error(f"🚨 ALERT: Negative sentiment spike detected ({negative_ratio*100:.1f}%)")
else:
    st.success(f"Market sentiment stable (Negative: {negative_ratio*100:.1f}%)")

# Sentiment Distribution
st.subheader("Sentiment Distribution")
sentiment_counts = df["sentiment"].value_counts()
st.bar_chart(sentiment_counts)

# E5: SENTIMENT COMPARISON VIEW
st.subheader("📊 Sentiment Comparison View")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Positive vs Negative Count")
    compare_df = pd.DataFrame({
        "Positive": [sentiment_counts.get("positive", 0)],
        "Negative": [sentiment_counts.get("negative", 0)]
    })
    st.bar_chart(compare_df)

with col2:
    st.markdown("### Neutral Count")
    st.metric(
        label="Neutral Posts",
        value=sentiment_counts.get("neutral", 0)
    )

# E4: Keyword Insights
st.subheader("🔑 Keyword Comparison (Explainability)")

stop_words = set(stopwords.words("english"))

def get_top_keywords(text_series, top_n=10):
    words = []
    for text in text_series:
        for word in text.split():
            if word not in stop_words and len(word) > 2:
                words.append(word)
    return Counter(words).most_common(top_n)

kcol1, kcol2 = st.columns(2)

with kcol1:
    st.markdown("### 😊 Positive Keywords")
    st.write(get_top_keywords(df[df["sentiment"] == "positive"]["clean_text"]))

with kcol2:
    st.markdown("### 😟 Negative Keywords")
    st.write(get_top_keywords(df[df["sentiment"] == "negative"]["clean_text"]))

# Confidence Trend
st.subheader("Sentiment Confidence Over Time")
st.line_chart(df["confidence"])

# Filter by Sentiment
st.subheader("Sample Market Discussions by Sentimen")

selected_sentiment = st.selectbox(
    "Choose sentiment",
    ["positive", "negative", "neutral"]
)

filtered_df = df[df["sentiment"] == selected_sentiment]
st.dataframe(filtered_df[["clean_text", "sentiment", "confidence"]])
