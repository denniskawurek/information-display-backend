import Adafruit_DHT
import sys
import json
import config

sys.path.append("../api_requests/")
from RequestHandler import *

flask_api_handler = RequestHandler()
sensor = Adafruit_DHT.DHT11 # use DHT22 for 22 or AM2302 for 2302 sensor
pin = config.TEMPERATURE_SENSOR_GPIO

def readFromSensorAndUpdate():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
	humidityQuality = getHumidityQuality(humidity)
	data = {"temperature": temperature, "humidity": humidity, "humidity_quality": humidityQuality}
        jsonData = json.dumps(data)
	print(jsonData)
        updateDatabase(jsonData)
    else:
        print("Failed to read temperature. Try again!")
        sys.exit(1)

def getHumidityQuality(humidity):
    if humidity < 40:
        return "LOW"
    elif humidity >= 40 and humidity < 60:
        return "GOOD"
    else:
        return "HIGH"

def updateDatabase(jsonData):
    if config.INIT is True:
        flask_api_handler.post("temperature", jsonData)
    else:
        flask_api_handler.put("temperature", jsonData)

if __name__ == "__main__":
    readFromSensorAndUpdate()
