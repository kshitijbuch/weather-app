"""
Weather App — Built with Streamlit + OpenWeatherMap API
Share with family via Streamlit Cloud link
"""

import streamlit as st
import requests
from datetime import datetime
import os

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS for mobile-friendly look ───────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        min-height: 100vh;
    }

    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 500px;
    }

    /* Search input */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.95) !important;
        border: 2px solid rgba(255,255,255,0.6) !important;
        border-radius: 50px !important;
        color: #1a1a2e !important;
        font-size: 18px !important;
        text-align: center !important;
        padding: 12px 20px !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.5) !important;
    }
    .stTextInput > label {display: none;}

    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #e94560, #0f3460) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        width: 100% !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        padding: 12px !important;
        margin-top: -8px !important;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(233,69,96,0.4) !important;
    }

    /* Cards */
    .weather-card {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 24px;
        padding: 28px;
        margin: 16px 0;
        text-align: center;
    }

    .city-name {
        font-size: 32px;
        font-weight: 700;
        color: white;
        margin: 0;
        letter-spacing: 1px;
    }

    .weather-desc {
        font-size: 18px;
        color: rgba(255,255,255,0.7);
        text-transform: capitalize;
        margin: 4px 0 16px 0;
    }

    .big-temp {
        font-size: 80px;
        font-weight: 300;
        color: white;
        line-height: 1;
        margin: 10px 0;
    }

    .feels-like {
        font-size: 15px;
        color: rgba(255,255,255,0.6);
        margin-bottom: 20px;
    }

    .weather-icon {
        font-size: 72px;
        line-height: 1;
        margin: 10px 0;
    }

    /* Stats row */
    .stats-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 20px;
        margin: 12px 0;
    }

    .stat-item {
        text-align: center;
        padding: 8px;
    }

    .stat-icon { font-size: 28px; }
    .stat-value {
        font-size: 20px;
        font-weight: 700;
        color: white;
        margin: 4px 0 2px 0;
    }
    .stat-label {
        font-size: 13px;
        color: rgba(255,255,255,0.5);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Forecast */
    .forecast-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 20px 16px;
        margin: 12px 0;
    }

    .forecast-title {
        font-size: 13px;
        color: rgba(255,255,255,0.5);
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 16px;
        text-align: left;
    }

    .forecast-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid rgba(255,255,255,0.07);
    }
    .forecast-row:last-child { border-bottom: none; }

    .forecast-day { color: white; font-size: 15px; font-weight: 500; width: 80px; }
    .forecast-icon { font-size: 22px; width: 36px; text-align: center; }
    .forecast-desc { color: rgba(255,255,255,0.6); font-size: 14px; flex: 1; text-align: center; text-transform: capitalize; }
    .forecast-temps { text-align: right; }
    .forecast-high { color: white; font-size: 16px; font-weight: 700; }
    .forecast-low { color: rgba(255,255,255,0.45); font-size: 14px; margin-left: 6px; }

    /* App title */
    .app-title {
        text-align: center;
        color: rgba(255,255,255,0.9);
        font-size: 26px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 24px;
    }

    /* Error */
    .error-box {
        background: rgba(233,69,96,0.15);
        border: 1px solid rgba(233,69,96,0.4);
        border-radius: 16px;
        padding: 16px;
        text-align: center;
        color: #ff6b8a;
        font-size: 16px;
        margin: 16px 0;
    }

    /* Last updated */
    .last-updated {
        text-align: center;
        color: rgba(255,255,255,0.3);
        font-size: 12px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ── API Config ────────────────────────────────────────────────────────────────
API_KEY = os.getenv("OPENWEATHER_API_KEY", st.secrets.get("OPENWEATHER_API_KEY", ""))
BASE_URL = "https://api.openweathermap.org/data/2.5"

# ── Weather icon mapping ──────────────────────────────────────────────────────
def get_weather_emoji(icon_code: str) -> str:
    mapping = {
        "01d": "☀️", "01n": "🌙",
        "02d": "⛅", "02n": "🌙",
        "03d": "☁️", "03n": "☁️",
        "04d": "☁️", "04n": "☁️",
        "09d": "🌧️", "09n": "🌧️",
        "10d": "🌦️", "10n": "🌧️",
        "11d": "⛈️", "11n": "⛈️",
        "13d": "❄️", "13n": "❄️",
        "50d": "🌫️", "50n": "🌫️",
    }
    return mapping.get(icon_code, "🌡️")

def get_wind_direction(degrees: float) -> str:
    dirs = ["N","NE","E","SE","S","SW","W","NW"]
    return dirs[round(degrees / 45) % 8]

# ── API calls ─────────────────────────────────────────────────────────────────
def get_current_weather(city: str):
    url = f"{BASE_URL}/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    r = requests.get(url, params=params, timeout=10)
    if r.status_code == 200:
        return r.json(), None
    elif r.status_code == 404:
        return None, f"City '{city}' not found. Please check spelling."
    elif r.status_code == 401:
        return None, "Invalid API key. Please check your OpenWeatherMap API key."
    else:
        return None, f"Error fetching weather: {r.status_code}"

def get_forecast(city: str):
    url = f"{BASE_URL}/forecast"
    params = {"q": city, "appid": API_KEY, "units": "metric", "cnt": 40}
    r = requests.get(url, params=params, timeout=10)
    if r.status_code == 200:
        return r.json(), None
    return None, "Could not fetch forecast."

def parse_daily_forecast(forecast_data):
    """Extract one entry per day (noon reading preferred)."""
    daily = {}
    for item in forecast_data["list"]:
        dt = datetime.fromtimestamp(item["dt"])
        day_key = dt.strftime("%Y-%m-%d")
        if day_key not in daily:
            daily[day_key] = {
                "dt": dt,
                "temps": [],
                "icon": item["weather"][0]["icon"],
                "desc": item["weather"][0]["description"],
            }
        daily[day_key]["temps"].append(item["main"]["temp"])
        # Prefer noon reading for icon/desc
        if dt.hour == 12 or dt.hour == 13:
            daily[day_key]["icon"] = item["weather"][0]["icon"]
            daily[day_key]["desc"] = item["weather"][0]["description"]

    result = []
    for day_key, data in list(daily.items())[1:6]:  # skip today, show next 5
        result.append({
            "day": data["dt"].strftime("%A"),
            "date": data["dt"].strftime("%d %b"),
            "icon": data["icon"],
            "desc": data["desc"],
            "high": round(max(data["temps"])),
            "low": round(min(data["temps"])),
        })
    return result

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown('<div class="app-title">🌤️ WEATHER</div>', unsafe_allow_html=True)

# Search bar
col1, col2 = st.columns([4, 1])
with col1:
    city_input = st.text_input("city", placeholder="Search city...", label_visibility="collapsed")
with col2:
    search_btn = st.button("Go", use_container_width=True)

# Default city
if "city" not in st.session_state:
    st.session_state.city = "Mumbai"

if search_btn and city_input.strip():
    st.session_state.city = city_input.strip()
elif not city_input and not search_btn:
    pass  # use session state default

# ── Check API key ─────────────────────────────────────────────────────────────
if not API_KEY:
    st.markdown("""
    <div class="error-box">
    ⚠️ <b>API Key Missing</b><br><br>
    Add your OpenWeatherMap API key to <code>.streamlit/secrets.toml</code>:<br><br>
    <code>OPENWEATHER_API_KEY = "your_key_here"</code>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ── Fetch & Display ───────────────────────────────────────────────────────────
city = st.session_state.city

with st.spinner(""):
    current, err1 = get_current_weather(city)
    forecast_data, err2 = get_forecast(city)

if err1:
    st.markdown(f'<div class="error-box">❌ {err1}</div>', unsafe_allow_html=True)
    st.stop()

# ── Current Weather Card ──────────────────────────────────────────────────────
temp        = round(current["main"]["temp"])
feels_like  = round(current["main"]["feels_like"])
description = current["weather"][0]["description"]
icon_code   = current["weather"][0]["icon"]
emoji       = get_weather_emoji(icon_code)
country     = current["sys"]["country"]
city_name   = current["name"]

humidity    = current["main"]["humidity"]
wind_speed  = round(current["wind"]["speed"] * 3.6)  # m/s → km/h
wind_deg    = current["wind"].get("deg", 0)
wind_dir    = get_wind_direction(wind_deg)
visibility  = round(current.get("visibility", 0) / 1000, 1)  # m → km
pressure    = current["main"]["pressure"]

sunrise     = datetime.fromtimestamp(current["sys"]["sunrise"]).strftime("%H:%M")
sunset      = datetime.fromtimestamp(current["sys"]["sunset"]).strftime("%H:%M")

st.markdown(f"""
<div class="weather-card">
    <p class="city-name">{city_name}, {country}</p>
    <p class="weather-desc">{description}</p>
    <div class="weather-icon">{emoji}</div>
    <p class="big-temp">{temp}°</p>
    <p class="feels-like">Feels like {feels_like}°C</p>
</div>
""", unsafe_allow_html=True)

# ── Stats Grid ────────────────────────────────────────────────────────────────
st.markdown('<div class="stats-card">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""
    <div class="stat-item">
        <div class="stat-icon">💧</div>
        <div class="stat-value">{humidity}%</div>
        <div class="stat-label">Humidity</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="stat-item">
        <div class="stat-icon">💨</div>
        <div class="stat-value">{wind_speed} km/h</div>
        <div class="stat-label">Wind {wind_dir}</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""
    <div class="stat-item">
        <div class="stat-icon">👁️</div>
        <div class="stat-value">{visibility} km</div>
        <div class="stat-label">Visibility</div>
    </div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)
with c4:
    st.markdown(f"""
    <div class="stat-item" style="background:rgba(255,255,255,0.04);border-radius:16px;padding:14px;">
        <div class="stat-icon">🌅</div>
        <div class="stat-value">{sunrise}</div>
        <div class="stat-label">Sunrise</div>
    </div>""", unsafe_allow_html=True)
with c5:
    st.markdown(f"""
    <div class="stat-item" style="background:rgba(255,255,255,0.04);border-radius:16px;padding:14px;">
        <div class="stat-icon">📊</div>
        <div class="stat-value">{pressure}</div>
        <div class="stat-label">hPa</div>
    </div>""", unsafe_allow_html=True)
with c6:
    st.markdown(f"""
    <div class="stat-item" style="background:rgba(255,255,255,0.04);border-radius:16px;padding:14px;">
        <div class="stat-icon">🌇</div>
        <div class="stat-value">{sunset}</div>
        <div class="stat-label">Sunset</div>
    </div>""", unsafe_allow_html=True)

# ── 5-Day Forecast ────────────────────────────────────────────────────────────
if forecast_data:
    daily = parse_daily_forecast(forecast_data)
    st.markdown("""
    <div style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);
                border-radius:20px;padding:20px 16px;margin:12px 0;">
        <div style="font-size:13px;color:rgba(255,255,255,0.5);text-transform:uppercase;
                    letter-spacing:2px;margin-bottom:16px;">📅 5-Day Forecast</div>
    </div>""", unsafe_allow_html=True)

    for i, d in enumerate(daily):
        emoji_f = get_weather_emoji(d["icon"])
        border = "" if i == len(daily)-1 else "border-bottom:1px solid rgba(255,255,255,0.07);"
        col1, col2, col3, col4 = st.columns([2, 1, 3, 2])
        with col1:
            st.markdown(f"""<div style="color:white;font-size:15px;font-weight:500;padding:8px 0;">
                {d['day'][:3]}<br>
                <span style="font-size:12px;color:rgba(255,255,255,0.4);">{d['date']}</span>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div style='font-size:24px;padding:8px 0;'>{emoji_f}</div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""<div style="color:rgba(255,255,255,0.6);font-size:14px;
                text-transform:capitalize;padding:10px 0;">{d['desc']}</div>""", unsafe_allow_html=True)
        with col4:
            st.markdown(f"""<div style="text-align:right;padding:8px 0;">
                <span style="color:white;font-size:16px;font-weight:700;">{d['high']}°</span>
                <span style="color:rgba(255,255,255,0.45);font-size:14px;margin-left:6px;">{d['low']}°</span>
            </div>""", unsafe_allow_html=True)
        st.markdown(f"<hr style='margin:0;border:none;border-top:1px solid rgba(255,255,255,0.07);{"" if i==len(daily)-1 else ""}'>" if i < len(daily)-1 else "", unsafe_allow_html=True)

# ── Last updated ──────────────────────────────────────────────────────────────
now = datetime.now().strftime("%d %b %Y, %I:%M %p")
st.markdown(f'<div class="last-updated">Last updated: {now}</div>', unsafe_allow_html=True)
