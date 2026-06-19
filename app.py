import streamlit as st
import database as db
import insights as i
import analytics as a
from datetime import date
import ml_engine as m
# --------------------
# INIT DATABASE
# --------------------
db.create_table()

st.title(" Smart Expense Tracker AI")
st.write("Track your expenses and get smart insights instantly")

# --------------------
# ADD EXPENSE SECTION
# --------------------
st.sidebar.header("Add Expense")

amount = st.sidebar.number_input("Amount", min_value=0.0)
category = st.sidebar.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
payment = st.sidebar.selectbox("Payment Method", ["Cash", "UPI", "Card"])
exp_date = st.sidebar.date_input("Date", date.today())

if st.sidebar.button("Add Expense"):
    db.add_expense(amount, category, str(exp_date), payment)
    st.success("Expense added successfully!")

# --------------------
# DATA DISPLAY
# --------------------
rows = db.get_expenses()

if rows:
    df = a.load_data()

    st.subheader(" Insights")
    for ins in i.generate_insights():
        st.write("•", ins)

    st.subheader(" Category Spending")
    st.bar_chart(a.category_wise_spending())

    st.subheader(" Monthly Spending")
    st.line_chart(a.monthly_spending())

    st.subheader(" AI Predictions")

    st.write(" Next Month Spending Prediction:")
    st.write(m.predict_next_month_spending())

    st.write(" Anomalies Detected:")
    st.write(m.detect_anomalies())

else:
    st.info("No expenses yet. Add some from sidebar.")