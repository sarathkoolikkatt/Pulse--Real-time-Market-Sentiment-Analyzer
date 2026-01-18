from transformers import pipeline

# Load FinBERT sentiment model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert",
    tokenizer="ProsusAI/finbert",
    truncation=True,
    max_length=512
)

def predict_sentiment(text):
    """
    Predict sentiment of financial text using FinBERT.
    Text is truncated to 512 tokens to avoid model errors.
    """
    try:
        result = sentiment_pipeline(text)[0]
        return {
            "label": result["label"],
            "score": round(result["score"], 4)
        }
    except Exception as e:
        return {
            "label": "error",
            "score": 0.0
        }
