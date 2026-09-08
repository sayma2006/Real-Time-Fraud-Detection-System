from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="Real-Time Fraud Detection API",
    description="XGBoost based credit card fraud detection system",
    version="1.0"
)

model = joblib.load(
    "credit_card_fraud_xgboost.pkl"
)


class Transaction(BaseModel):

    amount: float
    transaction_hour: int
    merchant_category: str
    foreign_transaction: int
    location_mismatch: int
    device_trust_score: int
    velocity_last_24h: int
    cardholder_age: int


@app.get("/")
def home():

    return {
        "message": "Real-Time Fraud Detection API is running"
    }


@app.post("/predict")
def predict(transaction: Transaction):

    data = pd.DataFrame(
        [transaction.model_dump()]
    )

    probability = float(
        model.predict_proba(data)[0][1]
    )

    prediction = int(
        probability >= 0.5
    )

    result = (
        "Fraud"
        if prediction == 1
        else "Genuine"
    )

    return {
        "prediction": prediction,
        "result": result,
        "fraud_probability": probability
    }
