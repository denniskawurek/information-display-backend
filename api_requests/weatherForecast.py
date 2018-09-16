import requests
import config
import json
from RequestHandler import *

flask_api_handler = RequestHandler()
api_url_forecast = "https://api.openweathermap.org/data/2.5/forecast" + "?id=" + config.WEATHER_CITY_ID + "&appid=" + config.WEATHER_API_KEY

def getWeatherForecastAndUpdate():
    result = requests.get(api_url_forecast)
    if result.status_code is not 200:
            return
    updateDatabase(json.dumps(result.json()))

def updateDatabase(jsonData):
    if config.INIT is True:
        flask_api_handler.post("weather_forecast", jsonData)
    else:
        flask_api_handler.put("weather_forecast", jsonData)

if __name__ == '__main__':
    getWeatherForecastAndUpdate()
