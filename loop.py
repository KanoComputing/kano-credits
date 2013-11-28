
import time
import controls
import graphics
import OOP_graphics
import OOP_text

frame_len = .3
last_update = None

maxSize = 22
move_y = 0


def init():

    graphics.init()
    graphics.drawBackground()

    OOP_text.init()

    
def update():
    global move_y

    if len(OOP_text.currentText[0].text) > 0:
        OOP_text.currentText[0].text.pop(0)

    # Go through array of visible ascii art
    # For each object, move the top line of the art to the bottom

    for i in range(len(OOP_graphics.visibleAsciiArt)):
        for x in range(OOP_graphics.visibleAsciiArt[i].numberOfLines):
            OOP_graphics.visibleAsciiArt[i].art.append(OOP_graphics.visibleAsciiArt[i].art[0])
            OOP_graphics.visibleAsciiArt[i].art.pop(0)
        
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
