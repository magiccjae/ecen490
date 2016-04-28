#!/usr/bin/python
from roboclaw import *

def right():
    M1Backward(35, 128)
    M2Backward(35, 128)
    M1Forward(70, 129)

def left():
    M1Forward(35, 128)
    M2Forward(35, 128)
    M1Backward(70, 129)

def forward():
    M1Forward(70, 128)
    M2Backward(70, 128)
    M1Forward(2, 129)

def back():
    M1Backward(70, 128)
    M2Forward(70, 128)
    M1Forward(0, 129)

def stop():
    M1Forward(0, 128)
    M2Forward(0, 128)
    M1Forward(0, 129)

def counterClockwise(speed):
    M1Forward(speed, 128)
    M2Forward(speed, 128)
    M1Forward(speed, 129)

def clockwise(speed):
    M1Backward(speed, 128)
    M2Backward(speed, 128)
    M1Backward(speed, 129)

def box():
    forward()
    time.sleep(.8)
    stop()
    time.sleep(.5)
    right()
    time.sleep(1.1)
    stop()
    time.sleep(.5)
    back()
    time.sleep(.7)
    stop()
    time.sleep(.5)
    left()
    time.sleep(1.3)
    stop()
    time.sleep(.5)
    stop()

def crazy():
    M1Forward(120, 128)
    M2Backward(120, 128)
    M1Forward(2, 129)
    time.sleep(.3)
    M1Backward(60, 128)
    M2Backward(60, 128)
    M1Forward(120, 129)
    time.sleep(.3)
    M1Backward(120, 128)
    M2Forward(120, 128)
    M1Forward(0, 129)
    time.sleep(.3)
    M1Forward(60, 128)
    M2Forward(60, 128)
    M1Backward(120, 129)
    time.sleep(.3)
    stop()



while(True):
    direction = raw_input("w, s, d, a, q, b for box, t for crazy:  ")
    if direction == 'w':
        forward()
    if direction == 's':
        back()
    if direction == 'a':
        left()
    if direction == 'd':
        right()
    if direction == 'q':
        stop()
    if direction == "z":
        counterClockwise(20)
    if direction == "v":
        clockwise(20)
    if direction == "b":
        box()
    if direction == "t":
        crazy()
        crazy()
        crazy()
        crazy()
