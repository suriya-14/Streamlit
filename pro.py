import streamlit as st
import pandas as pd
import google.generativeai as genai

# 🔐 Set your Gemini API Key
GEMINI_API_KEY = "AIzaSyAm0FRBQK42OaanbpDuD8GXKXfAs7EHbjA"  # Replace with your actual Gemini API key
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI setup
st.set_page_config(page_title="🧠 AI-powered Data Explorer", layout="wide")
st.title("📊 AI-powered Data Explorer")
st.markdown("Upload your *CSV or Excel file, and ask **AI* anything about your data.")

# Upload file
uploaded_file = st.file_uploader("📤 Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read file into DataFrame
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Display preview
    st.subheader("🧾 Data Preview")
    st.dataframe(df.head())

    # Ask questions
    st.subheader("🤖 Ask AI About Your Data")
    user_question = st.text_input("What do you want to know? (e.g., summary, trends, top values)")

    if user_question:
        with st.spinner("Thinking..."):
            # Convert DataFrame to CSV string (for Gemini input)
            csv_data = df.to_csv(index=False)

            # Prompt Gemini with the data and the user's question
            prompt = (
                f"You are a data analyst AI. Here is the data from a file in CSV format:\n\n"
                f"{csv_data}\n\n"
                f"The user asks: {user_question}\n\n"
                f"Please analyze the data and answer clearly. Include insights, trends, or relevant stats. "
                f"If applicable, suggest what the user can explore further."
            )

            # Get Gemini response
            try:
                response = model.generate_content(prompt)
                st.success("✅ Here's the analysis:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"⚠ Gemini API error: {str(e)}")
else:
    st.info("Upload a file to begin.")