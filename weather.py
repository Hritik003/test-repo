import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(location):
    """
    Fetch weather data for the given location using the stored API key.
    """
    import requests
    params = {
        "location": location,
        "key": WEATHER_API_KEY,
        "units": "metric",
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    response.raise_for_status()
    return response.json()
