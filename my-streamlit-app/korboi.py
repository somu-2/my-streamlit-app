# from numpy import savetxt
# import csv
# savetxt('data.csv', a, delimiter=',')
#
#
# from numpy import genfromtxt
# a = genfromtxt('data.csv', delimiter=',')




import numpy as np
import math
import matplotlib.pyplot as plt
import rle
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sys
import time
from tqwt import tqwt
from itqwt import itqwt
from numpy import random

def adi(main,pad,u,g):
    a=main
    b=pad
    t=[]
    c2=[]
    a=np.array(a)
    b=np.array(b)
   
    c=a.shape
    cl=len(c)
    if cl==1:
        c2=int(c[0])
        if c2==0:
            return(b)
        else:
            if u==0:
                if g==0:
                    r=np.vstack((a,b))
                else:
                    r=np.vstack((b,a))
            else:
                if g==0:
                    r=np.column_stack((a,b))
                else:
                    r=np.column_stack((b,a))
    else:
        if u==0:
            if g==0:
                r=np.vstack((a,b))
            else:
                r=np.vstack((b,a))
        else:
            if g==0:
                r=np.column_stack((a,b))
            else:
                r=np.column_stack((b,a))
    return(r)
def tke(a,b,c):
    a=np.array(a)
    c1=a.shape
    m=int(c1[1])
    n=int(c1[0])
    if c==0:
        e=np.ones(m)
        for i in range(0,m):
            e[i]=a[b,i]
    else:
        e=np.ones(n)
        for i in range(0,n):
            e[i]=a[i,b]
    return(e)
def pt(a):
    c=len(a)
    r=[]
    for i in range(0,c):
        r.append(i)
    return(r)
def ld_bt(ld,pk):
    ld2=[]
    p=[]
    pd=[]
    m=len(pk)
    pkd=[]
    btmt=[]
    pkf=[]
    pkb=[]
    vf=-100
    vb=-100
    
    for i in range(0,(m-1)):
        j=round((pk[i]+pk[i+1])/2)
        pkd.append(j)
        x=pk[i+1]-pkd[i]
        if x>=vf:
            vf=x
        if i!=(m-2):
            pkf.append(x)
        y=pkd[i]-pk[i]
        if y>vb:
            vb=y
        if i!=0:
            pkb.append(y)
    vf=vf+5
    vb=vb+5
    for i in range(0,(m-2)):
        x=vf-pkf[i]
        x1=np.ones(int(x))
        x2=x1*(ld[int(pkf[i])])
        x3=ld[int(pkd[i]):(int(pkd[i+1]))]
        ld2=np.concatenate((ld2,x3))
        y=vb-pkb[i]
        y1=np.ones(int(y))
        y2=y1*(ld[(int(pkb[i]))])
        t1=np.concatenate(([x2,x3,y2]))
        
        btmt=adi(btmt,t1,0,0)
        p=[x,y]
        pd=adi(pd,p,0,0)
    ld1=ld[int(pkd[0]):int(pkd[m-2])]
    return(ld1,btmt,pd)


def btld(a,pk):
    pkd=[0.0]
  
    m=len(pk)
    pkf=[]
    pkb=[]
    vf=(pk[0])
    pkf.append(vf)
    tt1=len(a)-pk[(m-1)]
    vb=tt1
    for i in range(0,(m-1)):
        j=round((pk[i]+pk[i+1])/2)
        pkd.append(j)
        x=pk[i+1]-pkd[i+1]
        y=pkd[i+1]-pk[i]
        if x>vf:
            vf=x
        pkf.append(x)
        if y>vb:
            vb=y
        pkb.append(y)
   
    pkb.append(tt1)
    pkd.append(len(a))
    ld=a
    ld2=[]
    t1=[]
    btmt=[]
    pd=[]
    for i in range(0,(m)):
        x=vf-pkf[i]
        x1=np.ones(int(x))
        t1=int(pkd[i])
        if t1==0:
            x2=x1*(ld[t1])
        else:
            x2=ld[int(t1-x):t1]
        x3=ld[int(pkd[i]):(int(pkd[i+1]))]
        y=vb-pkb[i]
        y1=np.ones(int(y))
        t2=(pkd[i+1]-1)
        if t2==(len(a)-1):
            y2=y1*(ld[(int(t2))])
        else:
            y2=ld[int(t2+1):int(t2+1+y)]
        t1=np.concatenate(([x2,x3,y2]))
        btmt=adi(btmt,t1,0,0)
        p=[x,y]
        pd=adi(pd,p,0,0)
    
    
    
    return(btmt,pd)

    







    
