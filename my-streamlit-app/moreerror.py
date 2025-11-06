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
import rlechq as rq


def mrer(str1,v,tsv,cl,bx,k11,b4,ln):
    if cl>0:
        vfe=v[0,0]
        vp=v
        v=np.transpose(v)
        vrest=v[1:9]
        vfe=round(vfe*1000)
        vfe=vfe/1000
        
     

        v=v[1:9]
        vb=[8,8,8,8,8,8,8,8]
        (vq,lb)=ko.quan(v,vb) ### lb
        #print(lb)
        #lb=ko.lnr(lb) ## it will stay



        gh=np.ones(10)
        r=ko.dquan(vq,(8*gh),lb)
        gh=np.ones(8)
        gg=vfe*gh
        v=np.transpose(v)
        v1=ko.adi(r,(gg),0,1)
        v1=np.transpose(v1)
        #print(vp-v1)


        (vq,lb)=ko.quan(str1,tsv)
        r=ko.dquan(vq,tsv,lb)
        #print(str1-r)
        fr=r

        mn1=ko.tke(fr,5,0)
        fr= fr[0:5]
        (fn4)=ko.antipca(v1,fr,mn1)
        #print(bx,k11)
        #print(fn4.shape)
        if bx[0]==1:
            fn4=np.transpose(fn4)
            fv=fn4[0:(int(k11)-1)]
            fv=np.transpose(fv)
            #print('tttt')
        else:
            fv=fn4
        #print(fv.shape)

        tg=ko.fnl(fv,0)
        tg=np.transpose(tg)

        b4=np.transpose(b4)

        
        b41=ko.fnl(b4,0)
        b41=np.transpose(b41)

        #print(tg-b41)

        tg=np.transpose(tg)
        b41=np.transpose(b41)
        [m1,m2]=b41.shape
        dat=k11*(sum(tsv))
        dat=dat+653
        dat1=m2
        ############
        bg=ko.err(tg,b41,1,0)  ##############


        #str1=np.transpose(str1)
        #print('888888',str1.shape)


        d=rq.rlemat(str1,tsv,1,k11)
        dat2=len(d)
        dat3=ln*(sum(tsv))
        #print(dat1,dat,dat2,dat3,650,bg[12,0]) 
        


        
        

        
        
        
        #print(r)


        


    c=0
        
        
        


        

    return(dat1,dat,dat2,dat3,650,bg[12,0])
