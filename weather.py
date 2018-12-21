import requests
from datetime import date


class Error(Exception):

    def __init__(self, message):
        self.message = message


class WeatherInfo:

    def __init__(self, data):
        self.current_temp = int((data["main"]["temp"] * 1.8)) + 32
        self.high = int((data["main"]["temp_max"] * 1.8)) + 32
        self.low = int((data["main"]["temp_min"] * 1.8)) + 32
        self.conditions = data["weather"][0]["description"]


def get_weather():
    url = "https://fcc-weather-api.glitch.me/api/current?lat=38.2527&lon=-85.7585"
    response = requests.get(url)
    if "Error" not in response.text:
        return WeatherInfo(response.json())
    else:
        raise Error("Error getting weather")


def writer(data):
    with open("weather.txt", "a", encoding="UTF8") as f:
        f.write(str(date.today()) + "," +
                str(data.current_temp) + "," +
                str(data.high) + "," +
                str(data.low) + "," +
                data.conditions + "\n")
        return "done"

try:
    weather = get_weather()
    print("\nCurrent Temp:", weather.current_temp)
    print("Today's High:", weather.high)
    print("Today's Low:", weather.low)
    print("Conditions:", weather.conditions)
    writer(weather)
except Error as e:
    print(e.message)
