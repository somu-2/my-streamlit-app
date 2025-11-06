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



mb=5
sf=1000
crt=0
tr1=[]
ts9=[]
z2=[]
tsm=[]
tsv=[]
tr2=[]
ff2=[]
vv1=[]
#Q=9.6
#R=2
#S=14
Q=6.7
R=2
S=15
tsv=[4,4,6,6,8,8]
if crt>0:
    pkv=[]
    tv=[]
    #ar=genfromtxt('104s0306lre.csv', delimiter=',')
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
    
    for i in range(0,8):
        xe=[0,1,6,7,8,9,10,11]
        a=ko.tke(aa,xe[i],1)
        a1=ko.adi(a1,a,1,0)
    savetxt('data.csv', a1, delimiter=',')
    savetxt('pk.csv', t, delimiter=',')
    for i in range(0,len(t)):
        x=int(t[i])
        t1=ar4[x]
        tv.append(t1)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(aw,ar4,'-',t,tv,'*')
    plt.subplot(212)
    plt.plot(td)
    plt.show()
    
else:
    a1=genfromtxt('data.csv', delimiter=',')
    pk1=genfromtxt('pk.csv', delimiter=',')
    pk1=pk1

s=len(pk1)-2
c=0
w1= round((pk1[0]+pk1[1])/2)
w2= round((pk1[s-1]+pk1[s-2]))
w1=int(w1)
w2=int(w2)
a=a1[w1:w2]
pk=pk1[1:(s+1)]
pk=pk-w1
dc=[]
dc1=[]
for i in range(0,100):
    if (s-mb)>=0:
        c=c+1
        s=s-mb
if s>2:
    c=c+1
    l=len(a)
else:
    l=round((pk1[(s-3)]+pk1[(s-2)])/2)
l=int(l)
bb=[]
fn2=[]
ss2=[]
for i in range(0,(c-2)):
    pkv=[]
    print(c-2, 'beat packet', i)
    if i==0:
        k=0
        k1= round((pk[(mb-1)]+pk[(mb)])/2)+1
    elif i>0 and i <(c-1):
        k=round((pk[((i*mb)-1)]+pk[((i*mb))])/2)+1
        k1=round((pk[(((i+1)*mb)-1)]+pk[(((i+1)*mb))])/2)+1
    else:
        k=round((pk[((i*mb)-1)]+pk[((i*mb))])/2)+1
        k1=l
    kk1=k1-k
    #if kk1%2 !=0:
    print('8888888888888', kk1, k, k1)
    k=int(k)
    k1=int(k1)
    b1=a[k:k1]
    b4=b1
    print(i, kk1)
    if kk1%2 !=0:
        bx=ko.tke(b1,0,0)
        b1=ko.adi(b1,bx,0,0)
        bx=[1]
        kk1=kk1+1
    else:
        bx=[0]
    print(b1.shape)
    b2=np.transpose(b1)
    
    
    (v,str1,mn,sw)=ko.pca(b2,0,0,0)
    (fn1)=ko.antipca(v,str1,mn)
    fn2=np.transpose(fn1)
    #print(v) 
    #print(str1)
   # print(mn)
    str1=ko.adi(str1,mn,0,0)
    savetxt('str1.csv', str1, delimiter=',')
    fr=[]
    
    gf=[]

    for j in range(0,(6)):
        
        strtk=ko.tke(str1,j,0)
        
        w = tqwt(strtk, Q,R,S)
        
        s1=[]
        for p in range(0,(S+1)):
            w1=w[(p):(p+1)]
            w2=w1[0]
            w2=np.array(w2)
            w3=w2.real
            #print(len(w2))
            if p!=S:
                w3=w3*0
            else:
                
                gf=ko.adi(gf,w3,0,0)
                lstln=len(w3)

                    
            s1.append(w3)
               
        y=itqwt(s1,Q,R, kk1)
        fr=ko.adi(fr,y,0,0)

    (ss1)=bfm.headerbyte(kk1,Q,R,S,v,mb,gf,tsv,lstln,1000)
    
    ss2=np.concatenate((ss2,ss1,bx))
    print('i am bx', bx)
    print('ss1 length',(len(ss1)+1))
    b2=np.transpose(b2)
    #b4=np.transpose(b4)
    if i==0:
        dc=b2
        dc1=b4
    else: 
        dc=np.concatenate((dc,b2))
        dc1=np.concatenate((dc1,b4))




savetxt('ss2.csv', ss2, delimiter=',')
savetxt('dc.csv', dc, delimiter=',')
savetxt('dc1.csv', dc1, delimiter=',')










    
