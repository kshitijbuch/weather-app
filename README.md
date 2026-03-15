# Weather App — Setup & Deployment Guide

## Folder Structure
```
weather_app/
├── app.py                    ← Main app
├── requirements.txt          ← Dependencies
├── .streamlit/
│   └── secrets.toml          ← Your API key (never share this file)
└── README.md
```

---

## Step 1 — Get Free OpenWeatherMap API Key

1. Go to https://openweathermap.org/api
2. Click "Sign Up" — free account
3. Go to "API Keys" tab in your account
4. Copy your default API key (or create a new one)
5. Note: takes up to 2 hours to activate after signup

---

## Step 2 — Add API Key Locally

Edit the file: `.streamlit/secrets.toml`

```toml
OPENWEATHER_API_KEY = "paste_your_key_here"
```

---

## Step 3 — Run Locally (Test First)

Open Anaconda Prompt, activate jobagent:
```cmd
conda activate jobagent
cd "C:\Users\Kshitij Buch\weather_app"
streamlit run app.py
```

Opens at http://localhost:8501
Test it — search Mumbai, Delhi, London etc.

---

## Step 4 — Deploy Free on Streamlit Cloud (Share with Family)

This gives you a public link like: https://kshitij-weather.streamlit.app

1. Create free account at https://github.com (if you don't have one)
2. Create a new repository called `weather-app`
3. Upload these files to the repo:
   - app.py
   - requirements.txt
   (Do NOT upload secrets.toml — keep that private)

4. Go to https://share.streamlit.io
5. Sign in with GitHub
6. Click "New app" → select your repo → select app.py → Deploy

7. After deployment, go to App Settings → Secrets
8. Add your API key there:
   ```
   OPENWEATHER_API_KEY = "your_key_here"
   ```

9. Share the link with family — works on any phone browser!

---

## Features
- 🌤️ Current weather with emoji icons
- 🌡️ Temperature + feels like
- 💧 Humidity, wind speed & direction
- 👁️ Visibility, pressure
- 🌅 Sunrise & sunset times
- 📅 5-day forecast
- 🔍 Search any city worldwide
- 📱 Mobile-friendly dark UI

---

## Default City
App opens with Mumbai by default.
To change: edit line in app.py:
```python
st.session_state.city = "Mumbai"  # change to your city
```
