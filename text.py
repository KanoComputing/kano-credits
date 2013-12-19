
# text.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# Licence:  http://www.gnu.org/licences/gpl-2.0.txt GNU General Public License v2
#

import curses
import console
import graphics


currentText = []
allText = []
height = 0
width = 0


# This class creates an object of all the names in a file.
class Text(object):

    # name is a string containing the name of the file
    def __init__(self, name):
        global height, width

        (width, height) = console.getTerminalSize()

        self.name = name
        self.startingHeight = height - 1

        with open(self.name) as f:
            self.text = f.readlines()
        for i in range(len(self.text)):
            self.text[i] = self.text[i].rstrip('\n')

    def drawText(self):
        global height, width

        color = curses.color_pair(8)

        x = (2 * width) / 4
        # y = self.startingHeight # Where the box is placed vertically
        y = 0
        idx = 0
        numLines = height
        for idx in range(numLines):
            if len(self.text) - 1 <= idx:
                break

            #if idx > height - y:
            #   continue

            if y < height:
                graphics.drawTile(x, y, self.text[idx], color)
                y = y + 1


def init():
    global currentText
    global allText
    global height

    # To add more text to the credits, create an object
    # from the name of the file and list it in the allText array.

    staff = Text("actualText")
    currentText = [staff]


def changeVisibleText():
    global allText
    global currentText

    if len(allText) != 0:
        currentText.append(allText[0])
        currentText.pop(0)
        allText.append(allText[0])
        allText.pop(0)