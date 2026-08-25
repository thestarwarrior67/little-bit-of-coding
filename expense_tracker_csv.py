import streamlit as st
import pandas as pd

st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("💰 Expense Tracker (CSV)")

# Load data
df = pd.read_csv("expense.csv")

# Sidebar filter
category = st.sidebar.selectbox("Select Category", ["All", "Food", "Transport", "Entertainment", "Grocery"])

if category == "All":
    filtered_df = df
else:
    filtered_df = df[df[category.lower()] > 0]

# Display table
st.dataframe(filtered_df)

# Totals
total_food = df["food"].sum()
total_transport = df["transport"].sum()
total_entertainment = df["entertainment"].sum()
total_grocery = df["grocery"].sum()

st.metric("🍽️ Food", f"₹{total_food}")
st.metric("🚗 Transport", f"₹{total_transport}")
st.metric("🎬 Entertainment", f"₹{total_entertainment}")
st.metric("🛒 Grocery", f"₹{total_grocery}")

# Monthly chart
df["month"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m")
monthly = df.groupby("month")[["food", "transport", "entertainment", "grocery"]].sum().sum(axis=1)
st.bar_chart(monthly)