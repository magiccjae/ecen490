import sys
import json
import math
import time

import shlex, subprocess

from motion_control import *
from functions import *

kick_constant = 25

goalDirection = 0
kicker = 1
kick_counter = 0


def mainFunc():
    initializePID()
    global kick_counter
    kick_counter = kick_constant

    if len(sys.argv) == 3:
        if(sys.argv[1] == 'h'):
            global goalDirection
            goalDirection = 1
        if(sys.argv[1] == 'a'):
            global goalDirection
            goalDirection = -1
        if(sys.argv[2] == 's'):
            straightAttack()
    if len(sys.argv) == 2:
        if(sys.argv[1] == 'h'):
            global goalDirection
            goalDirection = 1
            jsonDecoder()
        if(sys.argv[1] == 'a'):
            global goalDirection
            goalDirection = -1
            jsonDecoder()
        if(sys.argv[1] == 's'):
            straightAttack()
            jsonDecoder()
    else:
        jsonDecoder()

def initializePID():
    #current_pid = readM1pidq(128)
    #print "M1 before p,i,d,qpps: ", current_pid
    SetM1pidq(128,22000,80000,16351,180000)
    #new_pid = readM1pidq(128)
    #print "M1 after p,i,d,qpps: ", new_pid


    #current_pid = readM2pidq(128)
    #print "M2 before p,i,d,qpps: ", current_pid
    SetM2pidq(128,22000,80000,16351,180000)
    #new_pid = readM2pidq(128)
    #print "M2 after p,i,d,qpps: ", new_pid

    #print(readlogicbatterysettings())
    #print(readversion())
    #print "Error State:",repr(readerrorstate())
    #errorState = readerrorstate()
    #print errorState

    #current_pid = readM2pidq(129)
    #print "M3 before p,i,d,qpps: ", current_pid
    SetM2pidq(129,22000,80000,16351,180000)
    #new_pid = readM2pidq(129)
    #print "M3 after p,i,d,qpps: ", new_pid

def stop():
    M1Forward(128,0)
    M2Forward(128,0)
    M2Forward(129,0)
    M1Forward(128,0)
    M2Forward(128,0)
    M2Forward(129,0)
    M1Forward(128,0)
    M2Forward(128,0)
    M2Forward(129,0)
    M1Forward(128,0)
    M2Forward(128,0)
    M2Forward(129,0)
    print "STOPPED!!!!!!!!"

def start():
    initializePID()
    print "STARTED!!!!!!!"

def jsonDecoder():
    rx, ry, rw = 0, 0, 0
    oldrx, oldry, oldrw = 0, 0, 0
    oldbx, oldby = 0 , 0
    bx, by = 0 , 0
    time = 0
    dx, dy, dw = 0, 0, 0
    while 1:
        line = sys.stdin.readline()
        if not line:
            break
        j = json.loads(line)
        rx = j["players"][0]["X"]
        ry = j["players"][0]["Y"]
        rw = j["players"][0]["W"]
        bx = j["ball"]["X"]
        by = j["ball"]["Y"]

        #goToBall(rx, ry, rw, bx, by)
        #goToCenter(rx, ry, rw)

        if filter(oldrx, oldry, oldrw, oldbx, oldby, rx, ry, rw, bx, by):
            if goalDirection == 1: # Home
                xConstant = 12.0
                yConstant = 3.0
                ballAngleToGoal = math.atan2(by,(100-bx)*goalDirection)
                xPosBehindBall = float(xConstant) * float(math.cos(ballAngleToGoal))
                yPosBehindBall = yConstant*math.sin(ballAngleToGoal)

                ballX = bx

                xTemp = ballX - xPosBehindBall
                #print "------xtemp: ", xTemp, "-------"

                #print "angle: ", ballAngleToGoal, " xPos: ", xPosBehindBall, " yPos: ", yPosBehindBall
                #print "xTarget: ",bx-xPosBehindBall, "yTarget: ",by-yPosBehindBall

                if rx-bx < 8 and rx < bx and abs(ry-by) < 3:
                    print("------------attacking goal!--------------")
                    attackGoal(rx, ry, rw)
                else:
                    print("-------------going behind ball-----------")
                    if(by > 0):
                        goToBall(rx, ry, rw, bx-8, by+3)
                    else:
                        goToBall(rx, ry, rw, bx-8, by-3)

            elif goalDirection == -1: # Away
                if rx-bx < 8 and bx < rx and  abs(ry-by) < 3:
                    print("------------attacking goal!--------------")
                    attackGoal(rx, ry, rw)
                else:
                    print("-------------going behind ball-----------")
                    if(by > 0):
                        goToBall(rx, ry, rw, bx+8, by+3)
                    else:
                        goToBall(rx, ry, rw, bx+8, by-3)

        oldrx, oldry, oldrw, oldbx, oldby = rx, ry, rw, bx, by


        ##### START AND STOP COMMANDS #####

        if (bx == 666 and by == 666):
            stop()

        elif (bx == 555 and by == 555):
            start()

        ###################################

def kickBall():
    global kick_counter
    if(kick_counter == 0):
        cmd = 'echo 0 > /sys/class/gpio/gpio200/value'
        output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )
        time.sleep(.1)
        cmd = 'echo 1 > /sys/class/gpio/gpio200/value'
        output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )
        kick_counter = kick_constant
    else:
        kick_counter -= 1



def nearTarget(rx, ry, tx, ty):
    if abs(rx-tx) < 5 and abs(ry-ty) < 5:
        return true
    else:
        return false

def goToCenter(rx, ry, rw):
    time = determineTime(rx, ry, 0, 0)
    motion(rx, ry, rw, 0, 0, rw, 4)

def filter(orx, ory, orw, obx, oby, rx, ry, rw, bx, by):
    if abs(orx -rx) > 25:
        return False
    if abs(ory -ry) > 25:
        return False
    if abs(orw%360 - rw%360) > 25:
        return False
    if abs(obx -bx) > 25:
        return False
    if abs(oby -by) > 25:
        return False
    return True

def goToBall(rx, ry, rw, bx, by):
    time = determineTime(rx, ry, bx, by)
    #print(" rx: ", rx, " ry: ", ry, " rw: ", rw, " bx: ", bx, " by: ", by )

    dy = 0 - by
    dx = goalDirection*100-bx
    dw = math.degrees(math.atan2(dy,dx))

    motion(rx, ry, rw, bx, by, dw, time)

def attackGoal(rx, ry, rw):

    time = determineTime(rx, ry, 100*goalDirection, 0)
    motion(rx, ry, rw, 100*goalDirection, 0, 0, time)
    kickBall()


def determineTime(x, y, dx, dy):
    distance = math.sqrt((dx-x)**2 + (dy - y)**2)
    if(distance > 3):
        return 3;
    elif(distance > 2):
        return 2;
    else:
        return 1;

def createPoint(rx, ry, rw, dx, dy, dw, time):
    point = {}
    point["rx"] = rx
    point["ry"] = ry
    point["rw"] = rw
    point["dx"] = dx
    point["dy"] = dy
    point["dw"] = dw
    point["time"] = time
    return point

def defenseMove(cY, dY):
    move(robot.x, robot.y, robot.w, robot.x, ball.y, robot.w, time)

mainFunc()
