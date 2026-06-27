# 🛡️ FraudShield — Financial Fraud Detection System

A production-ready fraud detection system that analyzes bank transactions and flags fraudulent ones in real-time using Machine Learning.

## 🔍 What it does
Upload a CSV of bank transactions and FraudShield instantly detects fraud with confidence scores, risk levels, and explainable AI (SHAP).

## 📊 Model Performance
- **ROC-AUC:** 0.9760
- **Fraud Precision:** 92%
- **Fraud Recall:** 81%
- **Algorithm:** XGBoost + SMOTE
- **Explainability:** SHAP values

## 🛠️ Tech Stack
- **ML:** XGBoost, SMOTE, SHAP, Scikit-learn
- **Backend:** FastAPI, Uvicorn
- **Frontend:** HTML, CSS, JavaScript
- **Data:** Kaggle Credit Card Fraud Dataset

## 🚀 How to Run

### 1. Install dependencies
\```bash
pip install fastapi uvicorn xgboost scikit-learn imbalanced-learn shap joblib python-multipart pandas numpy
\```

### 2. Start the backend
\```bash
python -m uvicorn backend.main:app --reload
\```

### 3. Open the frontend
\```bash
cd frontend && python -m http.server 3000
\```
Go to `http://localhost:3000`

## 📁 Project Structure
\```
fraud-detection-system/
├── backend/
│   ├── main.py              
│   ├── fraud_model.pkl      
│   ├── scaler.pkl           
│   └── threshold.json       
├── frontend/
│   └── index.html           
└── fraud_detection_model.ipynb
\```