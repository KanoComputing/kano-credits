
# controls.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# Licence:  http://www.gnu.org/licences/gpl-2.0.txt GNU General Public License v2
#

import graphics

keys = {
    'Q': 0x71,
}


def update():
    key = graphics.screen.getch()

    if key > 0:

        if key == keys['Q']:
            exit()
