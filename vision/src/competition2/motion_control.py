#!/usr/bin/python
import numpy as np
import math
import sys
import json
from datetime import datetime
from roboclaw import *

vx = 0
vy = 0
w = 0
theta = 0
wheel_radius = 3.0
M = (1.0/wheel_radius)*np.matrix([[-0.5,0.866,(0.866*6.9282+0.5*4)],[-0.5,-0.866,(0.866*6.9282+.5*4)],[1,0,8]])
R = np.matrix([[],[],[]])
magic_number = 2**12
back_number = 2**11.8

def rotation_matrix(theta):
    theta = theta*math.pi/180
    R = np.matrix([[math.cos(theta),math.sin(theta),0],[-math.sin(theta),math.cos(theta),0],[0,0,1]])
    return R

def point_to_velocity(cx,cy,c_theta,dx,dy,d_theta,time):

    deltax = dx - cx
    deltay = dy - cy
    rads = math.atan2(deltay,deltax)
    #rads %= 2*math.pi
    #direction = math.degrees(rads)
    mult = 65

    vx = mult*math.cos(rads)
    vy = mult*math.sin(rads)

    #deltax = (dx-cx)
    #deltay = (dy-cy)
    #mult = 20

    #ratio = float(deltay)/float(deltax)
    #vx = mult
    #vy = ratio*mult


     #if(vx < 5 and vy < 5):
     #   vx = vx * 5
     #   vy = vy * 5

    #print("vx: ", vx, "vy: ", vy)

    # Set maximum speed to 100 speed units
   # max_speed = 100
   # if (vx > vy):
   #     if vx > math.abs(max_speed):
   #         vy = mult * max_speed / float(vx)
   #         vx = max_speed
   # else:
   #     if vy > math.abs(max_speed):
   #         vx = mult * max_speed / float(vy)
   #         vy = max_speed

    spin = 90.0 # higher is slower
    theta = (d_theta-c_theta)

    if theta >= -360 and theta < -180:
        w = -theta / spin
    elif theta >= -180 and theta < 0:
        w = theta / spin
    elif theta >= 0 and theta < 180:
        w = theta / spin
    else:
        w = - theta / spin

    # Set minimum speed
    if w >= .3 and w < 1:
        w = 1
    elif w <= -.3 and w > -1:
        w = -1

    return vx,vy,w

def motion(cx, cy, c_theta, dx, dy, d_theta, time):
   
    # Uncomment later
    #d_theta = 0
    if d_theta == 0:
        d_theta = 360

    temp = point_to_velocity(cx,cy,c_theta,dx,dy,d_theta,time)
    
    print "Desired theta: " , d_theta

    vx = temp[0]
    vy = temp[1]
    #w = temp[2]

    #vx = 0
    #vy = 0
    w = 0

    print "before rotation: vx: ", vx, "vy: ", vy, "w: ", w
    print "time: ", str(datetime.now())
    V = np.matrix([[vx],[vy],[w]])


    #R = rotation_matrix(c_theta + 270)
    R = rotation_matrix(c_theta + 270)
    final = M*R*V

    #print "a1: ", final[0], "a2: ", final[1], "a3: ", final[2]

    omega1 = int(final[0]*magic_number)
    omega2 = int(final[1]*magic_number)
    omega3 = int(final[2]*back_number)
    #print [omega1, omega2, omega3]
    SetM1Speed(128,-1*omega1)
    SetM2Speed(128,-1*omega2)
    SetM2Speed(129,-1*omega3)

#def mainFunc():
#    print(point_to_velocity(-75, -16, 117, 25, -2, 117, 4))
#
#mainFunc()
