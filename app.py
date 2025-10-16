import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("StudentsPerformance.csv")
    return df

df = load_data()

# Title
st.title("🎓 Student Performance Dashboard")
st.markdown("This dashboard provides insights into student performance based on various demographic factors.")  

# Sidebar filters
st.sidebar.header("Filter Options")
gender = st.sidebar.multiselect("Select Gender", df["gender"].unique())
tesr = st.sidebar.multiselect("Select Test Preparation Course", df["test preparation course"].unique())
education = st.sidebar.multiselect("Select Parental Level of Education", df["parental level of education"].unique())

# Apply filters
filtered_df = df.copy()
if gender:
    filtered_df = filtered_df[filtered_df["gender"].isin(gender)]
if tesr:
    filtered_df = filtered_df[filtered_df["test preparation course"].isin(tesr)]
if education:
    filtered_df = filtered_df[filtered_df["parental level of education"].isin(education)]

# Show data
st.dataframe(filtered_df.head())

# Visualization
st.subheader("Average Math Score by Gender")
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(data=filtered_df, x="gender", y="math score", estimator="mean", ci=None, ax=ax)
st.pyplot(fig)
