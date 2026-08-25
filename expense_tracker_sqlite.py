import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("💰 Expense Tracker (SQLite)")

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        food INTEGER,
        transport INTEGER,
        entertainment INTEGER,
        grocery INTEGER
    )
''')
conn.commit()

#data load
df = pd.read_sql_query("SELECT * FROM expenses", conn)

# Sidebar filter
category = st.sidebar.selectbox("Select Category", ["All", "Food", "Transport", "Entertainment", "Grocery"])

if category == "All":
    filtered_df = df
else:
    filtered_df = df[df[category.lower()] > 0]

st.dataframe(filtered_df)

#total
cursor.execute("SELECT SUM(food), SUM(transport), SUM(entertainment), SUM(grocery) FROM expenses")
total_food, total_transport, total_entertainment, total_grocery = cursor.fetchone()

st.metric("🍽️ Food", f"₹{total_food or 0}")
st.metric("🚗 Transport", f"₹{total_transport or 0}")
st.metric("🎬 Entertainment", f"₹{total_entertainment or 0}")
st.metric("🛒 Grocery", f"₹{total_grocery or 0}")

#chart
df["month"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m")
monthly = df.groupby("month")[["food", "transport", "entertainment", "grocery"]].sum().sum(axis=1)
st.bar_chart(monthly)

#ADD NEW EXPENSE
with st.sidebar.form("add_expense"):
    st.subheader("➕ Add New Expense")
    date = st.date_input("Date")
    food = st.number_input("Food", min_value=0, step=1)
    transport = st.number_input("Transport", min_value=0, step=1)
    entertainment = st.number_input("Entertainment", min_value=0, step=1)
    grocery = st.number_input("Grocery", min_value=0, step=1)
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        cursor.execute('''
            INSERT INTO expenses (date, food, transport, entertainment, grocery)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, food, transport, entertainment, grocery))
        conn.commit()
        st.success("✅ Expense added!")
        st.rerun()

conn.close()