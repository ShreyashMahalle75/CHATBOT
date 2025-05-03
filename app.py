import streamlit as st
import pandas as pd
import google.generativeai as genai

# Load dataset
import pandas as pd

url = "https://drive.google.com/file/d/1tap-0TxL4r2aC3yROyOvo1ao0mUz2NcB/view?usp=sharing"  # replace with your actual ID 
df = pd.read_csv(url)

# Optional: print the first few rows to check
print(df.head())

# Configure Gemini API
genai.configure(api_key=st.secrets["AIzaSyDjn79AMW-V9C2nPUyALtNFlgK6OJfIZJI"])
model = genai.GenerativeModel("gemini-pro")

# Chatbot interaction
st.title("Healthcare Chatbot")
user_input = st.text_input("Describe your symptom (e.g., 'I have fever')")

if user_input:
    gender = st.selectbox("Select your gender", ["Male", "Female"])
    age = st.number_input("Enter your age", min_value=1, max_value=120)
    weight = st.number_input("Enter your weight (kg)", min_value=1)

    # Match symptom
    matched = df[df["Symptom"].str.contains(user_input.lower(), case=False)]

    if not matched.empty:
        disease = matched.iloc[0]["Disease"]
        treatment = matched.iloc[0]["Treatment"]

        prompt = f"The patient is a {gender.lower()} aged {age} years, weighing {weight} kg, experiencing {user_input}. The diagnosis is {disease}. Provide a detailed treatment plan and prescription."

        response = model.generate_content(prompt)
        st.subheader("Suggested Diagnosis:")
        st.write(disease)
        st.subheader("Treatment Plan:")
        st.write(response.text)
    else:
        st.error("Sorry, symptom not found in the dataset.")
