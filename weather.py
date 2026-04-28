import os

# Now we read the API key from environment variable

def get_weather(city: str) -> str:
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("Missing WEATHER_API_KEY")
    # Simulate using the secret
    print("Authenticating with API key...")
    # Fake response
    return f"The weather in {city} is sunny 🌞"

if __name__ == "__main__":
    city = "Bangalore"
    weather = get_weather(city)
    print(weather)