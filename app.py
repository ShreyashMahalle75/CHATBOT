import streamlit as st
import google.generativeai as genai

# Setup Gemini
genai.configure(api_key=st.secrets["api_keys"]["google_api_key"])

# List available models to ensure 'gemini-pro' exists
available_models = [m.name for m in genai.list_models()]
if 'models/gemini-pro' not in available_models:
    st.error("Gemini Pro model not found in your API access. Please check your API key and permissions.")
    st.stop()

# Load the correct model
model = genai.GenerativeModel(model_name="gemini-pro")

# Streamlit UI
st.title("🧠 Healthcare AI Chatbot (Gemini-powered)")

with st.form("user_form"):
    symptom = st.text_input("🩺 Describe your symptom (e.g., 'I have a fever')")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=200.0, value=60.0)
    submitted = st.form_submit_button("Get Advice")

if submitted:
    st.info("🤖 Thinking...")
    prompt = f"""
    You are a medical AI assistant. A patient has reported the following:

    - Symptom: {symptom}
    - Age: {age}
    - Gender: {gender}
    - Weight: {weight} kg

    Provide:
    1. A likely diagnosis.
    2. Basic treatment suggestions.
    3. Prescription medication if applicable.
    4. Warning signs that require visiting a doctor.
    Use easy-to-understand language.
    """

    try:
        response = model.generate_content(prompt)
        st.success("✅ AI Health Recommendation")
        st.write(response.text)
    except Exception as e:
        st.error("❌ Failed to get response from Gemini API.")
        st.exception(e)
