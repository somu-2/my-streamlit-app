import numpy as np
import matplotlib.pyplot as plt
from numpy import savetxt

from numpy import savetxt
from numpy import genfromtxt
import csv

from tkinter import filedialog
import pandas as pd
import sys
import time
import tkinter as tk

from tqwt import tqwt
from itqwt import itqwt
import korboi as ko

q = 9.9; redundancy = 3; stages = 11     # parameters
               # signal length
##x = np.random.randn(n)    # test signal (white noise)
ar=genfromtxt('100.csv', delimiter=',')
x=np.array(ar)
x=x[0:700]
n=len(x)
w = tqwt(x, q, redundancy, stages)       # wavelet transform
s1=[];

for i in range(0,(stages+1)):
    w1=w[(i):(i+1)]
    w2=w1[0]
    w2=np.array(w2)
    w3=w2.real
    print(len(w2))
    if i!=stages:
        w3=w3*0
    s1.append(w3)


    plt.figure((1))
    plt.subplot(3,4,(i+1))
    plt.plot(w3)



#plt.figure((1))
##plt.subplot(3,4,(1))s1
    
#plt.plot(x)




y=itqwt(s1,q,redundancy, n)

plt.figure((2))
plt.subplot(211)
plt.plot(x)
plt.subplot(212)
plt.plot(y)

er=ko.ercom(x,y)
print(er)



plt.show()












    
