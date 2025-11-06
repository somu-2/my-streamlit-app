import numpy as np
import korboi as ko
import rle
import math
import rlechq as rq
from numpy import random
from tqwt import tqwt
import csv
import numpy as np
import rprak as rpk
#import rle
from numpy import savetxt
from numpy import genfromtxt
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
import tsvaddfnc as tsadd


def headerbyte(k1,Q,R,J,v,mb,gf,tsv,kgf,sf):
    c=[]
    #print('com',v)
    if mb==1:
       x1=[0,0]
      # x2=0
    elif mb==5:
       x1=[0,1]
       #x2=5*800;
    elif mb==10:
       x1=[1,0]
      # x2=10*800
    elif mb==15:
       x1=[1,1]
    #print('com td ', k1,sf)
      # x2=15*800
    #k1=k1-x2
    c=np.concatenate((c,x1))
    o1=round(sf*0.4*mb)
    o2=round(0.015*sf)
    sf=sf-200
    c1 = rle.tobin(sf, 2, 10, 0)
    c = np.concatenate((c, c1))
    
    
    k1=k1-o1
    #print('com 222222',sf,o1,o2,k1)


    c1=rle.tobin(k1,2,o2,0)
    c=np.concatenate((c,c1))


    vg1=int(Q)
    vg2=(Q*10)-(vg1*10)
    vg2=int(vg2)
    
    vg1=rle.tobin(vg1, 2, 4, 0)
    c=np.concatenate((c,vg1))
    vg2=rle.tobin(vg2, 2, 4, 0)
    c=np.concatenate((c,vg2))

    vg3=J-6
    vg3=rle.tobin(vg3, 2, 4, 0)
    c=np.concatenate((c,vg3))
    #print('com',Q,R,J)






    
    #if Q==11:
        #x1=[0]
    #else:
        #x1=[1]
    #c=np.concatenate((c,x1))
    vfe=v[0,0]
    v=np.transpose(v)
    vrest=v[1:9]
    if vfe<0:
        sgn=[0]
    else:
        sgn=[1];
    c=np.concatenate((c,sgn))
    vfe=round(vfe*1000)
    
    c3=rle.tobin(abs(vfe),2,12,0)
    c=np.concatenate((c,c3))

    v=v[1:9]
    vb=[8,8,8,8,8,8,8,8]
    (vq,lb)=ko.quan(v,vb) ### lb
    #print(lb)
    lb=ko.lnr(lb)
    
    for i in range(0,4):
        if lb[i]<0:
            sgn=[0]
        else:
            sgn=[1];
        c=np.concatenate((c,sgn))
        bl=round(lb[i]*1000)
        
        c3=rle.tobin(abs(bl),2,12,0)
        c=np.concatenate((c,c3))
        
    vl=ko.lnr(vq)
    c3=[]
    for i in range(0,len(vl)):
        c1=rle.tobin(int(vl[i]),2,8,0)
        
        c=np.concatenate((c,c1))
    #print('com', gf)
    #savetxt('gf1.csv', gf, delimiter=',')
   # print(tsv)
    d=rq.rlemat(gf,tsv,1,kgf)
    #print(kgf)
    c=np.concatenate((c,d))
    return(c)








def revheaderbyte(c,tsv):
    #print('jkjkjkj',tsv)
    #(c,tsv)=tsadd.tsvadd(cu,tsv,1)

    
    c1=c[0:2]
    x1=rle.frbin(c1,2,0)
    
    if x1==0:
        #x2=0;
        mb=1
    elif x1==1:
        mb=5
        #x2=5*800
    elif x1==2:
        mb=10
        #x2=10*800

    elif x1==3:
        mb=15
        #x2=15*800



    c1=c[2:12]
    sf = rle.frbin(c1, 2, 0)
    sf=sf+200
    o2 = round(0.015 * sf)
    o2=o2+12

    c1 = c[12:o2]

    betln=rle.frbin(c1,2,0)
    o1=round(sf*0.4*mb)

    betln=betln+o1

    #print('decom td ', betln, sf,o1,o2)



    vd1=c[o2:(o2+4)]
    vd2=c[(o2+4):(o2+8)]
    vd3=c[(o2+8):(o2+12)]
    vd1=rle.frbin(vd1,2,0)
    vd2=rle.frbin(vd2,2,0)
    vd3=rle.frbin(vd3,2,0)
    Q=vd1+0.1*vd2
    R=2
    S=int(vd3+6)
    #print('decom',Q,R,S,betln)





    
    #x1=c[o2]
    #if x1==0:
      #  Q=11
      #  R=2
      #  S=8
    #else:
        #Q=6.7
        #R=2
        #S=15
    c1=c[o2+12]
    
    if c1==0:
        sgn=-1
    else:
        sgn=1
    k=o2+13
    k1=o2+25

    #print('2222',betln)
    tr1=random.rand(int(betln))
    tr2 = tqwt(tr1, Q,R,S)
        
    tr3=[]
    for p in range(0,(S+1)):
        w1=tr2[(p):(p+1)]
        w2=w1[0]
        w2=np.array(w2)
        w3=w2.real
        
        if p!=S:
            w3=w3*0
            tr3.append(w3)
            #print(len(w2))
        else:
            lth=len(w2)
        
    lth=lth+2
    #print('decom qrs lth',Q,R,S,lth)


    
    c1=c[k:k1]
    vfe=rle.frbin(c1,2,0)
    vfe=vfe*sgn
    vfe=vfe/1000
    #print('decom vfe', vfe)
    k=k1
    lb1=[]
    for i in range(0,4):
        c1=c[k:(k+13)]
        c2=c1[0]
        if c2==0:
            sgn=-1
        else:
            sgn=1
        c2=c1[1:13]
        vf=rle.frbin(c2,2,0)
        vf=vf*sgn
        vf=vf/1000
        k=k+13
        lb1.append(vf)
    lb1=np.array(lb1)
    lb=ko.alr(lb1,2) #######
    lb1=[]
    for i in range(0,70):
        c1=c[k:(k+8)]
        vf=rle.frbin(c1,2,0)
        lb1.append(vf)
        k=k+8
    vq1=lb1
    vq=ko.alr(vq1,7)
    gh=np.ones(10)
    r=ko.dquan(vq,(8*gh),lb)
    gh=np.ones(8)
    gg=vfe*gh
    v=ko.adi(r,(gg),0,1)
    v=np.transpose(v)
    #print('decom',v)
   
    pq=int(len(c))
    d=c[k:(pq+1)]
    (a11,kp)=rq.matrle(d,lth,64,6,tsv)
    #print('decom',a11)
    #print(c.shape, (k+kp))
    bx=c[int(k+kp)]
    #print('i am bx', bx)
    k=k+1+kp
    


    
    
   

    return(betln,Q,R,S,v,mb,a11,k,bx,tr3,lth)


























