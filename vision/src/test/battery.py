#!/usr/bin/python
import numpy as np
import math
from random import randint
from roboclaw import *

speed = 16384
print "started"

print readlogicbatterysettings(128)
print readlogicbatterysettings(129)

setLogicbattery(128,40,200)
setLogicbattery(129,40,200)
time.sleep(1)

print readlogicbatterysettings(128)
print readlogicbatterysettings(129)

while True:
    
    print "loop begin"
    SetM1Speed(128,speed)
    SetM2Speed(129,speed)
    SetM2Speed(128,speed)
    time.sleep(1)
    
   # print readM1instspeed(128)
   # print readM2instspeed(128)
   # print readM2instspeed(129)

    print "roboclaw 1 battery: %d" % readlogicbattery(128)
    print "roboclaw 2 battery: %d" % readlogicbattery(129)

    time.sleep(1)
