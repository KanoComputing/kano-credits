#!/usr/bin/env python

# display_backers.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
#
# View backers names with colours

import os
import sys
import pydoc
import console
import random

if __name__ == '__main__' and __package__ is None:
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if dir_path != '/usr':
        sys.path.insert(0, dir_path)

from kano.colours import colourize256

LIST_FILENAME = "/tmp/real-backers-list"


def show_backer_names():
    turn_into_list()

    f = open(LIST_FILENAME)
    output = f.read()
    if len(output) > 0:
        pydoc.pipepager(output, cmd='less -R')


def turn_into_list():
    (width, height) = console.getTerminalSize()
    line_so_far = ""
    h = open("text/backers", 'r')
    text = h.readlines()
    w = open(LIST_FILENAME, 'w+')

    counter = 0
    output = ""

    # This is a bit complicated as we're add
    for i in range(len(text)):
        current_line = text[i]
        prev_line = ""
        if i > 0:
            prev_line = text[i - 1]
        if len(line_so_far + current_line) > width:
            whitespace = width - len(line_so_far)
            prev_line = prev_line.replace('\n', ','.ljust(whitespace) + '\n')
            line_so_far = current_line.replace('\n', ', ')

        else:
            prev_line = prev_line.replace('\n', ', ')
            line_so_far += current_line.replace('\n', ', ')

        number = random.randint(16, 254)
        # Colour background black
        colouredline = colourize256(prev_line, number, 0, True)
        output += colouredline
        counter = (counter + 1) % 15
        w.write(colouredline)

    w.close()

show_backer_names()
