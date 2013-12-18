
import curses
import console
import math
import loop
import ascii
import text
import sys

screen = None
#padding = (padding_y, padding_x, padding_y, padding_x)
width = 0
height = 0


def drawTile(x, y, tile='', color=None):
    global screen

    #x = x * 2 + stage.padding[3] * 2 + stage.width / 2
    #y += stage.padding[0] + stage.height / 2
    try :
        screen.addstr(y, x, tile, color)
        if (len(tile) < 2):
            screen.addstr(y, x + 1, tile, color)

    except:
        # suppress output
        print ''


def drawBackground():
    #global width, height

    print width
    print height
    # max_y = int(math.floor(height) / 2)
    max_x = int(math.floor(width) / 2)
    color = curses.color_pair(2)

    # Top to bottom
    for y in range(0, height):
        # Left to Right
        for x in range(0, max_x):
            drawTile(x, y, ' ', curses.COLOR_BLUE)
    
    #drawHeader()
    #drawBorders()


def drawHeader():

    global height, width
    color = curses.color_pair(1)

    drawTile(10, 0, "Width: %d, Height: %d" % (width, height), color)
    #drawTile(10, 0, 'c r e d i t s', curses.COLOR_GREEN)
 

def drawBorders():

    color = curses.color_pair(1)
    x_left = 2
    x_right = 100 #int(math.floor(width) / 2)
    y_top = 2
    y_bottom = 40 #int(math.floor(height) / 2) + 10

    for y in range(y_top, y_bottom):
        drawTile(x_left - 1, y, '  ', color)
        drawTile(x_right, y, '  ', color)

    for x in range(x_left, x_right):
        drawTile(x, y_top - 1, '  ', color)
        drawTile(x, y_bottom, '  ', color)

    drawTile(x_left - 1, y_top - 1, '  ', color)
    drawTile(x_left - 1, y_bottom, '  ', color)
    drawTile(x_right, y_top - 1, '  ', color)
    drawTile(x_right, y_bottom, '  ', color)
        

def update():

    changeText()
    text.currentText[0].drawText()

    popOffTop()

    # Go through visibleAsciiArt array, and draw seleted asci art on the page
    for i in range(len(ascii.visibleAsciiArt)):
        ascii.visibleAsciiArt[i].drawArt()


def popOffTop():
    if len(ascii.visibleAsciiArt) != 0:
        i = ascii.visibleAsciiArt[0].currentHeight

    # if element is off the screen and none of the above.
    if i <= -ascii.visibleAsciiArt[0].numberOfLines:
        ascii.visibleAsciiArt.pop(0)

    if len(ascii.visibleAsciiArt) == 0:
        sys.exit(0)


def changeText():

    if not text.currentText[0].text:
        text.changeVisibleText()
        #if text.currentText[0].name == "premiumDonators":
            # Add function here for removing images.  Maybe resize text box/change coordinates.


def init():
    global screen, width, height

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.start_color()
    screen.nodelay(1)
    (x, y) = console.getTerminalSize()
    width = x
    height = y

    # (font, background)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)

    ascii.init()


def exit():
    screen.clear()
    screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
