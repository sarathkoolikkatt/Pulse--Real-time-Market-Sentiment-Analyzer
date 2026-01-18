from fastapi import FastAPI
from pydantic import BaseModel
from model.sentiment_model import predict_sentiment

app = FastAPI(title="Pulse – Market Sentiment API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Pulse API is running"}

@app.post("/predict")
def predict(input_data: TextInput):
    result = predict_sentiment(input_data.text)
    return result
