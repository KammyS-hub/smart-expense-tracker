import analytics as a


# 🧠 Generate smart insights
def generate_insights():
    df = a.load_data()

    insights = []

    if df.empty:
        return ["No data available"]

    total_spent = df["amount"].sum()

    top_category = df.groupby("category")["amount"].sum().idxmax()

    avg_spend = df["amount"].mean()

    insights.append(f"Total Money Spent: ₹{total_spent}")
    insights.append(f"Highest Spending Category: {top_category}")
    insights.append(f"Average Expense: ₹{round(avg_spend, 2)}")

    # 🔥 behavior insight
    if total_spent > 1000:
        insights.append("Warning: High spending detected!")

    if avg_spend < 200:
        insights.append("Good job! Controlled spending behavior.")

    return insights