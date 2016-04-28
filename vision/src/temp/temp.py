import curses
import time

from functions import *
from roboclaw import *

while True:
    print("here")
    forward()
    time.sleep(1)
    stop()
    time.sleep(1)
    print("second")
    back()
    time.sleep(1)
    #perhaps add a stop out here so the robot defaults to just stopping
