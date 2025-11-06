import numpy as np
import fun3
import pandas
import korboi as ko
from numpy import savetxt
from numpy import genfromtxt
import csv
import matplotlib.pyplot as plt


fle=genfromtxt('104s0306lre.csv', delimiter=',')
#fle=genfromtxt('105s0303lre.csv', delimiter=',')
pqq=2
(data,pk,er,cr,ss,recon, orgi,aw,ar4,tv)=fun3.monn(fle,pqq)

bbg=recon
plt.figure(1)
plt.subplot(212)
for i in range(0,12):
    plt.plot(bbg[i])

        

bbg=orgi
plt.figure(1)
plt.subplot(211)
for i in range(0,12):
    plt.plot(bbg[i])
#plt.show()
