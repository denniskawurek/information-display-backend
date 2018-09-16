import requests
import config
import json
from RequestHandler import *

flask_api_handler = RequestHandler()
api_url_current_weather = "https://api.openweathermap.org/data/2.5/weather" + "?id=" + config.WEATHER_CITY_ID + "&appid=" + config.WEATHER_API_KEY

def getCurrentWeatherAndUpdate():
    result = requests.get(api_url_current_weather)
    if result.status_code is not 200:
            return
    updateDatabase(json.dumps(result.json()))

def updateDatabase(jsonData):
    if config.INIT is True:
        flask_api_handler.post("current_weather", jsonData)
    else:
        flask_api_handler.put("current_weather", jsonData)

if __name__ == '__main__':
    getCurrentWeatherAndUpdate()
