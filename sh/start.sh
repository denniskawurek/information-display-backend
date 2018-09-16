#!/bin/bash

cd ~/code/information-display/information-display-backend/sh
./startFlask.sh
./startApp.sh
./maximizeChrome.sh
cd ~/code/information-display/information-display-backend/sensors
./listen_touch &
