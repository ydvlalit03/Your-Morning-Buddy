# 🌞 Your Morning Buddy

Your Morning Buddy is an **AI-powered personal morning assistant** built with Python, Streamlit, and Google Gemini.  
It’s designed to kickstart your day with **motivation, awareness, and smart planning** — all in one place.

---

## ✨ Features

### 🧠 Thought for the Day
Start your morning with an inspiring quote rooted in positivity and ambition.  
> Example: “Rooted in Yadav values, driven by ambition. Believing in hard work and the power of dreams.”

---

### 🌦️ Get Weather of Your City
Get **real-time weather updates** for any city using the **OpenWeather API**.  
Includes:
- City & Country name  
- Temperature (in °C)  
- Feels-like temperature  
- Humidity, wind speed  
- Sunrise & Sunset times  
- Friendly outfit/carry suggestions based on weather (e.g., umbrella, jacket, sunglasses)

---

### 🗞️ News by Interest
Fetch trending news headlines based on your interests — like *technology, sports, or politics*.  
The app uses **NewsAPI** and **Gemini summarization** to generate crisp, human-like summaries.

---

### 🧭 Smart Planner
An intelligent **AI-based daily itinerary planner** powered by **Gemini + Google Search + SerpAPI**.  
It creates a personalized day plan for your chosen city that includes:
- Weather forecast  
- Top tourist attractions  
- Upcoming local events  
- Optimized timeline (Morning → Afternoon → Evening)  
- Restaurant and activity recommendations  

---

## ⚙️ Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Frontend UI | Streamlit |
| LLM | Google Gemini (via `google.genai`) |
| Weather Data | OpenWeather API |
| News Data | NewsAPI |
| Events Data | SerpAPI |
| Smart Forecasting | Gemini with Google Search grounding |
| Environment Config | python-dotenv |

---

## 🔐 API Keys Required

Create a `.env` file in your project root:

```bash
GOOGLE_API_KEY=your_google_api_key_here

