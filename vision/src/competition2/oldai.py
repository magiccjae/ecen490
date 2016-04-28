import sys                   
import json
import math
import time
from motion_control import *
from functions import *


def mainFunc():
    if len(sys.argv) == 2:
        if(sys.argv[1] == 's'):
            straightAttack()
    else:
        jsonDecoder()

def straightAttack():
    #things are wired backwards so i am doing this backwards
    back()
    time.sleep(1)
    stop()
    time.sleep(1)
    forward()
    time.sleep(1)
    stop()
    time.sleep(.5)
    jsonDecoder()

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

        goToBall(rx, ry, rw, bx, ry)

        if filter(oldrx, oldry, oldrw, oldbx, oldby, rx, ry, rw, bx, by):       
            goToBall(rx,ry,rw,bx,by)
#            if bx < 0:                                                          
#                goToBall(rx, ry, rw, bx, by)                                    
#            else:                                                               
#                if abs(rx-bx) < 5:                                              
#                    attackGoal(rx, ry, rw)                                      
#                else:                                                           
#                    goToBall(rx, ry, rw, bx, by)                                
        else:
            print("filtering")
        oldrx, oldry, oldrw, oldbx, oldby = rx, ry, rw, bx, by                  


def filter(orx, ory, orw, obx, oby, rx, ry, rw, bx, by):              
    if abs(orx -rx) > 25:                                             
        return False                                                  
    if abs(ory -ry) > 25:                                             
        return False                                                  
    if abs(orw -rw) > 25:                                             
        return False                                                  
    if abs(obx -bx) > 25:                                             
        return False                                                  
    if abs(oby -by) > 25:                                             
        return False                                                  
    return True                                                       

def goToBall(rx, ry, rw, bx, by):              
    time = determineTime(rx, ry, bx, by)       
    motion(rx, ry, rw, 0, 0, 0, time)       
    print "X coord: %d Y coord: %d" % (rx, ry)
    print "Ball x: %d Ball y: %d" % (bx, by)

def attackGoal(rx, ry, rw):                    
    time = determineTime(rx, ry, 100, 0)       
    motion(rx, ry, rw, 100, 0, 0, time)           


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
#jsonDecoder()
