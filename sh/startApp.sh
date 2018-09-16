#!/bin/bash

cd ~/code/information-display/information-display/dist
PORT=5002 serve -s . &
chromium-browser http://localhost:5002 &
sleep 30s
#WID=`xdotool search --desktop 0 --class "Chromium"`
#xdotool windowactivate $WID
#xdotool key F11

