from roboclaw import *

def counterClockwise(speed):
    M1Forward(speed, 128)
    M2Forward(speed, 128)
    M1Forward(speed, 129)

def clockwise(speed):
    M1Backward(speed, 128)
    M2Backward(speed, 128)
    M1Backward(speed, 129)

def right():
    M1Backward(35, 128)
    M2Backward(35, 128)
    M1Forward(70, 129)

def left():
    M1Forward(35, 128)
    M2Forward(35, 128)
    M1Backward(70, 129)

def forward():
    M1Forward(127, 128)
    M2Backward(127, 128)
    M1Forward(2, 129)

def back():
    M1Backward(127, 128)
    M2Forward(127, 128)
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
