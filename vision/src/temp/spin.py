#!/usr/bin/python
from roboclaw import *


def counterClockwise(speed):
    M1Forward(speed, 128)
    M2Forward(speed, 128)
    M1Forward(speed, 129)

def clockwise(speed):
    M1Backward(speed, 128)
    M2Backward(speed, 128)
    M1Backward(speed, 129)

def stop():
    M1Forward(0, 128)
    M2Forward(0, 128)
    M1Forward(0, 129)

speed = 0
while(True):
    direction = raw_input("r, l, p, s:  ")
    if direction == 'r':
        clockwise(speed)
    if direction == 'l':
        counterClockwise(speed)
    if direction == 's':
        speed = int(raw_input("speed: "))
    if direction == 'p':
        stop()
