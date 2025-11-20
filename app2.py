import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🏠 Boston Housing Data Analysis App")

uploaded_file = st.file_uploader("Upload your Boston Housing CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # Show dataset
    st.subheader("🔹 First 10 Rows")
    st.write(df.head(10))

    st.subheader("🔹 Column Names")
    st.write(df.columns.tolist())

    st.subheader("🔹 Summary Statistics")
    st.write(df.describe())

    st.subheader("🔹 Shape (Rows, Columns)")
    st.write(df.shape)

    st.subheader("🔹 Missing Values")
    st.write(df.isnull().sum())

    # Filtering operations
    st.header("📌 Filtering")

    # Houses with price > 30
    if "medv" in df.columns:
        st.subheader("Houses with Price > 30 (medv > 30)")
        st.write(df[df["medv"] > 30])
    else:
        st.warning("medv column not found. Please check your CSV header.")

    # Houses with more than 6 rooms
    if "rm" in df.columns:
        st.subheader("Houses with More Than 6 Rooms (rm > 6)")
        st.write(df[df["rm"] > 6])
    else:
        st.warning("rm column not found.")

    # Low crime rate
    if "crim" in df.columns:
        st.subheader("Low crime Rate (crim < 0.1)")
        st.write(df[df["crim"] < 0.1])
    else:
        st.warning("crim column not found.")

    # Grouping
    st.header("📌 Grouping")

    if "rm" in df.columns and "medv" in df.columns:
        st.subheader("Average Price by Number of Rooms")
        st.write(df.groupby("rm")["medv"].mean())
    else:
        st.warning("Cannot group because rm or medv missing.")

    # Visualization
    st.header("📊 Visualization")

    if "rm" in df.columns and "medv" in df.columns:
        st.subheader("Rooms vs Price Scatter Plot")

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(df["rm"], df["medv"])
        ax.set_xlabel("Rooms (rm)")
        ax.set_ylabel("House Price (medv)")
        ax.set_title("Rooms vs Price Scatter Plot")
        st.pyplot(fig)
    else:
        st.warning("Cannot show scatter plot because rm or medv missing.")
else:
    st.info("Please upload a CSV file to begin.")
