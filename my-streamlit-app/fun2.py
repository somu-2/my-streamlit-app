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
import bom2

tqpar=genfromtxt('tqpar.csv', delimiter=',')

gf=[]
ap=[]


sf=1000
gd=0



mult=1
ap1=np.zeros(mult+1)
for i in range (0,mult):
    aa=ko.get(0)
   # print(aa[0,0])
    if i==0:
        ap=aa 
    else:
        ap=np.concatenate((ap,aa))
        
    [m1,m2]=ap.shape
    ap1[i+1]=m1


for d in range(0,mult):
    mf=ap[int(ap1[d]):int(ap1[d+1])]
    pq=1    #will take mf if pq=0, else will ask
    crt=1   # =1, to operate
    pts=1
    (data,pk)=pkdt.peakdt(sf,pq,crt,pts,mf)
    pq=10  # for compression

    for i in range (0,0):
        QRS=ko.tke(tqpar,2,0)
        for j in range (0,0):
            momo=i+1;
            mb=j*5
            #pq=2
            if j==0:
                mb=mb+1
            tq1=ko.tke(tqpar,2,0)
            k=(i*4)+j+1
            if gd>0:
                pq=ko.mbpq(mb)
            (cr,er,tsv1,ff)=bom2.crck(momo,pq,mb,QRS,k)
            
           # print('***    CR is', cr, 'PRD= ', er[12,0], 'PRDN= ', er[12,1], 'Q_level', tsv1, mb,momo,QRS)
            bh=[k]
            g1=ko.tke(er,0,1)
            g2=ko.tke(er,1,1)
            g1=g1[0:12]
            g2=g2[0:12]
            bh=np.concatenate((bh,tsv1, [mb]))
            bh=np.concatenate((bh,[momo],QRS,ff))
            bh=np.concatenate((bh,g1,g2))
            gf=ko.adi(gf,bh,0,0)
            print('K is = ',k, ' for ',(d+1), '-th file out of ', (mult))
            
            

    for i in range (2,3):
        QRS=ko.tke(tqpar,i,0)
        for j in range (1,2):
            k=(i*4)+j+9
            momo=3;
            mb=j*5
            #pq=2
            if j==0:
                mb=mb+1
            tq1=ko.tke(tqpar,2,0)
            if gd>0:
                pq=ko.mbpq(mb)
            (cr,er,tsv1,ff)=bom2.crck(momo,pq,mb,QRS,k)
            
            #print('***    CR is', cr, 'PRD= ', er[12,0], 'PRDN= ', er[12,1], 'Q_level', tsv1, mb,momo,QRS)
            bh=[k]
            g1=ko.tke(er,0,1)
            g2=ko.tke(er,1,1)
            g1=g1[0:12]
            g2=g2[0:12]
            bh=np.concatenate((bh,tsv1, [mb]))
            bh=np.concatenate((bh,[momo],QRS,ff))
            bh=np.concatenate((bh,g1,g2))
            gf=ko.adi(gf,bh,0,0)
            print('K is = ',k, ' for ',(d+1), '-th file out of ', (mult))


    gu=0
    if gu>0:
        aq1=genfromtxt('result.csv', delimiter=',')
        [m1,m2]=gf.shape
        for i in range(0,m1):
            aq2=ko.tke(gf,i,0)
            aq1=ko.adi(aq1,aq2,0,0)
        savetxt('result.csv', aq1, delimiter=',')
    gf=[]





