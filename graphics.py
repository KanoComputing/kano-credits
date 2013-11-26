
import curses
import console
import math
import loop

screen = None
#padding = (padding_y, padding_x, padding_y, padding_x)
width = 0
height = 0


def drawTile(x, y, tile='', color=None):
    global screen

    #x = x * 2 + stage.padding[3] * 2 + stage.width / 2
    #y += stage.padding[0] + stage.height / 2

    screen.addstr(y, x, tile, color)
    if (len(tile) < 2):
        screen.addstr(y, x + 1, tile, color)


def drawBackground():
    #global width, height

    print width
    print height
    #max_y = int(math.floor(height) / 2)
    max_x = int(math.floor(width) / 2)
    color = curses.color_pair(2)

    # Top to bottom
    for y in range(0, height):
        # Left to Right
        for x in range(0, max_x):
            drawTile(x, y, ' ', curses.COLOR_BLUE)
    
    drawHeader()
    drawBorders()


def drawHeader():
    global height, width
    color = curses.color_pair(1)

    drawTile(10, 0, "Width: %d, Height: %d" % (width, height), color)
    #drawTile(10, 0, ' C R E D I T S', curses.COLOR_GREEN)
 

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


def drawText():
    global height, width
    color = curses.color_pair(2)

    x = 20
    y = 3
    idx = 0
    numLines = 36
    for idx in range(numLines):
        if len(loop.text)-1 <= idx:
            break
        drawTile(x, y, loop.text[idx], color)
        y = y + 1
        

def update():
    drawText()


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


def exit():
    screen.clear()
    screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
