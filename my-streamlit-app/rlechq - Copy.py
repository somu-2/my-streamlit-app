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

ce=1
if ce>0:
        a1=genfromtxt('gf.csv', delimiter=',')
        tsv=[4,4,6,6,8,8]
        (vq,lb)=ko.quan(a1,tsv)
        zqq1=ko.dquan(vq,tsv,lb)
        h1=ko.matarryfixbyte(lb,13)

        #vq=np.transpose(vq) 
        f=0

        c2=[]
        c=[]
        nb1=0
        nb2=0
        for i in range(0,1):
                for j in range(0,6):
                    x=ko.tke(vq,j,0)
                    xg=x
                    x1=x[2:230]
                    (x2,x3)=rle.decum(x1,0,0)
                    c1=rle.tobin(int(x3[0]),2,int(tsv[f]),0)
                    c11=rle.stb(int(x3[1]),2,int(tsv[f]),0)
                    f=f+1
                    c2=np.concatenate((c2,c1,c11))
                    f2,w,w1,w2,s2,f1,f3=rle.rl(0,x2,7)
                    c1=rle.tobin(f3,2,4,0)
                    c11=rle.tobin((f3-f1),2,3,0)
                    c12=rle.tobin((w-0),2,10,0)
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
                    c=np.concatenate((c,q1,q2))
                    c2=[]
                    c2=np.array(c2)

                c=np.concatenate((h1,c))

                



                u=0
                w2=[]
                s2=[]
                w1=[]
                ts9=[]
                k1=0
                s1=lb
                lth=230
                mb=1
                ft=c[0:56]
                h2=ko.bytematarryfix(ft,4,2,13)
                k1=56
              
                for i in range(0,6):
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
                    k1=k+10
                    c1=c[int(k):int(k1)]  
                    w=rle.frbin(c1,2,0) ##
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
                    #print(i, len(w1), w, len(s2))
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

                #g1=(lth-2)*mb
                #g2=ko.sum(pd)
                #g1=g1-g2
                #

def rlemat(a1,tsv,vf,kgf):
        (vq,lb)=ko.quan(a1,tsv)
        #print('lb com rle initial',lb)
        #zqq1=ko.dquan(vq,tsv,lb)
        h1=ko.matarryfixbyte(lb,15)
        [m1,m2]=vq.shape
        #vq=np.transpose(vq) 
        f=0
        c2=[]
        c=[]
        nb1=0
        nb2=0
        for i in range(0,1):
                for j in range(0,int(m1)):
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
                    c12=rle.tobin((w-0),2,10,0)
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
                        
                        c=np.concatenate((h1,c))






        return(c)


def matrle(c,lth,hdbysize,m1,tsv):
        u=0
        w2=[]
        s2=[]
        w1=[]
        ts9=[]
        k1=0
        #s1=lb
        h2=[]
        #print('decom',lth)
        #lth=230
        if hdbysize>0:
                ft=c[0:hdbysize]
                h2=ko.bytematarryfix(ft,4,2,15)
                k1=hdbysize
        #print('decom rle intial',h2)
        for i in range(0,int(m1)):
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
            k1=k+10
            c1=c[int(k):int(k1)]  
            w=rle.frbin(c1,2,0) ##
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
            #print(i, len(w1), w, len(s2))
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







                
