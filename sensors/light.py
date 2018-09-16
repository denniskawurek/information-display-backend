import RPi.GPIO as GPIO
import sys
import time
import json
import config

sys.path.append("../api_requests/")
from RequestHandler import *

flask_api_handler = RequestHandler()

def readFromSensorAndUpdate():
    GPIO.setmode(GPIO.BOARD)
    pin_to_circuit = config.LIGHT_SENSOR_GPIO
  
    # Output on the pin
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
    light_on = GPIO.input(pin_to_circuit) == GPIO.LOW
    data = {"light_on": light_on}
    jsonData = json.dumps(data)
    updateDatabase(jsonData)

'''
def readFromSensorAndUpdate():
    GPIO.setmode(GPIO.BOARD)
    pin_to_circuit = config.LIGHT_SENSOR_GPIO
  
    # Output on the pin
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)

    lastStatus = None

    while(True):
        GPIO.setup(pin_to_circuit, GPIO.IN)
        light_on = GPIO.input(pin_to_circuit) == GPIO.LOW
        if lastStatus is None or lastStatus is not light_on:
            data = {"light_on": light_on}
            jsonData = json.dumps(data)
            updateDatabase(jsonData)
            lastStatus = light_on

        time.sleep(1)
'''
def updateDatabase(jsonData):
    print("Writing to database...")
    if config.INIT is True:
        flask_api_handler.post("light", jsonData)
    else:
        flask_api_handler.put("light", jsonData)

if __name__ == "__main__":
    try:
        readFromSensorAndUpdate()
    finally:
        GPIO.cleanup()
