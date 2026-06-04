# Your Morning Buddy

An **AI-powered personal morning assistant** built with Python, Streamlit, and Google Gemini. It kickstarts your day with motivation, awareness, and smart planning — all in one place.

---

## Features

### Thought for the Day
An inspiring, ambition-driven quote to start your morning.

### Weather of Your City
Real-time weather for any city via the OpenWeather API — temperature, feels-like, humidity, wind, sunrise/sunset, plus friendly outfit/carry suggestions (umbrella, jacket, sunglasses).

### News by Interest
Trending headlines for your chosen topics (tech, sports, politics…), summarized into crisp, human-like briefs with NewsAPI + Gemini.

### Smart Planner
An AI daily-itinerary planner (Gemini + Google Search grounding + SerpAPI) that builds a personalized day plan for any city — weather, top attractions, local events, an optimized Morning → Afternoon → Evening timeline, and food/activity recommendations.

---

## Tech Stack

- **UI**: Streamlit
- **LLM**: Google Gemini (`google.genai`) with Google Search grounding
- **Weather**: OpenWeather API
- **News**: NewsAPI
- **Events**: SerpAPI
- **Config**: python-dotenv

---

## Quick Start

```bash
pip install -r requirements.txt
```

Create a `.env` file with your keys:

```
GOOGLE_API_KEY=your_google_api_key
OPENWEATHER_API_KEY=your_openweather_key
NEWS_API_KEY=your_newsapi_key
SERPAPI_KEY=your_serpapi_key
```

Run the app:

```bash
streamlit run app.py
```
