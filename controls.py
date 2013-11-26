
import graphics

keys = {
    'Q': 0x71,
}


def update():
    key = graphics.screen.getch()

    if key > 0:

        if key == keys['Q']:
            exit()
