#!/bin/bash

#old: xdotool search --desktop 0 "Chromium" windowactivate

if [[ -z "$WID" ]]; then
   WID=`xdotool search --desktop 0 --class "Chromium"`
fi

xdotool windowactivate $WID
xdotool key Right
export WID=$WID
