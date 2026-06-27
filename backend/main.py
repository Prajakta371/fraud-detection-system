from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import joblib
import json
import io
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "fraud_model.pkl"))
with open(os.path.join(BASE_DIR, "threshold.json")) as f:
    threshold = json.load(f)["threshold"]

app = FastAPI(
    title="FraudShield API",
    description="Production-ready financial fraud detection system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Fraud Detection API is running!"}

@app.post("/batch-predict")
async def batch_predict(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    df["Amount_Scaled"] = StandardScaler().fit_transform(df[["Amount"]])
    df["Time_Scaled"] = StandardScaler().fit_transform(df[["Time"]])
    df = df.drop(["Amount", "Time"], axis=1)

    if "Class" in df.columns:
        df = df.drop("Class", axis=1)

    proba = model.predict_proba(df)[:, 1]
    predictions = (proba >= threshold).astype(int)

    results = []
    for i, (pred, prob) in enumerate(zip(predictions, proba)):
        results.append({
            "transaction_id": i + 1,
            "fraud_probability": round(float(prob), 4),
            "prediction": "FRAUD" if pred == 1 else "LEGIT",
            "risk_level": "HIGH" if prob >= 0.8 else "MEDIUM" if prob >= 0.5 else "LOW"
        })

    fraud_count = sum(predictions)
    return {
        "total_transactions": len(predictions),
        "fraud_detected": int(fraud_count),
        "legit_transactions": int(len(predictions) - fraud_count),
        "fraud_rate": round(float(fraud_count / len(predictions) * 100), 2),
        "results": results
    }