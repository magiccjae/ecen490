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

def box():
    forward()
    time.sleep(1)
    stop()
    time.sleep(.3)
    right()
    time.sleep(1.5)
    stop()
    time.sleep(.3)
    back()
    time.sleep(.8)
    stop()
    time.sleep(.3)
    left()
    time.sleep(1.5)
    stop()
    time.sleep(.3)
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
    direction = raw_input("f, b, l, r, s:  ")
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
    if direction == "b":
        box()
    if direction == "t":
        crazy()
        crazy()
        crazy()
        crazy()
