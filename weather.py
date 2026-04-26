import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
if not WEATHER_API_KEY:
    raise RuntimeError("Missing WEATHER_API_KEY environment variable")

def get_weather(city):
    # TODO: Implement actual weather fetching logic using the API key
    print(f"Fetching weather for {city} using API key {WEATHER_API_KEY}")
