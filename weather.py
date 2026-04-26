import os

from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str) -> str:
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("Missing WEATHER_API_KEY")

    print("Authenticating with API key...")

    # Fake response
    return f"The weather in {city} is sunny \u2600\ufe0f"


if __name__ == "__main__":
    city = "Bangalore"
    weather = get_weather(city)
    print(weather)
