import numpy as np
import matplotlib.pyplot as plt
import korboi as ko
def find(ar2,pk):
    up=0
    val=100
    for i in range(0,len(pk)):
        k=0
        x=pk[i]
        for j in range((x-100),(x+100)):
            
            if j<0:
                j=0
            if j>len(ar2)-2:
                j=len(ar2)-2
            #print(j,len(ar2))
            if ar2[j+1]<=ar2[j] and ar2[j+1]<val:
                val=ar2[j+1]
                k=j+1
        val=100
        if (x-60)<0:
            x=60
        if (x+60)>=2938:
            x=2938
        v1=(ar2[x-60]+ar2[x+60])/2
        x1=abs(v1-ar2[x])
        x2=abs(v1-ar2[k])
        if (x2*0.6)>x1:
            pk[i]=k
            up=1
    return(pk,up)
def fndpk(ar3,sf,pt):
    c=[]
    e2=[]
    er5=[]
    c2=[]
    pkv=[]
    pw=[]
    ar1=[]
    pk=[]
    k1=0
    vl1=-100
    ar5=[]
    i1=[]
    dr6=[]
    c1=[]
    d=[]
    k=0
    
    sm=0
    sm1=0
    dr5=[]
    rn1=round((sf/250)*20)
    rn1=int(rn1)
    for i in range(0,(rn1-1)):
        pw.append(2)
    for i in range(0,len(ar3)):
        e=ar3[i]+rn1
        ar1.append(e)
    
    for i in range(0,len(ar3)):
        c2.append(i)
    
    ar4=np.diff(ar3)
    for i in range(0,len(ar4)):
        c.append(i)
        e=ar4[i]**2
        ar5.append(e)
    rn=round((sf/250)*7)
    ar5=np.sort(ar5)
    rn=int(rn)
    rt=1
    if rt>0:
        for i in range (0,(len(ar3)-rn1)):
            j=rn1+i
            dr1=ar3[i:j]
            dr2=np.diff(dr1)
            dr3=np.power(dr2,pw)
            dr4=np.sum(dr3)    
            dr5.append(dr4)
            c1.append(i)
      
        dr5=np.sort(dr5)
        for i in range(0,rn):
            sm=sm+dr5[len(dr5)-i-1]
        sm=sm/rn
        for i in range (0,(len(ar3)-rn1)):
            j=rn1+i
            er1=ar3[i:j]
            er2=np.diff(er1)
            er3=np.power(er2,pw)
            er4=np.sum(er3)
            er5.append(er4)
            e2.append(i)
            if er4>=(sm*0.4):
                for i1 in range(i,j):
                    if ar3[i1+1]>=ar3[i1] and ar3[i1+1]>=vl1:
                        vl1=ar3[i1+1]
                        k=i1
                if k1!=k:
                    k2=(k-k1)
                    if k2 > (sf/2):
                        k1=k
                        pk.append((k1+1))
            vl1=-100
            
    (f,up)=find(ar3,pk)
    if pt>0:
        for i in range(0,len(pk)):
            e=pk[i]
            e1=ar3[e]
            pkv.append(e1)
        plt.figure(pt)
        plt.subplot(211)
        plt.plot(c2,ar3,'-',pk,pkv,'+')
        plt.subplot(212)
        plt.plot(e2,er5)
        plt.show()
    cut=0
    s2=0
    cutval=0

    for i in range(0,len(f)):
        s1=0
        x=f[i]
        lx=ar3[int(x-60):int(x+60)]
        cut,s1=feat(lx)
        cutval=cutval+cut
        s2=s2+s1
        
    cutval=cutval/(len(f))
    s2=s2/(len(f))
    sa=np.diff(f)
    sa=np.average(sa)
    sa=round(sa)
        
    return(f,cutval,sa,s2,sm,up)

def cal(x,c):
    if c==0:
        k=0
        vl1=-100
        for i in range(0,len(x)-1):
            if x[i+1]>=x[i] and x[i+1]>=vl1:
                vl1=x[i+1]
                k=i+1
        return(k)
    else:
        vl1=100
        k=0
        for i in range(0,len(x)-1):
            if x[i+1]<x[i] and x[i+1]<vl1:
                vl1=x[i+1]
                k=i+1
        return(k)

