import numpy as np
import rprak as rpk
import rle
from numpy import savetxt
from numpy import genfromtxt
import csv
import korboi as ko
import matplotlib.pyplot as plt
import byteform as bfm
#import fbm
from tkinter import filedialog
#import pandas as pd
import sys
import time
import tkinter as tk
from tqwt import tqwt
from itqwt import itqwt
from numpy import random
import tsvaddfnc as tsadd


def rlemat(a1,tsv,vf,kgf):
        #print(a1.shape, kgf,tsv)
        
        (vq,lb)=ko.quan(a1,tsv)
        #print('lb com rle initial',lb)
        #zqq1=ko.dquan(vq,tsv,lb)
        h1=ko.matarryfixbyte(lb,15)
        tsz=tsadd.tsvadd(tsv,0)
        h1=np.concatenate((h1,tsz))
        [m1,m2]=vq.shape
        #vq=np.transpose(vq) 
        f=0
        c2=[]
        c=[]
        nb1=0
        nb2=0
        for i in range(0,1):
                for j in range(0,int(m1)):
                    #print(j)
                    x=ko.tke(vq,j,0)
                    xg=x
                    x1=x[2:(kgf+2)]
                    (x2,x3)=rle.decum(x1,0,0)
                    c1=rle.tobin(int(x3[0]),2,int(tsv[f]),0)
                    c11=rle.stb(int(x3[1]),2,int(tsv[f]),0)
                    f=f+1
                    c2=np.concatenate((c2,c1,c11))
                    f2,w,w1,w2,s2,f1,f3=rle.rl(0,x2,7)
                    
                    c1=rle.tobin(f3,2,4,0)
                    c11=rle.tobin((f3-f1),2,3,0)
                    c12=rle.tobin((w-0),2,15,0)#########
                   # print('com',j, w,c12)
                    #print('fffff', f3,f1,w)
                    c2=np.concatenate((c2,c1,c11,c12))
                    for h in range(0,len(w2)):
                        c1=rle.tobin(int(w2[h]),2,3,0)
                        c2=np.concatenate((c2,c1))
                    for h in range(0,len(s2)):
                        c1=rle.stb(int(s2[h]),2,(f3-1),0)
                        c2=np.concatenate((c2,c1))
                    for h in range(0,len(w1)):
                        c1=rle.tobin(int(w1[h]),2,f1,0)
                        c2=np.concatenate((c2,c1))
                    f21,ww,ww1,ww2=rle.rle(0,x2,7)
                    #print('com',j, len(w1), w, len(s2))
                    #print(f1,f2,f3)
                    #print('$$$$$$$$$$')
                    mm=rle.rl1(1,f2,7,w1,(w2),s2)
                    
                    rt=(np.subtract(mm,x2))
                    rt=abs(rt)
                    bn1=(f1*len(w1)+3*len(w2)+f3*len(s2))
                    bn2=len(ww1)*f3+3*len(ww2)
                    nb1=nb1+bn1
                    nb2=nb2+bn2
                    c=np.concatenate((c,c2))
                    #print('dek re', len(c2))
                    q1=rle.tobin(x[0],2,8,0)
                    q2=rle.tobin(x[1],2,8,0)
                    #print('fff',x)
                    c=np.concatenate((c,q1,q2))
                    c2=[]
                    c2=np.array(c2)


                
                if vf>0:
                        #print(len(h1))
                        
                        c=np.concatenate((h1,c))
        #print('com',len(c))






        return(c)


def matrle(c,lth,hdbysize,m1,tsv):
        #print('com',len(c))
        u=0
        w2=[]
        s2=[]
        w1=[]
        ts9=[]
        k1=0
        #s1=lb
        h2=[]
        #print('decom',lth,tsv)
        #lth=230
        if hdbysize>0:
                ft=c[0:hdbysize]
                h2=ko.bytematarryfix(ft,4,2,15)
                k1=hdbysize
        tsz1=c[k1:(k1+12)]
        tsv=tsadd.tsvadd(tsz1,1)
        k1=k1+12
        #print(tsv)
       # print('decom rle intial',h2)
        for i in range(0,int(m1)):
            #print(i)
            k=k1
            k1=k+tsv[u]
            #print(k, k1, tsv[u])
            
            c1=c[int(k):int(k1)]
            #print(c1)
            k=k1
            k1=int(k1+tsv[u]+1)
            
            x3=rle.frbin(c1,2,0) ##
            c1=c[int(k):int(k1)]  
            x4=rle.sfb(c1,2,0) ##
            x3=np.concatenate(([x3],[x4]))
            
            k=k1
            k1=k+4
            c1=c[int(k):int(k1)]  
            f3=rle.frbin(c1,2,0) ##
            k=k1
            k1=k+3
            c1=c[int(k):int(k1)]  
            f1=rle.frbin(c1,2,0) ##
            f1=f3-f1
            k=k1
            k1=k+15####################
            c1=c[int(k):int(k1)]  
            w=rle.frbin(c1,2,0) ##
           # print('decom',i, w,c1)
            cn0=0
            for j in range(0,int(w)):
                k=k1
                k1=k+3
                c1=c[int(k):int(k1)]  
                xw=rle.frbin(c1,2,0)
                if xw==0:
                    cn0=cn0+1
                w2=np.concatenate((w2,[xw]))
            for j in range(0,cn0):
                k=k1
                k1=k+f3
                c1=c[int(k):int(k1)]  
                xw=rle.sfb(c1,2,0)
                s2=np.concatenate((s2,[xw]))
            cn0=0
            cn=lth-sum(w2)+w-len(s2)+1-4
            for j in range(0,int(cn)):
                k=k1
                k1=k+f1
                c1=c[int(k):int(k1)]  
                xw=rle.frbin(c1,2,0)
                w1=np.concatenate((w1,[xw]))
            f=int((2**f1)-1)
            f2=round(f//2)+1
            #print('decom',i, len(w1), w, len(s2))
            #print(f1,f2,f3)
            #print('##############')
            mm=rle.rl1(1,f2,7,w1,(w2),s2)
            y=rle.decum(mm,x3,1)
            p1=c[int(k1):int(k1+8)]
            pp1=rle.frbin(p1,2,0)
            
            p1=c[int(k1+8):int(k1+16)]
            pp2=rle.frbin(p1,2,0)
            y=np.concatenate(([pp1],[pp2],y))
            #print(k1, len(y))
            ts9=ko.adi(ts9,y,0,0)
            k1=k1+16
            w1=[]
            w2=[]
            s2=[]
            u=u+1
            gh=k1
            x3=[]
        zqq=ko.dquan(ts9,tsv,h2)

        return(zqq,gh)


#d=rlemat(a1,tsv,1)
#a11=matrle(d,230,56,6,tsv)







                