def bt_ld(btmt,pd):
    ld1=[]
    c1=btmt.shape
    m=int(c1[0])
    n=int(c1[1])
    for i in range(0,m):
        a1=tke(btmt,i,0)
        w1=int(pd[i,0])
        w2=int(pd[i,1])
        bt=a1[(w1):(n-w2)]
        ld1=np.concatenate((ld1,bt))
    return(ld1)

def rnd(a,r):
    a=np.array(a)
    b=a.shape
    c=len(b)
    if c==1:
        m=int(b[0])
        for i in range(0,m):
            a[i]=round(a[i],r)
    else:
        m=int(b[0])
        n=int(b[1])
        for i in range(0,m):
            for j in range(0,n):
                a[i,j]=round(a[i,j],r)
    return(a)
# b=main matrix
# r=2...no compression
# r=0...8 row matrix to 5 row matrix(lead-wise)
# r=1....then
#   q=5,10,15,20..beat matrix compression
#       5 : nu=(0/1),(3,2)
#       10: nu=(0/1),(5,4)
#       15: nu=(0/1),(6,5)
#       20: genuene compression
def pca(b,r,q,nu):
    c1=b.shape
    mn=[]
    m=int(c1[0])
    n=int(c1[1])
    am=[]
    for i in range(0,n):
        x=tke(b,i,1)
        y=np.mean(x)
        mn.append(y)
        x1=x-y
        
        am=adi(am,x1,1,0)
    am1=np.transpose(am)
    am2=np.matmul(am,am1)
    (ww,vv)=np.linalg.eig(am2)
  
    (v,w)=pcajh(vv,ww)
   
    v1=np.transpose(v)
    
    str2=np.matmul(v1,am)
   
    sw=tke(v,0,0)
    if r==0:
        str1=str2[(m-5):(m)]
       
        return(v,str1,mn,sw)
    elif r==1:
        sm=0
        sm1=0
        for i in range(0,m):
            sm=sm+(w[i]**2)
           
   
        for i in range(0,m):
            sm1=sm1+(w[(m-i-1)]**2)
            
            if sm1>=(sm*0.9):
                break
        if q==5:
            if nu==0:
                if i>2:
                    i=2
               # elif i<1:
                  #  i=1
            else:
                if i>1:
                    i=1
        elif q==10:
            if nu==0:
                if i>4:
                    i=4
               # elif i<2:
                #    i=2
            
            else:
                if i>3:
                    i=3
        elif q==15:
           
            if nu==0:
                if i>5:
                    i=5
              #  elif i<2:
                 #   i=2
               
            else:
                if i>4:
                    i=4
                   
          
        else:
            i=i
       
        str1=str2[(m-i-1):(m)]
    else:
        str1=str2
    return(v,str1,mn,i)
def antipca(v1,str2,mn):
    v=np.transpose(v1)
    s1=np.linalg.inv(v)
    
    cv=v1.shape
    c1=int(cv[0])
    cs=str2.shape
    if len(cs)==1:
        m=0
        n=int(cs[0])
    else:
        m=int(cs[0])
        n=int(cs[1])
    for i in range(0,(c1-m)):
        r=np.zeros(n)
        str2=adi(str2,r,0,1)
    m=c1
    fn=[]           
    s2=np.matmul(s1,str2)
    
    for i in range(0,n):
        q1=tke(s2,i,1)
        q2=q1+mn[i]
        fn=adi(fn,q2,1,0)
    return(fn)


