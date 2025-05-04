import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key=st.secrets["api_keys"]["google_api_key"])

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

st.title("🩺 Healthcare Chatbot (AI-Powered)")

# Step-by-step form input
with st.form("health_form"):
    symptom = st.text_input("Describe your symptom (e.g., 'I have fever')")
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    age = st.number_input("Enter your age", min_value=1, max_value=120, value=25)
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=200.0, value=60.0)
    submitted = st.form_submit_button("Get Treatment Advice")

# When form is submitted
if submitted:
    with st.spinner("Consulting AI Doctor..."):
        prompt = f"""
        You are a healthcare assistant. Based on the user's input, give a brief diagnosis,
        suggest possible treatments, and recommend prescription medications if appropriate.

        Patient info:
        - Symptom: {symptom}
        - Gender: {gender}
        - Age: {age}
        - Weight: {weight} kg

        Respond in a helpful and friendly tone. If symptoms are serious, advise visiting a doctor.
        """

        try:
            response = model.generate_content(prompt)
            st.markdown("### 🩺 Treatment Recommendation")
            st.write(response.text)
        except Exception as e:
            st.error("Something went wrong while contacting Gemini API.")
            st.exception(e)