def feat(lx):
    s1=0
    c=(lx[0]+lx[len(lx)-1])/2
    cut=abs(c-lx[60])
    lx=lx-c
    for j in range(0,len(lx)):
        s1=s1+lx[j]**2
    s1=s1/120
    return(cut,s1)

#len(ar3)-rn1
def rndpk(ar3,pkk,sf,cutval,cutdur,ene,slpene,up):
    rj=[0]
    pk=[-100]
    bu=0
    rj1=[0]
    u=0
    #ar3=ar3[int(pkk[0]-round(cutdur/2)):len(ar3)]
    b=np.ones(2)
    tg=[]
    b[0]=cutval
    b[1]=ene
    a=[]
    for i in range(0,3):
        a=ko.adi(a,b,0,0)
    b=cutdur*(np.ones(3))
    
    
    rn1=round((sf/250)*20)
    rn1=int(rn1)
    ep=2*np.ones(rn1)
    pw=2*np.ones(100)
    pw1=2*np.ones(200)
    e2=[]
   
    k=0
    k1=0
    h=0
    for i in range(0,(len(ar3)-100)):
        e=ar3[i:(i+rn1+1)]
        e=np.diff(e)
        e1=np.power(e,ep)
        es=np.sum(e1)
        if es>=(slpene*0.4) and abs((pk[-1]-i))>100:
            
            if k==0:
                k=i
            else:
               if (i-k)>round(sf*0.04):
                   k=i
            
            if k1!=k and k>100:
                
                k1=k
                e=ar3[(k1-50):(k1+51)]
                
                if u==0:
                    #print(len(e), len(pw),k)
                    u=1
                e=np.diff(e)
               
                e1=np.power(e,pw)
                
                t1=cal(e1,0)
                t1=k1-60+t1#####
                e=ar3[(t1-60):(t1+61)]
                t2=cal(e,up)
                
                t2=t1-60+t2
                #print(t2)
                #e=ar3[(t2-60):(t2+61)]
                #t3=find(e,[60])
                #t1=t2-60+t3[0]
                t1=t2
                
                    
               
                if h==0:
                    pk[0]=t1
                    
                    k1=t1
                    h=1
                else:
                    k3=pk[-1]
                    td=t1-k3
                    
                    if td>round(sf*0.17):###
                        #print(t1)
                        #print(i,t1,pk[-1],(i-pk[-1]))
                        #print(k3,td,t1,cutdur)
                        if (0.1*(cutdur))<td<0.7*(cutdur):
                            
                            lx=ar3[int(t1-60):int(t1+60)]
                            cut,s1=feat(lx)
                            
                                
                            (g,a,cutval,ene,p)=fetavg(cut,s1,a,cutval,ene,0)
                            if t1==90048: #######
                                print(t1,cut,s1,cutval,ene,p,'peye6i 1')
                            if g==1:
                                if (t1-pk[-1])>(sf*0.02):
                                    pk.append(t1)
                                if t1==11702:
                                    print(t1,pk[-1],'peye6i 1')
                                k1=t1
                                i=i+50
                            elif p[0]==-1 or p[1]==-1:
                                tg.append(t1)
                        if (0.7*cutdur)<=td<=1.4*(cutdur):
                            
                            lx=ar3[int(t1-60):int(t1+60)]
                            
                            cut,s1=feat(lx)
                            
                                
                            (g,a,cutval,ene,p)=fetavg(cut,s1,a,cutval,ene,1)
                            if t1==90048: ######
                                print(t1,cut,s1,cutval,ene,p,'peye6i 2')
                            if g==1:
                                if (t1-pk[-1])>(sf*0.02): 
                                    pk.append(t1)
                                if t1==11702:
                                    print('peye6i 2')
                                k1=t1
                                i=i+50
                                bb=pk[-1]-pk[-2]
                                #print(bb)
                                if (0.6*cutdur)<bb<(1.67*cutdur):
                                    b=np.concatenate(([bb],b))
                                    b=b[0:3]
                                    bs=np.average(b)
                                    cutdur=round(bs)
                            elif p[0]==-1 or p[1]==-1:
                                tg.append(t1)
                            else:
                                if p[0]==1:
                                    rj.append(t1)
                        if td>1.4*(cutdur):
                            
                            rd1=(td/cutdur)
                            if t1==17380:
                                print('eikhane')
                            rd=round(rd1)
                            if 1.4<=rd1<1.5:
                                rd=2
                           # if rd<rd1:
                                #rd=rd+1
                            
                            for f in range(0,(int(rd)-1)):
                                #d1=t1-((int(rd)-1+f)*cutdur)
                                d1=pk[-1]+((f+1)*cutdur)
                         
                                #print(i,pk[-1],d1,t1,cutdur,rd)
                                
                                d2=ar3[int(d1-100):int(d1+101)]
                                d2d=np.diff(d2)###
                                d2p=np.power(d2d,pw1)
                                d3=cal(d2p,0)
                                d3=d1-100+d3
                                d2=ar3[int(d3-60):int(d3+61)]
                                d3=int(d3)
                                
                                d4=cal(d2,up)
                                d3=d3-60+d4
                                lx=ar3[int(d3-60):int(d3+60)]
                                
                                cut,s1=feat(lx)
                                (g,a,cutval,ene,p)=fetavg(cut,s1,a,cutval,ene,0)
                                if g==1:
                                    if (d3-pk[-1])>(sf*0.02):
                                        pk.append(d3)
                                    if d3==11702:
                                        print('peye6i 3')
                                    bu=1
                                    k1=d3
                                    b[0]=pk[-1]-pk[-2]
                                    cutdur=np.average(b)
                                    cutdur=round(cutdur)
                                else:
                                    gf1=d3-rj[-1]
                                    
                                    gf1=abs(gf1)
                                    if gf1<(cutdur*0.3):
                                        rj1.append(d3)
                                        pk.append(rj[-1])
                                        bu=1
                                if bu==0:
                                    if k3<rj[-1]<t1:
                                        #print('#####paini',k3,rd,rj[-1])
                                        if pk[-1]!=rj[-1]:
                                            pk.append(rj[-1])
                                bu=0
                              
                            lx=ar3[int(t1-60):int(t1+60)]
                            cut,s1=feat(lx)
                            
                            (g,a,cutval,ene,p)=fetavg(cut,s1,a,cutval,ene,1)
                            if t1==9515:
                                print(t1,cut,s1,cutval,ene,p)
                            
                            if g==1:
                                if (t1-pk[-1])>(sf*0.02):
                                    pk.append(t1)
                                if t1==11702:
                                        print('peye6i 4')
                                k1=t1
                                i=i+50
                            elif p[0]==-1 or p[1]==-1:
                                tg.append(t1)
                            else:
                                if p[0]==1:
                                    rj.append(t1)
                            #print('chudeche')
                            #break
                    
                            
    plt.plot(i,ar3[i])
    
    return(pk,rj,rj1,tg)