def ercom(a,b):

    s=0
    s1=0
    s2=0
    s3=0
    m=len(b)
    amn=np.mean(a)
    amx=max(a)
    for i in range(0,m):
        x=(a[i]-b[i])
        xm=abs(x)
        x1=x**2
        z=(a[i]-amn)**2
        y=a[i]**2
        s=s+y
        s1=s1+x1
        s2=s2+z
        s3=s3+xm
    prd=((s1/s)**0.5)*100
    prdn=((s1/s2)**0.5)*100
    mae=(xm/m)*100
    mse=(s1/m)*100

    rmse=((mse/100)**0.5)*100
    e1=s/s1
    e2=math.log(e1,10)
    snr=10*e2
    r1=(amx**2)/(mse/100)
    #r2=math.log(r1,10)
    r2=0
    psnr=10*r2
    fn=[prd,prdn,mae,mse,rmse,snr,psnr]
    fn1=rnd(fn,2)
    fn2=fn1.tolist()
    return(fn2)
def err(a,b,p,kh1):
    c=a.shape
    d=len(c)
    if d==1:
        e=ercom(a,b)
        return(e)
    else:
        r4=[]
        po=[]
        kh=[]
        m=int(c[0])
        n=int(c[1])
        for i in range(0,m):
            r1=tke(a,i,0)
            r2=tke(b,i,0)
            r3=ercom(r1,r2)
            
            r4=adi(r4,r3,0,0)
        if p>0:
            for i in range(0,m):
                x=tke(r4,i,0)
                y=x.tolist()
                if i==0:
                    kx=y
                else:
                    kx=adi(kx,y,0,0)
                if kh1>0:
                    print('lead,', (i+1), 'error is', y)
            [u1,u2]=r4.shape
            

            for i in range(0,u2):
                x=tke(r4,i,1)
                x1=np.mean(x)
                
                po=np.concatenate((po,[x1]))
            
            po=np.around(po, 2)
            po1=po.tolist()
            if kh1>0:
                print('average ' , 'error is', po1)
            kx=adi(kx,po1,0,0)
        
        return(kx)
        
def pcajh(a,b):
    s2=[]
    c=len(b)
    b=np.array(b)
    b1=np.sort(b)
    
    for i in range(0,c):
        x = np.where(b == b1[i])
        y=int(x[0])
        s1=tke(a,y,1)
        s2=adi(s2,s1,1,0)
    
    return(s2,b1)

# to quantize 'a' matrix row wise...(3*10)
# b= q.level..(4,6,8)
# return for single lead(w=quatized.3*10.....qd=(diff,min))
#        for matrix, w1=spc.quantized.5*10....e1=[2*2]
def quan(a,b):
    e1=[]
    w1=[]
    w2=[]
    c=a.shape
    c1=int(len(c))

    if c1==1:
        (w,qd)=qn(a,b)
        return(w,qd)
    else:
        m=int(c[0])
        for i in range(0,m):
            x=tke(a,i,0)
            (w,v)=qn(x,b[i])
            w1=adi(w1,w,0,0)
            w2=adi(w2,v,0,0)
        for i in range(0,2):
            x=tke(w2,i,1)
            (w,v)=qn(x,8)
          
            e1=adi(e1,v,0,1)
            w1=adi(w1,w,1,1)
       
        return(w1,e1)

        
    
    
def qn(a,b):
    w=[]
    cmn=min(a)
    cmx=max(a)
    cd=cmx-cmn
    n=int(len(a))
    for i in range(0,n):
        x=((a[i]-cmn)/(cd))*((2**b)-1)
        y=round(x)
        w.append(y)
    qd=[cd,cmn]
    qd=np.array(qd)
    return(w,qd)
