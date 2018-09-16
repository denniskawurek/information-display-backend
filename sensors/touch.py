import time
import RPi.GPIO as GPIO
import config
import subprocess
'''
If the sensor is touched, a script is called, which simulates a right click
'''

def listenForPress():
    GPIO.setmode(GPIO.BCM)

    padPin = config.TOUCH_SENSOR_GPIO
    GPIO.setup(padPin, GPIO.IN)

    alreadyPressed = False

    while True:
        padPressed = GPIO.input(padPin)

        if padPressed and not alreadyPressed:
            subprocess.call(["./sh/rightClick.sh"])

        alreadyPressed = padPressed
        time.sleep(0.1)

if __name__ == "__main__":
    listenForPress()