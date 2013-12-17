
import graphics
import loop
import os


def exit():
    graphics.exit()


def run():
    try:
        loop.start()

    except KeyboardInterrupt:
        exit()

run()
