
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
