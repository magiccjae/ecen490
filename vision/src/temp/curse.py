import curses
import time

from functions import *
from roboclaw import *


screen = curses.initscr()
curses.echo()

while True:
    key = screen.getch()
    if key == 113:
        counterClockwise(60)
    elif key == 101:
        clockwise(60)
    elif key == 119:
        forward()
    elif key == 115:
        back()
    elif key == 97:
        left()
    elif key == 100:
        right()
    elif key == 112:
        stop()
    elif key == 98:
        box()
    elif key == 116:
        crazy()
        crazy()
        crazy()
        crazy()
    time.sleep(0.01)
    #perhaps add a stop out here so the robot defaults to just stopping
