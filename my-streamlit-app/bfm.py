import numpy as np
import korboi as ko
import rle
from numpy import savetxt
from numpy import genfromtxt
import matplotlib.pyplot as plt
import csv

#v=genfromtxt('v.csv', delimiter=',')
#ts9=genfromtxt('ts9.csv', delimiter=',')
#tsm=genfromtxt('tsm.csv', delimiter=',')
#vv1=genfromtxt('vv1.csv', delimiter=',')
#ff2=genfromtxt('ff2.csv', delimiter=',')
#pd=genfromtxt('pd.csv', delimiter=',')

def gen(v,tsm,vv1,ff2,pd,mb,ts9):
    # to generate mb and pd
    c=[]
    c=np.array(c)

    m=(mb/5)-1
    c=rle.tobin(m,2,2,0)

    [e1,e2]=ts9.shape
    e1=int(e1)
    e2=int(e2)
    e2=e2-400
    x1=rle.tobin(e2,2,11,0)   ##
    c=np.concatenate((c,x1))
    for i in range(0, len(tsm)):
        x=int(tsm[i]-2)
        print(x)
        if mb<2:
            x1=rle.tobin(x,2,2,0)
            c=np.concatenate((c,x1))
        else:
            x1=rle.tobin(x,2,3,0)
            c=np.concatenate((c,x1))  ##
        print(x1)



    pdl=ko.lnr(pd)
    for i in range(0,(mb-1)):
        r=((i*2)+1)
        pdl[r]=pdl[r]-pdl[r+1]
    pdm=max(pdl)
    for i in range(0,10):
        if (2**i)>pdm:
            break
    tb=i
    c1=rle.tobin((i-5),2,2,0)
    c=np.concatenate((c,c1))
    for i in range(0,(len(pdl)-2)):
        if (i%2)==0:
            c1=rle.tobin(int(pdl[i]),2,tb,0)
            c=np.concatenate((c,c1,[pdl[i+1]]))
    c1=rle.tobin(int(pdl[((mb*2)-2)]),2,tb,0)
    c2=rle.tobin(int(pdl[((mb*2)-1)]),2,tb,0)
    c=np.concatenate((c,c1,c2))
    #_---------________--------_______-------_______-----mb,pd



    c3=[]
    c3=np.array(c3)
    c1=[]
    v=np.transpose(v)
    v1=v[0,0]  ###
    v2=v[1:8]
    vb=[8,8,8,8,8,8,8,8]
    (vq,lb)=ko.quan(v2,vb) ### lb
    vl=ko.lnr(vq)
    for i in range(0,len(vl)):
        c1=rle.tobin(int(vl[i]),2,8,0)
        
        c3=np.concatenate((c3,c1))
      
    ##  to optimze all vector matrices vv1

    vcm=[]
    vcp=[]
    vcf=[]
    s=vv1.shape
    s1=int(s[0])
    for i in range(0,6):
        g1=vv1[(i*mb):((i*mb)+mb)]
        g2=np.transpose(g1)
        g3=g2[0,0]  
        g4=g2[1:mb]
        gb=8*(np.ones(mb))
        (gq,gp)=ko.quan(g4,gb)
       
        vcm=ko.adi(vcm, gq,0,0) ### vcm
        vcf.append(g3)          ### vcf
        vcp=ko.adi(vcp,gp,0,0) ### vcb
    vcf=np.array(vcf)

    ##  2..to store prefixes of V-1(lb),v-6(vcp),str-6(ff2)
    y=ko.matlr(lb,0,0)
    y1=ko.matlr(vcp,0,0)
    y2=ko.matlr(ff2,0,0)
    c=np.concatenate((c,y,y1,y2))
    ##  2... end of store



    ## 3. to store first elemet of all vectors v1,vcf

    v1=1000*v1
    v1=round(v1,0)
    vb1=rle.stb(int(v1),2,12,0)
    x=1000*vcf
    x=ko.rnd(x,0)
    x1=abs(x)
    x2=np.diff(x1)
    if min(x2)==0 and max(x2)==0:
        p=0
        y1=rle.stb(int(x[0]),2,12,0)
        e=[]
        for i in range(0,(len(x)-1)):
            if x[i+1]==x[0]:
                e.append(0)
            else:
                e.append(1)
        e=np.array(e)
        c=np.concatenate((c,vb1,[p],y1,e))
    else:
        p=1
        c=np.concatenate((c,vb1,[p]))
        for i in range(0,len(x)):
            y1=rle.stb(int(x[i]),2,12,0)
            c=np.concatenate((c,y1))
    ##  3... end of store


    c=np.concatenate((c,c3))
    for i in range(0,((mb-1)*6)):
        for j in range(0,(mb+2)):
            x=vcm[i,j]
            x1=rle.tobin(int(x),2,8,0)
            c=np.concatenate((c,x1))






                 
    ## 4. to store str
    ##############

    for i in range(0,e1):
        for j in range(0,2):
            x=ts9[i,j]
            x1=rle.tobin(int(x),2,8,0)
            c=np.concatenate((c,x1))   
    tsv=ko.bitgen(tsm)
    tm=sum(tsm)
    #print('vbsachbnfrtv', len(c))
    f=0
    c2=[]
    e2=e2+400
    nb1=0
    nb2=0
    for i in range(0,1):
        for j in range(0,int(tm)):
            x=ko.tke(ts9,j,0)
            x1=x[2:(e2)]
            (x2,x3)=rle.decum(x1,0,0)
            c1=rle.tobin(int(x3[0]),2,int(tsv[f]),0)
            c11=rle.stb(int(x3[1]),2,int(tsv[f]),0)
            f=f+1
            c2=np.concatenate((c2,c1,c11))
            f2,w,w1,w2,s2,f1,f3=rle.rl(0,x2,7)
            c1=rle.tobin(f3,2,4,0)
            c11=rle.tobin((f3-f1),2,3,0)
            c12=rle.tobin((w-0),2,8,0)
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
            
            
                
                
                             

            
            


            print(j, len(w1), w, len(s2))
            f21,ww,ww1,ww2=rle.rle(0,x2,7)
            mm=rle.rl1(1,f2,7,w1,(w2),s2)
            
            rt=(np.subtract(mm,x2))
            rt=abs(rt)
            bn1=(f1*len(w1)+3*len(w2)+f3*len(s2))
            bn2=len(ww1)*f3+3*len(ww2)
            nb1=nb1+bn1
            nb2=nb2+bn2
            c=np.concatenate((c,c2))
            print('dek re', len(c2))
            c2=[]
            c2=np.array(c2)
            
                

    return(c)






    

