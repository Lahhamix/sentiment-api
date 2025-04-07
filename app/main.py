from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load the model
model = joblib.load("app/model.joblib")

# FastAPI app
app = FastAPI(title="Simple Sentiment API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the Simple Sentiment API"}

@app.post("/predict")
def predict_sentiment(data: TextInput):
    prediction = model.predict([data.text])[0]
    sentiment = "positive" if prediction == 1 else "negative"
    return {"input": data.text, "sentiment": sentiment}
@app.get("/health")
def health_check():
    return {"status": "API is up and running"}
