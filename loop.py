
import time
import controls
import graphics

frame_len = .3
last_update = None
text = []
maxSize = 22


def init():
    global text

    graphics.init()
    graphics.drawBackground()
    with open("credits") as f:
        text = f.readlines()
    #for i in range(len(text)):
        #text[i] = text[i].rstrip()
    

def update():
    global text

    if len(text) > 0:
        text.pop(0)
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
