import requests

API_KEY = "724d96eac3b2278b4837772ff1cd4a75"
city = "Delhi"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": city, "appid": API_KEY, "units": "metric"}

response = requests.get(url, params=params)
data = response.json()

if data["cod"] == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"])
else:
    print("Error:", data["message"])