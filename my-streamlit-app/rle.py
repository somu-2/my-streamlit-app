# Function name 'fun_rle'
# this is a function to run length encoding
# to convert nrm to rle
#
# r=0
# re2=double derivatived nrm file
# fe= IV..in count file e.g. 15
# rtn= [(IV..in cmprsed.file) (length of count.file) (cmprsed.file) (count.file) ]
#

#
# for conversion 12-->[0 1 1 0 0]/[1100]
# Function name 'tobin'-(12,(base-2),(element-5),(0/1))
#
# for conversion: A=[0 1 1 0 0]/[1100]-->12
# Function name 'frbin'-(A,(base-2),(0/1))
#


import numpy as nm
import math
def rle(r,re2,fe):
        val=0
        w1=[]
        w2=[]
        for i in range(0,len(re2)):
            x=abs(re2[i])
            if x>=val:
                val=x
        for i in range(0,8):
            if (2**i)> ((val*2)+1):
                break
        c=0
        f1=i
        
        f=(2**i)-1
        f2=round(f//2)+1
        for i in range(0,len(re2)):
            if re2[i]==0:
                c=c+1
            else:
                    if c==1:
                        w1=w1+[0]
                    elif c==2:
                        w1=w1+[0,0]
                    elif c>2:
                        x=(c//fe)+1
                        y=c%fe
                        if y==0:
                            x=x-1
                        for j in range(0,x):
                            w1.append(f2)
                            if j!=(x-1):
                                w2.append(fe)
                            else:
                                w2.append(y)
                    c=0
                    w1.append(re2[i])
        w=[len(w2)]
        w1=nm.array(w1)
        w1=w1+f2-1
     
        return (f2,w,w1,w2)
#
# to convert rle to nrm
#
# r=1
# fe=IV..in count file e.g. 15
# f2=IV..in cmprsed file e.g. 15
# w1=comprsed file
# w2=count file
def rle1(r,f2,fe,we1,we2):
        we1=we1-f2+1
        k=0
        er1=[]
        for i in range(0,len(we1)):
            if we1[i]==f2:
               
               if we2[k]==0:
                   we2[k]=fe
               for j in range(0,int(we2[k])):
                   er1.append(0)
               k=k+1
            else:
                er1.append(we1[i])      
        return(er1)

def tobin(a,bt,lt,c):
        b=[]
        sm=0
        for i in range(0,lt):
            x=a/bt
            y=a%bt
            
            a=x
            sm=sm+y*(10**i)
            y1=math.floor(y)
            b=nm.concatenate(([y1],b))
        if c==0:
                return(b)
        else:
                return(sm)

def frbin(b,bt,c):
        sm1=0
        sm2=0
        
        if c==0:
                t=len(b)
                for i in range(0,t):
                    x=b[i]*(bt**(t-i-1))
                    sm1=sm1+x
                return(sm1)
        else:
                for i in range(0,100):
                    for j in range(0,i):
                        x=10**(j)
                        sm2=sm2+x
                    if sm2>=b:
                        sm2=0
                        break
                    else:
                        sm2=0
                e=[]
                for j in range(0,i):
                    x=b/(10**((i-j-1)))
                    y=b%(10**((i-j-1)))
                    if j!=(i-1):
                        e=nm.concatenate((e,[x]))
                        b=y
                    else:
                        e=nm.concatenate((e,[x]))
                e1=frbin(e,bt,0)
                return(e1)

def decom():
        fn=antipca(v1,str2,mn)
        

def stb(a,bt,lt,c):
        if a!=abs(a):
                s=1
        else:
                s=0
        a=abs(a)
        b=tobin(a,bt,lt,c)
        b=nm.concatenate(([s],b))
        return(b)
def sfb(b,bt,c):
        l=len(b)
        s=b[0]
        b1=b[1:l]
        a=frbin(b1,bt,c)
        if s==1:
                a=-1*a
        return(a)
        
def decum(a,b,c):
        d=[]
        if c==0:
                d.append(a[0])
                d1=nm.diff(a)
                d.append(d1[0])
                d2=nm.diff(d1)
                d=nm.array(d)
                return(d2,d)
        else:
                b=nm.array(b)
                d=b[1]
               
                a=nm.concatenate(([d],a))
                d1=nm.cumsum(a)
                d=b[0]
                d2=nm.concatenate(([d],d1))
                d3=nm.cumsum(d2)
                return(d3)

def rl(r,re2,fe):
        s2=[]
        s2=nm.array(s2)
        val=0
        w1=[]
        w2=[]
        for i in range(0,len(re2)):
            x=abs(re2[i])
            if x>=val:
                val=x
        for i in range(0,20):
            if (2**i)> ((val*2)+1):
                break
        c=0
        
        lb=[]
       
        p=0
        t=nm.zeros(i-1)
        for j in range(0,len(re2)):
                x=abs(re2[j])
                for f in range(0,(i-1)):
                        
                        if ((2*x)+1)>=(2**(f+1)):
                                t[f]=t[f]+1
                                if f==(i-3):
                                        lb.append(j)
                        
        #print('i 1st', i)
        f3=i
        gg=0
        if gg>0:
                if t[i-3]<5:
                        
                        for r2 in range(0,len(lb)):
                                r3=lb[r2]
                                r1=((2**(i-1))-2)//2
                                if re2[r3]>0:
                                        re2[r3]=r1
                                else:
                                        re2[r3]=-1*r1
                        i=i-1
        #print(t)
        for j in range((len(t)-1),-1,-1):
                if t[j]>100:
                        j=j+1
                        #print('i kom6e',i)
                        i=j+1
                        break
        #print('j', j)
        #print('i 2nt', i)
        re2=nm.concatenate((re2,[1]))
        #print('i 3rt', i)
        f=(2**i)-1
        f2=round(f//2)+1
        f1=i
        #print(i, f, f2)
        for i in range(0,len(re2)):
            if re2[i]==0:
                c=c+1
            else:
                    if c==1:
                        w1=w1+[0]

                    elif c==2:
                        w1=w1+[0,0]
                    elif c>2:
                        #print('ggggg', c, fe)
                        x=(c//fe)+1
                        y=c%fe
                        
                        if y==0:
                            x=x-1
                        for j in range(0,x):
                            w1.append(f2)
                            if j!=(x-1):
                                w2.append(fe)
                            else:
                                if y==0:
                                        y=fe
                                w2.append(y)
                    c=0
                    if abs(re2[i])>=(f2):
                        w1.append(f2)
                        w2.append(0)
                        s2=nm.concatenate((s2,[re2[i]]))
                    else:
                        w1.append(re2[i])
        w=len(w2)   
        w1=nm.array(w1)
        w1=w1+f2-1
     
        return (f2,w,w1,w2,s2,f1,f3)


def rl1(r,f2,fe,we1,we2,s2):
        p=0
        we1=we1-f2+1
        k=0
        er1=[]
        for i in range(0,len(we1)):
            if we1[i]==f2:
               
               if we2[k]!=0:
                       for j in range(0,int(we2[k])):
                           er1.append(0)
               else:
                       er1.append(s2[p])
                       p=p+1
               k=k+1
            else:
                er1.append(we1[i])
        g=len(er1)
        er2=er1[0:(g-1)]
        er2=nm.array(er2)
        return(er2)
                

















        
        


