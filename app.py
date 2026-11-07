import os
import requests
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please enter a city name"}), 400

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    data = requests.get(url, params=params).json()

    if data.get("cod") != 200:
        return jsonify({"error": "City not found"}), 404

    return jsonify({
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
    })

if __name__ == "__main__":
    app.run(debug=True)