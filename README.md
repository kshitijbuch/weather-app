# 🌤️ Weather App

A clean, mobile-friendly weather app built with Python and Streamlit.  
Get real-time weather + 5-day forecast for any city in the world — instantly.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://weather-app-kjscqpzlkta6pbvimwuyxi.streamlit.app)

> ⭐ **If you find this useful, please star this repo — it helps others find it!**

---

## 🔗 Live Demo

**👉 [https://weather-app-kjscqpzlkta6pbvimwuyxi.streamlit.app](https://weather-app-kjscqpzlkta6pbvimwuyxi.streamlit.app)**

No installation needed — open the link on any phone or browser and search your city.

---

## ✨ Features

- 🌡️ **Current weather** — temperature, feels like, weather condition
- 💧 **Humidity, wind speed & direction**
- 👁️ **Visibility & atmospheric pressure**
- 🌅 **Sunrise & sunset times** in the city's local timezone
- 📅 **5-day forecast** with daily high/low temperatures
- 🔍 **Search any city** worldwide by name
- 📍 **Use My Location** — detect weather via GPS automatically
- 📱 **Mobile-friendly** dark UI — works great on phones
- ⚡ **Fast & lightweight** — just Python + Streamlit + OpenWeatherMap

---

## 📍 How Location Detection Works

The app supports two ways to get weather:

**Option 1 — Search by city name**
Type any city name in the search bar and press **Go**.

**Option 2 — Use GPS location**
1. Click **📍 Use My Location**
2. Allow location access when browser asks
3. Tap the coordinates box that appears to copy
4. Paste into the coordinates field and press **Go**

> Uses OpenWeatherMap reverse geocoding — no third-party location service needed.

---

## 🚀 Run It Yourself Locally

### Prerequisites
- Python 3.9+
- Free [OpenWeatherMap API key](https://openweathermap.org/api) (takes ~2 hours to activate after signup)

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/kshitijbuch/weather-app.git
cd weather-app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
mkdir .streamlit
echo 'OPENWEATHER_API_KEY = "your_key_here"' > .streamlit/secrets.toml

# 4. Run the app
streamlit run app.py
```

Opens at **http://localhost:8501**

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.11 |
| Web Framework | Streamlit |
| Weather Data | OpenWeatherMap API |
| Location | Browser GPS + OWM Reverse Geocoding |
| Hosting | Streamlit Cloud (free) |
| UI | Custom CSS — dark gradient theme |

---

## 📁 Project Structure

```
weather-app/
├── app.py              ← Main application
├── requirements.txt    ← Python dependencies
├── .gitignore          ← Keeps secrets.toml out of GitHub
└── README.md           ← This file
```

> ⚠️ Never commit `.streamlit/secrets.toml` — your API key lives there locally.  
> On Streamlit Cloud, add it via App Settings → Secrets instead.

---

## 🌿 Branches

| Branch | Purpose |
|---|---|
| `main` | Stable production version |
| `feature/geolocation` | GPS location detection feature (merged) |

---

## 🙌 Support This Project

If this helped you or you simply like what you see:

- ⭐ **Star this repo** — one click, means a lot
- 🍴 **Fork it** and build your own version
- 🐛 Found a bug? Open an [issue](https://github.com/kshitijbuch/weather-app/issues)

---

## 👤 Author

**Kshitij Buch** — Mumbai, India  
[github.com/kshitijbuch](https://github.com/kshitijbuch)

---

## 📄 License

Licensed under the [Apache License 2.0](./LICENSE).

You are free to use and modify this project **with attribution** —  
credit must be given to the original author: **Kshitij Buch** (github.com/kshitijbuch).
