#!/usr/bin/python
import numpy as np
import math
from roboclaw import *

print "loop begin"
while True:

    print "Error State:", repr(readerrorstate())
