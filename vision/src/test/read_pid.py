#!/usr/bin/python
from roboclaw import *

print "test started"

m1_pid = readM1pidq(128)
print "M1 p,i,d,qpps: ", m1_pid
m2_pid = readM2pidq(128)
print "M2 p,i,d,qpps: ", m2_pid
m3_pid = readM1pidq(129)
print "M3 p,i,d,qpps: ", m3_pid
