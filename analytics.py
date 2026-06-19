import pandas as pd
import database as db


# 📥 Load data into DataFrame
def load_data():
    rows = db.get_expenses()

    df = pd.DataFrame(rows, columns=[
        "id", "amount", "category", "date", "payment_method"
    ])

    return df


# 📊 Category-wise spending
def category_wise_spending():
    df = load_data()

    if df.empty:
        return df

    return df.groupby("category")["amount"].sum().sort_values(ascending=False)


# 📈 Monthly spending trend
def monthly_spending():
    df = load_data()

    if df.empty:
        return df

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    return df.groupby("month")["amount"].sum()