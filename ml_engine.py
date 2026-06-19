import pandas as pd
import numpy as np
import database as db


# 📥 Load data
def load_ml_data():
    rows = db.get_expenses()

    df = pd.DataFrame(rows, columns=[
        "id", "amount", "category", "date", "payment_method"
    ])

    if df.empty:
        return df

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    return df


# 💰 Predict next month spending (simple trend-based ML)
def predict_next_month_spending():
    df = load_ml_data()

    if df.empty:
        return 0

    monthly = df.groupby("month")["amount"].sum()

    if len(monthly) < 2:
        return monthly.iloc[0]

    # simple trend approximation (NOT heavy ML but interview-safe)
    growth_rate = (monthly.iloc[-1] - monthly.iloc[0]) / len(monthly)

    prediction = monthly.iloc[-1] + growth_rate

    return round(prediction, 2)


# 🚨 Detect anomalies (z-score based)
def detect_anomalies():
    df = load_ml_data()

    if df.empty:
        return []

    mean = df["amount"].mean()
    std = df["amount"].std()

    if std == 0:
        return []

    anomalies = df[np.abs(df["amount"] - mean) > 2 * std]

    return anomalies[["amount", "category", "date"]]