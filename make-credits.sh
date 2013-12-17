#!/bin/bash

# make-credits
#
# Copyright (C) 2013 Kano Computing Ltd.
# Licence:  http://www.gnu.org/licences/gpl-2.0.txt GNU General Public License v2
#

wid=$(xdotool getactivewindow)
kano-window-tool -i $wid -m -dno
python build.py
killall python
python main.py
xdotool windowkill $wid 