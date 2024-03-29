
# ascii.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# Licence:  http://www.gnu.org/licences/gpl-2.0.txt GNU General Public License v2
#

import curses
import console
import graphics

visibleAsciiArt = []
staffAsciiArt = []
premiumAsciiArt = []
allAsciiArt = []
height = 0
width = 0
printMessageToScreen = ''


class AsciiArt(object):

    # art will store the asciiArt
    # name will store the name of the file
    # numberOfLines will store how long each piece of ascii art is
    # startingHeight gives us how high on the screen the image is drawn.
    # When this value is < 2 - numberOfLines, it gets removed from the visibleAsciiArt array

    def __init__(self, name, numberOfLines, color):
        global height
        global width

        (width, height) = console.getTerminalSize()

        self.name = name
        self.numberOfLines = numberOfLines
        self.startingHeight = height
        self.currentHeight = height
        self.color = color

        with open(self.name) as f:
            self.art = f.readlines()
        for j in range(len(self.art)):
            self.art[j] = self.art[j].rstrip('\n')

    # This function draws the ascii art on the terminal and displays it
    #
    #
    def drawArt(self):
        global width

        x = width / 20
        y = self.currentHeight
        tempy = self.currentHeight
        idx = 0
        idx2 = self.numberOfLines

        # if element is a set distance above starting point, and staffAsciiArt is not empty
        if (y == (self.startingHeight - self.numberOfLines)) and staffAsciiArt:
            makeStaffElementVisible()
        # if element from premiumAsciiArt is a set distance from where it started and is in the premiumA
        elif (y == (self.startingHeight - self.numberOfLines)) and self in premiumAsciiArt:
            switchToPremiumImages()

        # if image would otherwise be drawn outside (above) the terminal
        if y <= 0:
            tempy = 0
            idx = -y

        # if image would otherwise be drawn outside (below) the terminal
        if y >= height - self.numberOfLines - 1:
            idx2 = height - y

        for idx in range(idx, idx2):
            if y == -self.numberOfLines:
                # so the element is back at the bottom of the page at the end of this function
                self.currentHeight = self.startingHeight
                return
            graphics.drawTile(x, tempy, self.art[idx], self.color)
            tempy = tempy + 1

        self.currentHeight = self.currentHeight - 1


def init():
    global visibleAsciiArt
    global premiumAsciiArt
    global staffAsciiArt
    global allAsciiArt

    backers = AsciiArt("headings/backers", 9, curses.color_pair(8))
    specialThanks = AsciiArt("headings/specialThanks", 12, curses.color_pair(8))
    #translators = AsciiArt("headings/translators", 9, curses.color_pair(8))
    kano = AsciiArt("headings/kano", 21, curses.color_pair(8))

    brainy = AsciiArt("staff-images/brainy-guy", 21, curses.color_pair(5))
    hand = AsciiArt("staff-images/hand", 15, curses.color_pair(2))
    book = AsciiArt("staff-images/book", 18, curses.color_pair(3))
    monkey = AsciiArt("staff-images/monkey", 24, curses.color_pair(4))
    hair = AsciiArt("staff-images/hair", 18, curses.color_pair(6))
    pikachu = AsciiArt("staff-images/pikachu", 22, curses.color_pair(6))
    bowl = AsciiArt("staff-images/bowl", 18, curses.color_pair(7))
    camera = AsciiArt("staff-images/camera", 18, curses.color_pair(8))
    wizard = AsciiArt("staff-images/wizard", 18, curses.color_pair(2))
    shoes = AsciiArt("staff-images/shoes", 18, curses.color_pair(8))
    coffee = AsciiArt("staff-images/coffee", 18, curses.color_pair(5))
    boom = AsciiArt("staff-images/boom", 15, curses.color_pair(4))
    smileyFace = AsciiArt("staff-images/smiley-face", 15, curses.color_pair(6))
    peter = AsciiArt("staff-images/peter-pan", 26, curses.color_pair(2))
    aeroplane = AsciiArt("staff-images/aeroplane", 18, curses.color_pair(3))
    judoka = AsciiArt("staff-images/judoka", 25, curses.color_pair(7))

    #imageBlank1 = AsciiArt("headings/blank", 16, curses.color_pair(8))
    #imageBlank2 = AsciiArt("headings/blank", 16, curses.color_pair(8))
    imageBlank3 = AsciiArt("headings/blank", 16, curses.color_pair(8))
    #blank = AsciiArt("staff-images/blank", 1, curses.color_pair(6))

    staffAsciiArt = [brainy, hand, hair, coffee, boom, smileyFace, book, peter, monkey, pikachu,
                     bowl, camera, wizard, shoes, aeroplane, judoka, specialThanks, imageBlank3,
                     backers]
    visibleAsciiArt = [kano]
    allAsciiArt = visibleAsciiArt + staffAsciiArt

    visibleAsciiArt[0].currentHeight = visibleAsciiArt[0].currentHeight - visibleAsciiArt[0].numberOfLines


def makeStaffElementVisible():
    global visibleAsciiArt
    global staffAsciiArt

    visibleAsciiArt.append(staffAsciiArt[0])
    staffAsciiArt.pop(0)


def switchToPremiumImages():  # TODO: need to turn this off if filled with icons already
    global visibleAsciiArt
    global premiumAsciiArt
    global printMessageToScreen

    if len(premiumAsciiArt) != 0:
        premiumAsciiArt[0].currentHeight = premiumAsciiArt[0].startingHeight
        visibleAsciiArt.append(premiumAsciiArt[0])
        premiumAsciiArt.append(premiumAsciiArt[0])
        premiumAsciiArt.pop(0)


# Sticks the object at the top of the array onto the bottom
def moveObjectToBottom():
    global visibleAsciiArt
    visibleAsciiArt[0].currentHeight = visibleAsciiArt[0].startingHeight
    visibleAsciiArt.append(visibleAsciiArt[0])
    visibleAsciiArt.remove(visibleAsciiArt[0])


def removeTopElement():
    global visibleAsciiArt
    visibleAsciiArt.pop(0)


def update():
    # Go through array of visible ascii art
    # For each object, move the top line of the art to the bottom

    for i in range(len(visibleAsciiArt)):
        for x in range(visibleAsciiArt[i].numberOfLines):
            visibleAsciiArt[i].art.append(visibleAsciiArt[i].art[0])
            visibleAsciiArt[i].art.pop(0)
