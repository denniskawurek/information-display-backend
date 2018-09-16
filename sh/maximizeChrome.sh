#!/bin/bash

WID=`xdotool search --desktop 0 --class "Chromium"`

while [ -z "$WID" ]; do
  WID=`xdotool search --desktop 0 --class "Chromium"`
  sleep 1s
done  

xdotool windowactivate $WID
xdotool key F11
export WID=$IWD
