import matplotlib.pyplot as pl
import numpy as np

f = open('angular_data.txt','r')
str = f.read()
data = str.split();
desired = []
for i in range(len(data)-1):
    desired.append(data[0])
feedback = data[1:len(data)]

t = np.arange(0,len(feedback),1)

xlimit = len(feedback)-1
ylimit = int(max(data))+1000

pl.plot(t,feedback,'r')
pl.plot(t,desired,'b')
pl.title('system response')
pl.xlabel('time')
pl.ylabel('angular velocity')
pl.axis([0, xlimit, 0, ylimit])
pl.show()

