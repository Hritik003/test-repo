import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("WEATHER_API_KEY not set in environment variables")
    url = f"https://api.weather.com/v3/weather/conditions?city={city}&apiKey={api_key}"
    # TODO: Add request handling and response parsing
    # Placeholder return
    return url
