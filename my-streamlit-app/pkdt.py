import numpy as np
import rprak as rpk

from numpy import savetxt
from numpy import genfromtxt
import csv
import korboi as ko
import matplotlib.pyplot as plt


from tkinter import filedialog
import pandas as pd
import sys
import time
import tkinter as tk

from numpy import random

# sf= sampling frequency
# pq= 0: it will automatically take 104.csv_12 lead.......  1: panda will run
# crt= 0: NOP...   1: progam will run
# pts: 1: plot will show.....    0: no plt
# return:   data and R-peak


def peakdt(sf,pq,crt,pts,mf):
    tr1=[]
    ts9=[]
    z2=[]
    tsm=[]
    tsv=[]
    tr2=[]
    ff2=[]
    vv1=[]
    a1=[]
    t=[]

    if crt>0:
        pkv=[]
        tv=[]
        if pq==0:
            aa=mf
            
            ar=ko.tke(aa,7,1)
        else:
            a1=[]
            aa=ko.get(0)
            ar=ko.tke(aa,7,1)
        ar3=ar[0:(sf*3)]
        start = time.time()
        pk,cutval,cutdur,ene,slpene,up =rpk.fndpk(ar3,sf,0)
        end = time.time()
        ft1=((end-start)/(sf*3))
        print('feature time', (ft1*1000))
        ar4=ar
        start = time.time()
        t,rj,rj1,tg=rpk.rndpk(ar4,pk,sf,cutval,cutdur,ene,slpene,up)
        end = time.time()
        ft1=((end-start)/(len(ar4)))
        print('actual time', (ft1*1000))
        td=np.diff(t)
        aw=ko.pt(ar4)
        title = ["Peak detected ECG lead", "Difference between each peak"]
        
        for i in range(0,8):
            xe=[0,1,6,7,8,9,10,11]
            a=ko.tke(aa,xe[i],1)
            a1=ko.adi(a1,a,1,0)
        #savetxt('data.csv', a1, delimiter=',')
        #savetxt('pk.csv', t, delimiter=',')
        for i in range(0,len(t)):
            x=int(t[i])
            t1=ar4[x]
            tv.append(t1)
        plt.figure(100)
        plt.subplot(211)
        plt.plot(aw,ar4,'-',t,tv,'*')
        plt.gca().set_title(title[0]) 
        plt.subplot(212)
        plt.plot(td)
        plt.gca().set_title(title[1]) 
        plt.tight_layout()
        if pts<00:
            plt.show()

    return(a1,t)













