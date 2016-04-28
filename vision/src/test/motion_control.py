#!/usr/bin/python
import numpy as np
import math
from roboclaw import *

vx = 0
vy = 0
w = 0
theta = 0
wheel_radius = 3.0
M = 1.0/wheel_radius*np.matrix([[-0.5,0.866,(0.866*6.9282+0.5*4)],[-0.5,-0.866,(0.866*6.9282+.5*4)],[1,0,8]])
R = np.matrix([[],[],[]])
magic_number = 2**13
back_number = 2**12.8
def rotation_matrix(theta):
    R = np.matrix([[math.cos(theta),math.sin(theta),0],[-math.sin(theta),math.cos(theta),0],[0,0,1]])
    return R

while True:
    #receive vx,vy,w through JSON
    vx = 0
    vy = 10
    w = 1
    theta = 0*math.pi/180
    R = rotation_matrix(theta)
    V = [[vx],[vy],[w]]
    final = M*R*V
    omega1 = int(final[0]*magic_number)
    omega2 = int(final[1]*magic_number)
    omega3 = int(final[2]*back_number)
    print omega1, omega2, omega3
    
    SetM1Speed(128,-1*omega1)
    SetM2Speed(128,-1*omega2)
    SetM2Speed(129,-1*omega3)

