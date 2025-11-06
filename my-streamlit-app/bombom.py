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
from itqwt import itqwt
from numpy import random
import math
import pkdt



import compressfunc as comfnc
import decompressfunc as decomfnc

ts=[]
jk1=0
tsv1=genfromtxt('tsv2.csv', delimiter=',')
[m1,m2]=tsv1.shape
for i in range(0,1):
    tsv=ko.tke(tsv1,i,0)
    print(tsv)
    #tsv=[3,3,6,5,6,6]


    #tsv=[4,4,6,6,8,8]
    sf=1000
    ###########1__1__1__1__1__1__1__1__1__1__1__1__1__#######################
    #######    1st function :    peakdt(sf,pq,crt,pts)
    # sf= sampling frequency
    # pq= 0: it will automatically take 104.csv_12 lead.......  1: panda will run
    # crt= 0: NOP...   1: program will run
    # pts: 1: plot will show.....    0: no plt
    # return:   data and R-peak

    pq=1
    if i==0:
        crt=1
    else:
        crt=0
    pts=0
    (data,pk)=pkdt.peakdt(sf,pq,crt,pts)
    print('   ')
    print('   ')
    print('****----      peak detection end ----    ******')
    print('   ')
    print('   ')

    #########################1__1__1__1__1__##############################



    #############2__2__2__2__2__2__2__2__2__2__2__2__2__2__#############
    #######     dcom(tsv,crt,sf,mb,pq,momo):
    # crt= always 1
    # mb= 1,5,10,15 asyou wish
    # momo= 0: No excess compresseion
    # pq= number ofbeat compressed, if 0: system generated..    >0: pq number of beat matrix will be compressed
    mb=1
    pq=1
    momo=1
    (ss1,q1,q2,q3,q4,q5,tsv1)=comfnc.dcom(tsv,1,sf,mb,pq,momo)
    print('   ')
    print('   ')
    print('****----    Data compression done----    ******')
    print('   ')
    print('   ')


    ##########################2__2__2__2__2__############################






    #############3__3__3__3__3__3__3__3__3__3__3__3__3__3__##############
    ########   decomdata(tsv,mm)
    # mm: 1: plot will show.....    0: no plt
    mm=0
    mmx=0
    (cr,er)=decomfnc.decomdata(tsv1,mm,mmx)
    if momo>0:
        ff=er[12,1]
        ff1=er[12,0]
        q21=q2*ff/ff1
        ff=np.concatenate(([i],[q1],[q3],[q4],[cr],[q2],[q21], [ff1], [ff],[q5]))
        ff=np.round(ff,2)
        
        ff1=list(ff)
        #qall=[q1,q3,q4,cr,q2,er[12,0],er[12,1]]
        #qall=np.arrray(qall)
        #qall=round(qall,2)
        print('   ')
        print('   ')

        print(ff1)
    print('   ')
    print('   ')

    print('****----    Data re-construction done----    ******')

    if mm==1:
        plt.show()
    #########################3__3__3__3__3__#############################

    v1=cr/er[12,0]
    v1=round(v1,2)
    tsv=np.concatenate(([i],tsv,[cr],[er[12,0]],[v1]))
    jk=(tsv[7]/tsv[8])/tsv[8]
    if jk>jk1:
        jk1=jk
        gt=tsv
        
    if i==0:
        ts=tsv
    else:
        ts=ko.adi(ts,tsv,0,0)
    
savetxt('tss1.csv', ts, delimiter=',')










