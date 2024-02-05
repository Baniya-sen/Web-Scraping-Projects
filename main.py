import requests

API_KEY = "your_openweather_api_key"
Lat = 0.00  # Your lat
Long = 0.00  # Your long

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?"
                            f"lat={Lat}&lon={Long}&appid={API_KEY}&units=metric&cnt={4}")
response.raise_for_status()

for weather in response.json()["list"]:
    if weather["weather"][0]["id"] < 700:
        print("Bring an umbrella!")
        break
