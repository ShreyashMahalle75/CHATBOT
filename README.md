# Healthcare Chatbot (Gemini)

This is a healthcare chatbot built using Streamlit and Google's Gemini LLM. It reads user symptoms, collects basic information, and recommends treatment based on a public dataset.

## Running Locally
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Set your Gemini API key in `.streamlit/secrets.toml`:
```
[general]
gemini_api_key = "your-api-key-here"
```

3. Run the app:
```
streamlit run app.py
```

## Deployment
You can deploy this app on [Streamlit Cloud](https://streamlit.io/cloud).
