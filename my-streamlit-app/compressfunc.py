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
import moreerror as morer
import moreerror1 as morer1
import math
import tsvaddfnc as tsadd



        
    
    

def dcom(tsv,crt,sf,mb,pq,momo,QRS,data,pk):
    tr1=[]
    ts9=[]
    z2=[]
    tsm=[]
    #tsv=[]
    tr2=[]
    ff2=[]
    vv1=[]
    bmn=-100


    bk1=0
    bk2=0
    bk3=0
    bk4=0
    bk5=0
    bk6=0

    #Q=9.6
    #R=2
    #S=14
    Q=(QRS[0])
    R=int(QRS[1])
    S=int(QRS[2])
    #print(Q,R,S)
    #tsv=[4,4,6,6,8,8]
    if crt==0:
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
        #a1=genfromtxt('data.csv', delimiter=',')
        #pk1=genfromtxt('pk.csv', delimiter=',')
        a1=data
        pk1=np.array(pk)

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
    if pq==0:
        lp=c-2
    else:
        lp=pq
    for i in range(0,(lp)):
        pkv=[]
        #print(c-2, 'beat packet', i)
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
        
        k=int(k)
        k1=int(k1)
        b1=a[k:k1]
        b4=b1
        #print(i, kk1)
        if kk1%2 !=0:
            bx=ko.tke(b1,0,0)
            b1=ko.adi(b1,bx,0,0)
            bx=[1]
            kk1=kk1+1
        else:
            bx=[0]
        #print(b1.shape)
        b2=np.transpose(b1)
        
        
        (v,str1,mn,sw)=ko.pca(b2,0,0,0)
        (fn1)=ko.antipca(v,str1,mn)
        fn2=np.transpose(fn1)
        #print(v) 
        #print(str1)
       # print(mn)
        str1=ko.adi(str1,mn,0,0)
        #savetxt('str1.csv', str1, delimiter=',')
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
        if momo>0:
            tsv=[]
            if momo==1:
                tsvv=genfromtxt('tsv1.csv', delimiter=',')
                [m1,m2]=tsvv.shape
            elif momo==2:
                tsvv=genfromtxt('tsv2.csv', delimiter=',')
                [m1,m2]=tsvv.shape
            else:
                tsvv=genfromtxt('tsv3.csv', delimiter=',')
                [m1,m2]=tsvv.shape
            
            for cv in range(0,m1):
                tsv3=ko.tke(tsvv,cv,0)
                (dat1,dat2,dat3,dat4,dat5,dat6)=morer.mrer(str1,v,tsv3,1,bx,kk1,b4,lstln)
                #bk1=bk1+dat1
                #bk2=bk2+dat2
                #bk3=bk3+dat3
                #bk4=bk4+dat4
                #bk5=bk5+dat5
                #bk6=bk6+dat6

                #crpca=(bk1*12*16)/(bk2+bk5)
                erpca=dat6/(i+1)
                crpcall=(dat1*12*16)/(dat3+dat5)
                #crpcattq=(bk1*12*16)/(bk4+bk5)
                if momo==2:
                    qscq=(crpcall)/(erpca*erpca)
                elif momo==1:
                    qscq=(crpcall*crpcall)/(erpca)
                else:
                    qscq=(crpcall)/(erpca)
                if qscq> bmn:
                    bmn=qscq
                    tsv=tsv3
                #print('qscq',qscq,tsv3)
            #print('9999',tsv)
            bmn=-100

        else:
            crpca=0
            erpca=0
            crpcall=0
            crpcattq=0
            qscq=0
        #print('morer end')
        #print(tsv)

        (ss1)=bfm.headerbyte(kk1,Q,R,S,v,mb,gf,tsv,lstln,1000)
        
        ss2=np.concatenate((ss2,ss1,bx))
        #(ss2,gb)=tsadd.tsvadd(ss2,tsv,0)
        if momo>0:
            (dat1,dat2,dat3,dat4,dat5,dat6)=morer1.mrer1(str1,v,tsv,1,bx,kk1,b4,lstln)
            bk1=bk1+dat1
            bk2=bk2+dat2
            bk3=bk3+dat3
            bk4=bk4+dat4
            bk5=bk5+dat5
            bk6=bk6+dat6


            
            
        #print('i am bx', bx)
        print(lp,' beat_matrix ',(i+1), ' -th length ', kk1, ' bit_length ',(len(ss1)+1))
        
        b2=np.transpose(b2)
        #b4=np.transpose(b4)
        if i==0:
            dc=b2
            dc1=b4
        else: 
            dc=np.concatenate((dc,b2))
            dc1=np.concatenate((dc1,b4))

            
    if momo>0:
        #bk5=0
        crpca=(bk1*12*16)/(bk2+bk5)
        erpca=bk6/(i+1)
        crpcall=(bk1*12*16)/(bk3+bk5)
        crpcattq=(bk1*12*16)/(bk4+bk5)
        qscq=(crpcall*crpcall)/erpca
    else:
        crpca=0
        erpca=0
        crpcall=0
        crpcattq=0
        qscq=0



    



    #savetxt('ss2.csv', ss2, delimiter=',')
    #savetxt('dc.csv', dc, delimiter=',')
    #savetxt('dc1.csv', dc1, delimiter=',')


    return(ss2,crpca,erpca,crpcall,crpcattq,qscq,tsv,dc1)
