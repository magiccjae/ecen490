#!/usr/bin/python
import numpy as np
import math
from roboclaw import *

speed = 16384
print "started"

while True:
    print "loop begin"
    SetM1Speed(128,speed)
    SetM2Speed(129,speed)
    SetM2Speed(128,speed)
    time.sleep(1)
    
   # print readM1instspeed(128)
   # print readM2instspeed(128)
   # print readM2instspeed(129)
    time.sleep(1)
