# Real-Time Fraud Detection System

## Overview

This project implements a real-time credit card fraud detection system using Machine Learning and FastAPI.

The system uses an XGBoost classification model to predict whether a transaction is fraudulent or genuine.

## Features

- XGBoost-based fraud detection
- Real-time prediction through REST API
- FastAPI deployment
- Fraud probability prediction
- Inference time evaluation
- Memory usage evaluation
- Load testing under different request loads

## Technologies Used

- Python
- XGBoost
- Scikit-learn
- Pandas
- NumPy
- FastAPI
- Uvicorn
- Joblib
- Psutil

## Dataset

The project uses a credit card fraud dataset containing 10,000 transactions:

- Genuine transactions: 9,849
- Fraudulent transactions: 151

## Model Performance

The trained XGBoost model achieved:

- Accuracy: 99.95%
- Precision: 100%
- Recall: 96.67%
- F1 Score: 98.31%
- ROC-AUC: 1.00

## API

The FastAPI application provides:

### GET /

Checks whether the API is running.

### POST /predict

Accepts transaction details and returns:

- Fraud/Genuine prediction
- Fraud probability

## Project Structure

```text
Real-Time-Fraud-Detection-System/
│
├── app.py
├── requirements.txt
├── credit_card_fraud_xgboost.pkl
└── README.md