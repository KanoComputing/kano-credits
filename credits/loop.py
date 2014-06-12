
# loop.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# Licence:  http://www.gnu.org/licences/gpl-2.0.txt GNU General Public License v2
#

import time
import controls
import graphics
import ascii
import text

frame_len = .3
last_update = None

maxSize = 22
move_y = 0


def init():

    graphics.init()
    graphics.drawBackground()
    text.init()


def update():
    global move_y

    text.popTopOff()
    ascii.update()
    graphics.update()


def step():
    global last_update

    cur_time = time.time()

    if last_update:
        elapsed = cur_time - last_update
    else:
        elapsed = 0

    if not elapsed or elapsed > frame_len:

        if not elapsed:
            until_next = frame_len
        else:
            until_next = elapsed - frame_len
            time.sleep(until_next)

        update()
        last_update = time.time()


def start():

    init()
    while True:
        controls.update()
        step()
