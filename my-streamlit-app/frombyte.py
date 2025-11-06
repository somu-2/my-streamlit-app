import numpy as np
import rprak as rpk
#import rle
from numpy import savetxt
from numpy import genfromtxt
import csv
import korboi as ko
import matplotlib.pyplot as plt
import byteform as bfm
#import fbm
from tkinter import filedialog
import pandas as pd
import sys
import time
import tkinter as tk
from tqwt import tqwt
#from itqwt import itqwt
from numpy import random
import math







#ss2=genfromtxt('ss2.csv', delimiter=',')
#bb=genfromtxt('dc1.csv', delimiter=',')



tsv=[4,4,6,6,8,8]
#w = tqwt(strtk, Q,R,S)
g1=len(ss2)
g2=g1
op=[]
kth=0
jh=0
for d in range(0,1000):
    
    if (g1-kth)>10:
        
        g1=g1-kth
        print('ggggg', d, kth)
        jh=jh+kth
        s2=ss2[int(jh):g2]
        (k11,Q1,R1,S1,v1,mb1,a11,kth,bx,tr3,lth)=bfm.revheaderbyte(s2,tsv)
        print('kth', kth)
        lth=lth-2
        tr4=tr3
        fr=[]
        for i in range(0,6):
            dy2=ko.tke(a11,i,0)
            dy1=ko.paap(dy2,Q1,R1,S1,k11)
            if i==0:
                fr=dy1
            else:
                fr=ko.adi(fr,dy1,0,0)
        mn1=ko.tke(fr,5,0)
        fr= fr[0:5]
        (fn4)=ko.antipca(v1,fr,mn1)
        if bx==1:
            fn4=np.transpose(fn4)
            fv=fn4[0:(int(k11)-1)]
            fv=np.transpose(fv)
        else:
            fv=fn4
        tg=ko.fnl(fv,0)
        tg=np.transpose(tg)
        #print(d)
        if d==0:
            op=tg
        else:
            op=np.concatenate((op,tg))
    else:
        break
    
   






op=np.transpose(op)
bbg=op
plt.figure(1)
plt.subplot(211)
for i in range(0,12):
    plt.plot(bbg[i])
    
bb=np.transpose(bb)
v2=ko.fnl(bb,0)

bbg=v2
plt.figure(1)
plt.subplot(212)
for i in range(0,12):
    plt.plot(bbg[i])



#tg=np.transpose(tg)
#v2=np.transpose(v2)
bg=ko.err(op,v2,1)
[m1,m2]=op.shape

f1=(m2*12*16)/g2
f1=np.round(f1,2)
print(' CR is', f1, 'PRD= ', bg[12,0], 'PRDN= ', bg[12,1])
plt.show()


    

    







        