# a=quantized matrix or array
# qn=q.level in array or number
# b=(def.min) for array, (min.def) for matrix
def dquan(a,qn,b):
    
    a=np.array(a)
    w=[]
    c=a.shape
    c1=int(len(c))
    if c1==1:
        w=dqn(a,qn,b)
   
        return(w)
    else:
        b=np.array(b)
        y1=[]
        for i in range(0,2):
            x=tke(a,i,1)
            b1=tke(b,i,0)
            y=dqn(x,8,b1,0)
            
            y1=adi(y1,y,1,0)
        m=int(c[0])
        
        n=int(c[1])
        z2=[]
        for i in range(0,m):
            x=tke(a,i,0)
            y=x[2:n]
            y2=tke(y1,i,0)
            y4=swp(y2)
            
            z1=dqn(y,int(qn[i]),y2,1)
            z2=adi(z2,z1,0,0)
        return(z2)
            

def dqn(a,qd,b,lg):
    w=[]
    n=len(a)
    for i in range(0,n):
        if lg==0:
            x=((a[i]/((2**qd)-1))*b[0])+b[1]
        else:
            x=((a[i]/((2**qd)-1))*b[1])+b[0]
        w.append(x)
    w=np.array(w)
    return(w)
def swp(a):
    b=[1,1]
    a=np.array(a)
    b=np.array(b)
    b[0]=a[1]
    b[1]=a[0]
    return(b)
def plt(a,pk,c):
    if c==0:
        pkv=[]
        b=pt(a)
        for i in range(0,len(pk)):
            e=int(pk[i])
            e1=a[e]
            pkv.append(e1)
        return(b,pkv)
# c=0...8*1000
#c=1... 1000*8
def fnl(a,c):
      if c>0:
          a=np.transpose(a)
      s=a.shape
      e1=tke(a,0,0)
      e2=tke(a,1,0)
      ef=a[2:8]
      e3=np.subtract(e2,e1)
      er=-0.5*(np.add(e1,e2))
      el=-0.5*(np.subtract(e3,e1))
      efn=0.5*(np.add(e2,e3))
      ef=adi(ef,efn,0,1)
      ef=adi(ef,el,0,1)
      ef=adi(ef,er,0,1)
      ef=adi(ef,e3,0,1)
      ef=adi(ef,e2,0,1)
      ef=adi(ef,e1,0,1)
      if c>0:
          ef=np.transpose(ef)
      ef=rnd(ef,3)
      return(ef)
      
def lnr(a):
    
    s=a.shape
    s1=int(s[0])
    s2=int(s[1])
    s3=s1*s2
    k=0
    y=np.zeros(s3)
    for i in range(0,s1):
        for j in range(0,s2):
            y[k]=a[i,j]
           
            k=k+1
       
    return(y)

def alr(a,m):
    n=len(a)
    p=n/m
    p=int(p)
    
    y=[]
    for i in range(0,m):
        x=a[(i*p):((i*p)+p)]
        y=adi(y,x,0,0)
    return(y)
def con(a,b):
    a=np.array(a)
    b=np.array(b)
   
    c=a.shape
    cl=len(c)
    if cl==1:
        c2=int(c[0])
        if c2==0:
            return(b)
        else:
            d=np.concatenate((a,b))
            d=np.array(d)
            return(d)


def matlr(a,f,l):
    if f==0:
        a1=lnr(a)
        a1=1000*(a1)
        a2=rnd(a1,0)
        
        a3=abs(a2)
        am=max(a3)
        for i in range(0,15):
            if (2**i)>am:
                break
        if i<=11:
            c=[0,0]
            i=11
        elif i==12:
            c=[0,1]
        elif i==13:
            c=[1,0]
        elif i==14:
            c=[1,1]
        else:
            print('geche re hotovaga')
           
        bt=i
       
        c=np.array(c)
        k=1
        for i in range(0,int(len(a2))):
            if i==((k*2)-1):
                k=k+2
                if a2[i]==a3[i]:
                    j=0
                else:
                    j=1
                c1=rle.tobin(int(a3[i]),2,bt,0)
               
                c=np.concatenate((c,[j],c1))
            else:
                c1=rle.tobin(int(a3[i]),2,bt,0)
                c=np.concatenate((c,c1))
               
        return(c)
    
    else:
        fn=[]
        c=[a[0],a[1]]
        c1=rle.frbin(c,2,0)
        c1=int(c1+11)
        c2=(len(a)-2-(l/2))/c1
        a1=a[2:int(len(a))]
        for i in range(0,int((c2/2))):
            j=int((i+1)/2)
            k=int((c1*(i*2))+j)
            if (i%2)==0:
                x1=a1[k:(k+c1)]
                x2=a1[k+c1]
                x3=a1[(k+c1+1):(k+c1+(c1+1))]
                xq1=rle.frbin(x1,2,0)
                xq3=rle.frbin(x3,2,0)
                if x2==1:
                    xq3=-1*xq3
                r1=[xq1,xq3]
                fn=adi(fn,r1,0,0)
            else:
                x1=a1[k:(k+c1)]
                x3=a1[(k+c1):(k+c1+c1)]
                xq1=rle.frbin(x1,2,0)
                xq3=rle.frbin(x3,2,0)
                r1=[xq1,xq3]
                fn=adi(fn,r1,0,0)
        fn=fn/1000
        return(fn)
                
