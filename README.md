# Information Display (Backend)

This is the backend for the [Information Display](https://github.com/denniskawurek/information-display-backend).

If you want to read how to setup the whole display you should read the [article I wrote](https://dkwr.de/articles/a/information-display-raspberry-pi-zero).

## Folder structure

```
information-display-backend
│   server.py - the API (using Flask)
└───api_requests - requests to other APIs (e.g. weather, transportation, ...)
│
└───db - files for database operations
└───sensors - files reading sensor states
|   | config.py - Set GPIO Pins for sensors
│   └───sh - shell scripts for executing after getting 
│       │   rightClick.sh - simulates a right button click in chrome
└───sh
     | infoDisplay.desktop - starts the display after boot
     | crontab - Cronjobs
     | start.sh  - script to start the FLASK API and VueJS app
```

# Setup

This describes the setup for a Raspberry PI (Zero W) running **Raspbian**. Open a terminal and type in the following commands.

1. Install mongoDB:
 `sudo apt-get install mongodb`

2. Install NodeJS (and Node dependencies)
Get the current version from the official NodeJS page: https://nodejs.org/dist

*Hint:* Get System information by `cat /proc/cpuinfo`

```
wget https://nodejs.org/dist/v10.9.0/node-v10.9.0-linux-armv6l.tar.gz
tar xvf node-v10.9.0-linux-armv6l.tar.gz
sudo cp -R * /usr/local/

node -v
npm -v

sudo npm install npm@latest -g
sudo npm install serve --save -g
```

3. Create the folder for the information display

```
cd ~
mkdir code/information-display
cd code/information-display
```
4. Clone this project
```
git clone https://github.com/denniskawurek/information-display-backend
```
5. Clone the app
```
git clone https://github.com/denniskawurek/information-display
```
6. Install the AdaFruit library
Will be used for the temperature sensor.

```
cd ~/code/information-display
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
```

7. Install `xdotool` (for keyboard simulation)

`sudo apt-get install xdotool`

8. Configure the API keys

In the `api_requests` folder is a file called `config.py`.
There are the API keys etc. which you need to set.

The weather module is using [openweathermap.org](https://openweathermap.org/)

9. Set the `INIT` variable
In `api_requests/config.py` and `sensors/config.py` you need to set the `INIT` variable to `True` for the first run.
**Afterwards** you need to **change it back** to `False`.

10. Install python dependencies

Install the python dependencies with the command below:

```
pip install -r requirements.txt
```

## Serve the App

Change to the dist/ directory of the application
Type in the following command:
`PORT=5001 serve -s .`

## Serve the API

You can run the app either by
`FLASK_APP=server.py flask run` or `python server.py`


# Pins
See [pinout.xyz](https://de.pinout.xyz/#)
By default the project is using the following Pins for its sensors.

| Sensor               | BCM | Physical | Wiring Pi |
|----------------------|-----|----------|-----------|
| DHT11 (Temperature)  | 2   | 3        | 8         |
| Touch Sensor         | 10  | 19       | 12        |
| Light Sensor         | 17  | 11       | 0         |
| PIR Sensor           | 24  | 18       | 5         |
