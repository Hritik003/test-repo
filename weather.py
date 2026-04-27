import os

# Retrieve the Weather API key from environment variables
API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("WEATHER_API_KEY environment variable is not set.")

# Example function: get weather data using the API key
import requests

def get_weather(city: str):
    """Fetch weather data for a given city.

    Args:
        city (str): Name of the city.

    Returns:
        dict: JSON response from the weather API.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)
    city_name = " ".join(sys.argv[1:])
    data = get_weather(city_name)
    print(data)
