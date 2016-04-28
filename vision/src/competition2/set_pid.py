
from roboclaw import *                                                          
                                                                                 
print "set pid started"                                                         

SetM1pidq(128,22000,80000,16351,180000)                                         
new_pid = readM1pidq(128)                                                       
print "M1 after p,i,d,qpps: ", new_pid                                          


SetM2pidq(128,22000,80000,16351,180000)                                         
new_pid = readM2pidq(128)                                                       
print "M2 after p,i,d,qpps: ", new_pid                                          


SetM2pidq(129,22000,80000,16351,180000)                                         
new_pid = readM2pidq(129)                                                       
print "M3 after p,i,d,qpps: ", new_pid 
