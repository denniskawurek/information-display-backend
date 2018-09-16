import requests
import config
import json
from RequestHandler import *

flask_api_handler = RequestHandler()

base_url = "https://www.rmv.de/hapi/departureBoard?format=json&accessId=" + config.TRANSPORT_API_KEY

# Wolfstr -> Kl. Linden
departureBus1 = base_url + "&id=3014523&direction=3014605"
# Nahrungsberg -> Bhf
departureBus2 = base_url + "&id=3019155&direction=3011016"
# Bhf Licher Str
departureTrain1 = base_url + "&id=3011178"

api_urls = [departureBus1, departureBus2, departureTrain1]
types = ["bus1", "bus2", "train1"]

def getDepartureBoardAndUpdate():
    data = {}
    index = 0
    for url in api_urls:
        result = requests.get(url)
        if result.status_code is not 200:
            return
        jsonObj = result.json()
        data[index] = jsonObj
        index += 1
        
    updateDatabase(json.dumps(data))

def updateDatabase(jsonData):
    if config.INIT is True:
        flask_api_handler.post("departures", jsonData)
    else:
        flask_api_handler.put("departures", jsonData)

if __name__ == '__main__':
    getDepartureBoardAndUpdate()