def fetavg(cut,s1,a,cutval,ene,c):
    p=[0,0]
    k=0
    
    p=np.array(p)
    if c==0:
        if 0.45<=(cut/cutval)<=1.9:
            p[0]=1
    else:
        if 0.5<=(cut/cutval)<=3:
            p[0]=1
    if c==0:
        if 0.5<=(s1/ene)<=1.8:
            p[1]=1
    else:
        if 0.60<=(s1/ene)<=1.6:
            p[1]=1
    if 0.2<(cut/cutval)<.45 or 3<(cut/cutval)<5:
        p[0]=-1
    if 0.2<(s1/ene)<.5 or 1.8<(s1/ene)<5:
        p[1]=-1
            
    if c==0:
        
        if p[0]==1 or p[1]==1:
            #a1=[cut,s1]
            #a2=ko.adi(a,a1,0,1)
            #a=a2[0:3]
            #cutval=(a[1,0]+a[2,0]+a[0,0])/3
            #ene=(a[1,1]+a[2,1]+a[0,1])/3
            k=1
            return(k,a,cutval,ene,p)
        else:
            return(k,a,cutval,ene,p)
    
    if c==1:
        
        if p[0]==1 and p[0]==1:
            a1=[cut,s1]
            a2=ko.adi(a,a1,0,1)
            a=a2[0:3]
            cutval=(a[1,0]+a[2,0]+a[0,0])/3
            ene=(a[1,1]+a[2,1]+a[0,1])/3
            k=1
            return(k,a,cutval,ene,p)
        else:
            return(k,a,cutval,ene,p)


