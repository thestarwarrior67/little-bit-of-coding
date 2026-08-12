import streamlit as st
import pandas as pd
st.title("📊 Student Dashboard")
df = pd.read_csv("student.csv")
st.dataframe(df)

def search_student(df, search):
    if search == "":
        return df
        return df[df['Name'].str.contains(search, case=False, na=False)]

#filters

def filter_by_city(df, city):
    if city == "all":
        return df
    return df[df["City"].str.contains(city, case=False, na=False)]

def filter_by_grade(df, grade):
    if grade == "all":
        return df
    return df[df["Grade"].str.contains(grade, case=False, na=False)]

def filter_by_subject(df, subject):
    if subject == "all":
        return df
    return df[df["Subject"].str.contains(subject, case=False, na=False)]
    
    avg_grade = df["Grade"].mean()
    st.metric("Average Grade", round(avg_grade, 2))

    #sorting

    sort_by = st.selectbox("Sort by", ["Name", "Age", "Score", "Grade"])
order = st.radio("Order", ["Ascending", "Descending"])

col1, col2 = st.columns(2)
col1.metric("📊 Average Score", round(df["Score"].mean(), 1))
col2.metric("📅 Average Age", round(df["Age"].mean(), 1))

st.bar_chart(df, x="Name", y="Score")