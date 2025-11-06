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



mb=1
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
Q=9.6
R=2
S=14
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
for i in range(0,(1)):
    pkv=[]
    print(c-2, 'beat packet', i)
    if i==0:
        k=0
        k1= round((pk[(mb-1)]+pk[(mb)])/2)+2
    elif i>0 and i <(c-1):
        k=round((pk[((i*mb)-1)]+pk[((i*mb))])/2)+1
        k1=round((pk[(((i+1)*mb)-1)]+pk[(((i+1)*mb))])/2)+1
    else:
        k=round((pk[((i*mb)-1)]+pk[((i*mb))])/2)+1
        k1=l
    
    print('8888888888888', k, k1)
    k=int(k)
    k1=int(k1)
    b1=a[k:k1]
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
            
            if p!=S:
                w3=w3*0
                
            else:
                #print(j,p,len(w2))
                gf=ko.adi(gf,w3,0,0)

                    
            s1.append(w3)
               
        y=itqwt(s1,Q,R, k1)
        
        print(s1)
        fr=ko.adi(fr,y,0,0)

    (ss1)=bfm.headerbyte(k1,Q,R,S,v,mb,gf,tsv)
    (k11,Q1,R1,S1,v1,mb1,a11,kth,bx,tr3,ltt)=bfm.revheaderbyte(ss1,tsv)
 
    #print('8888888888888', v)
    #print('8888888888888', fr)
   # print('8888888888888', mn)
    mn1=ko.tke(fr,5,0)
    fr= fr[0:5]
    (fn4)=ko.antipca(v,fr,mn1)
    tg=ko.fnl(fn4,0)
    b2=np.transpose(b2)
    bb=ko.adi(bb,b2,0,0)
    
bb=np.transpose(bb)
v2=ko.fnl(bb,0)



bbg=fr
plt.figure(1)
for i in range(0,5):
    plt.plot(bbg[i])

bbg=str1
plt.figure(2)
for i in range(0,5):
    plt.plot(bbg[i])



#er=ko.err(tg,v2,1)
     



#plt.show()                       
                          
        
        
        
        
        
        
       
      
    

            
        
    
    
    














