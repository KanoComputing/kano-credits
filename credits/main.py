
# main.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# Licence:  http://www.gnu.org/licences/gpl-2.0.txt GNU General Public License v2
#

import graphics
import loop


def exit():
    graphics.exit()


def run():
    try:
        loop.start()

    except KeyboardInterrupt:
        exit()

run()
