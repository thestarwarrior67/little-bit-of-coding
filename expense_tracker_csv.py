import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="expense tracker",
    layout="wide"
)

df= pd.read_csv("expense.csv")

category = st.sidebar.selectbox("select category", ["all", "food", "transport", "entertainment", "grocery", "other"])
 
if category == "All":
 filtered_df = df
else:
 filtered_df = df
 filtered_df = df[df[category.lower()] >0]
 