<div align="center">

# 🌞 Your Morning Buddy

### An AI-powered personal morning assistant — motivation, weather, news, and a smart day plan

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![OpenWeather](https://img.shields.io/badge/OpenWeather-EB6E4B?style=flat-square&logo=openweathermap&logoColor=white)

</div>

---

## 📖 Overview

**Your Morning Buddy** is a single-screen assistant that gives your morning a running start. Built with **Streamlit** and **Google Gemini**, it bundles four things you'd otherwise check across four apps: a motivational thought, real-time weather with practical suggestions, news summarized to your interests, and an AI-generated day plan for any city — all in one place, all conversational.

---

## 📑 Table of Contents

- [Features](#-features)
- [Tech stack](#-tech-stack)
- [Installation](#-installation)
- [API keys](#-api-keys)
- [Usage](#-usage)

---

## ✨ Features

### 🧠 Thought for the Day
Start with an inspiring, ambition-driven quote rooted in positivity.

### 🌦️ Weather of Your City
Real-time weather for any city via the **OpenWeather API**:
- City & country, temperature (°C) and feels-like
- Humidity, wind speed, sunrise & sunset
- Friendly outfit/carry suggestions based on conditions (umbrella, jacket, sunglasses)

### 🗞️ News by Interest
Trending headlines for the topics you care about (tech, sports, politics…), pulled from **NewsAPI** and summarized into crisp, human-like briefs by Gemini.

### 🧭 Smart Planner
An AI day-itinerary planner powered by **Gemini + Google Search grounding + SerpAPI** that builds a personalized plan for any city:
- Weather forecast
- Top tourist attractions
- Upcoming local events
- An optimized Morning → Afternoon → Evening timeline
- Restaurant and activity recommendations

---

## 🛠️ Tech stack

| Component | Technology |
|-----------|------------|
| **UI** | Streamlit |
| **LLM** | Google Gemini (`google.genai`) with Google Search grounding |
| **Weather** | OpenWeather API |
| **News** | NewsAPI |
| **Events** | SerpAPI |
| **Config** | python-dotenv |

---

## 📦 Installation

```bash
git clone https://github.com/ydvlalit03/Your-Morning-Buddy.git
cd Your-Morning-Buddy
pip install -r requirements.txt
```

---

## 🔑 API keys

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
OPENWEATHER_API_KEY=your_openweather_key_here
NEWS_API_KEY=your_newsapi_key_here
SERPAPI_KEY=your_serpapi_key_here
```

---

## 🚀 Usage

```bash
streamlit run app.py
```

Open the local URL Streamlit prints, pick your city and interests, and start your morning.