def bitgen(a):
    b=[]
    b=np.array(b)
    for h in range(0,len(a)):
            if a[h]==2:
                qc=[8,8]
            elif a[h]==3:
                qc=[6,8,8]
            elif a[h]==4:
                qc=[6,6,8,8]
            else:
                q1=[6,6,8,8]
                q1=np.array(q1)
                q2=4*(np.ones(int(a[h])-4))
                qc=np.concatenate(([q2,q1]))
            b=np.concatenate((b,qc))
    return(b)
def sum(a):
    a=np.array(a)
    xm1=0
    [s1,s2]=a.shape
    for i in range(0,int(s1)):
        x=tke(a,i,0)
        xm=np.sum(x)
        xm1=xm+xm1
    return(xm1)
def get(v):
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
    canvas1.pack()

    def getCSV ():
        global df
        
        import_file_path = filedialog.askopenfilename()
        df = pd.read_csv (import_file_path)
        print('file uploaded')
        print('close dialogue box')
        
    browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_CSV)

    root.mainloop()
    return(df)
def matarryfixbyte(lb,bt):
    c=[]
    [s1,s2]=lb.shape
    
    if s1>0:
        lb=lnr(lb)
    l=len(lb)
    l=int(l)
    for i in range(0,l):
        if lb[i]<0:
            sgn=[0]
        else:
            sgn=[1];
        c=np.concatenate((c,sgn))
        bl=round(lb[i]*1000)
        
        c3=rle.tobin(abs(bl),2,bt,0)
        c=np.concatenate((c,c3))
    return(c)

def bytematarryfix(c,totalbt,rw,bt):
    k=0
    lb1=[]
    for i in range(0,totalbt):
        c1=c[k:(k+(bt+1))]
        c2=c1[0]
        if c2==0:
            sgn=-1
        else:
            sgn=1
        c2=c1[1:(bt+1)]
        vf=rle.frbin(c2,2,0)
        vf=vf*sgn
        vf=vf/1000
        k=k+(bt+1)
        lb1.append(vf)
    lb1=np.array(lb1)
    if rw>1:
        lb1=alr(lb1,rw)
    return(lb1)
        
def paap(a1,Q,R,S,k11):
    

    tr1=random.rand(int(k11))
    tr2 = tqwt(tr1, Q,R,S)
        
    t3=[]
    for p in range(0,(S+1)):
        w1=tr2[(p):(p+1)]
        w2=w1[0]
        w2=np.array(w2)
        w3=w2.real
        
        if p!=S:
            w3=w3*0
            
            
        else:
            w3=w3*0
            w3=np.add(w3, 1)
            w3=(np.multiply(w3, a1)) 
        t3.append(w3)
    #print(t3)
    y=itqwt(t3,Q,R, k11)
    #print(len(y))
    return(y)
def mbpq(mb):
    print(mb)
    if mb==1:
        pq=10
    elif mb==5:
        pq=3
    elif mb==10:
        pq=3
    elif mb==15:
        pq=2
    return(pq)
        








    
    






