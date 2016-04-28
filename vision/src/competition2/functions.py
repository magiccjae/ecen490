from roboclaw import *

def counterClockwise(speed):
    M1Forward(128, speed) 
    M2Forward(128, speed) 
    M2Forward(129, speed) 

def clockwise(speed):
    M1Backward(128, speed)
    M2Backward(128, speed)
    M2Backward(129, speed)

def right():
    M1Backward(128, 60)
    M2Backward(128, 60)
    M2Forward(129, 120)

def left():
    M1Forward(128, 60)
    M2Forward(128, 60)
    M2Backward(129, 120)

def forward():
    M1Forward(128, 127)
    M2Backward(128, 127)
    M2Forward(129, 2)

def back():
    M1Backward(128, 127)
    M2Forward(128, 127)
    M2Forward(129, 0)

def stop():
    M1Forward(128, 0)
    M2Forward(128, 0)
    M2Forward(129, 0)

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
