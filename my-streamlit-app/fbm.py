import numpy as np
import korboi as ko
import rle
from numpy import savetxt
from numpy import genfromtxt
import csv
import matplotlib.pyplot as plt

def gen(c):
    k=0
    fn1=[]
    c1=len(c)
    for ren in range(0,1000):
        
        c2=c[int(k):(c1)]
        fn,k1=agen(c2,0)
        print('kkkkkkkkkkk', ren, c1,k,k1,(k+k1), fn.shape)
        k=k+k1
        fn1=ko.adi(fn1,fn,0,0)
        if k==c1:
            return(fn1)
        
        
        


def agen(c,k):
    
    for ren in range(0,1):
        print('##############')
        print('##############')
        print('##############')
        print('##############')
        
        x=c[k:(k+2)]
        mb=(rle.frbin(x,2,0))+1
        mb=mb*5
        mb=int(mb)

        k=k+2
        k1=k+11
        c1=c[k:k1]
        k=k1
        lth=rle.frbin(c1,2,0)
        lth=lth+400     ## lenth of beat
        tsm=[]
        if mb<2:
            k1=k+12
            c1=c[k:k1]
            for i in range(0,6):
                x=c1[(i*2):((i+1)*2)]
                x1=rle.frbin(x,2,0)
                tsm.append(x1)
        else:
            k1=k+18
            c1=c[k:k1]
            for i in range(0,6):
                x=c1[(i*3):((i+1)*3)]
                x1=rle.frbin(x,2,0)
                x1=x1+2
               
                tsm.append(x1)  

        # 1. provie mb=5,101,15


        # 2. provide pd
        pdl=[]
        pd=[]
        k=31
        x=c[k:(k+2)]
        pw=(rle.frbin(x,2,0))+5
        pw=int(pw)
        k=(k+2)
        k1=(mb-1)+(mb+1)*pw
        c1=c[int(k):int((k1+k))]
        k=int(k+k1+1)
        for i in range(0,(mb-1)):
            x=c1[(i*(pw+1)):((i*(pw+1))+(pw))]
            x1=rle.frbin(x,2,0)
            x2=c1[((i*(pw+1))+pw)]
            pdl.append(x1)
            pdl.append(x2)
        i=i+1
        x=c1[(i*(pw+1)):((i*(pw+1))+pw)]
        x1=rle.frbin(x,2,0)
        pdl.append(x1)
        x=c1[(((i+1)*(pw+1))-1):(((i+1)*(pw+1))+(pw-1))]
        x1=rle.frbin(x,2,0)
        pdl.append(x1)
        for i in range(0,((mb*2)-1)):
            if (i%2)==1:
                pdl[i]=pdl[i]+pdl[(i+1)]
        for i in range(0,mb):
            er=pdl[(i*2):((i*2)+2)]
            pd=ko.adi(pd,er,1,0)
        pd=np.transpose(pd)

        #  3. provide prefixes, V-1, v-6,str-6
        k=k-1
        c1=c[(k):(k+2)]
        c2=(rle.frbin(c1,2,0))+11
        k1=int(k+(c2*4)+3)
        x=c[k:k1]
        lb=ko.matlr(x,1,2)   ## V1=lb
        k=k1
        c1=c[(k):(k+2)]
        c2=(rle.frbin(c1,2,0))+11
        k1=int(k+(c2*24)+8)
        x=c[k:k1]
        vcp=ko.matlr(x,1,12)  ## v-6 = vcp
        k=k1
        c1=c[(k):(k+2)]
        c2=(rle.frbin(c1,2,0))+11
        k1=int(k+(c2*24)+8)
        x=c[k:k1]
        ff2=ko.matlr(x,1,12)   ## str-6 = ff2
        k=k1

        # 4. to provide first elemet of all vectors
        vcf=[]
        c1=c[k:(k+13)]
        v1=(rle.sfb(c1,2,0))/1000  ## v1
        k=k+13
        p=c[k]
        k=k+1
        if p==0:
            c1=c[k:(k+13)]
            v2=(rle.sfb(c1,2,0))/1000
            vcf.append(v2)
            k=k+13
            for i in range(0,5):
                if c[k+i]==0:
                    vcf.append(v2)
                else:
                    vcf.append((-1*v2))
        else:
            for i in range(0,6):
                c1=c[(k+(i*13)):(k+((i+1)*13))]
                v3=(rle.sfb(c1,2,0))/1000
                vcf.append(v3)    ## vcf

        # 5. to provide  all vectors
        y1=[]
        k=k+i+1
        k1=k+560
        c1=c[k:k1]
        for i in range(0,70):
            x=c1[(i*8):((i+1)*8)]
            
            x1=rle.frbin(x,2,0)
            y1.append(x1)
        vm=ko.alr(y1,7)     ## main vector
        k=k1
        g=((mb-1)*6*(mb+2))
        k1=k+(g*8)
        c1=c[k:k1]
        y1=[]
        for i in range(0,g):
            x=c1[(i*8):((i+1)*8)]
            x1=rle.frbin(x,2,0)
            y1.append(x1)
        va=ko.alr(y1,((mb-1)*6))         ## other vectors
        ## to regenrate all vectors
        vv1=[]
        gh=np.ones(8)
        gh1=np.ones(mb)
        r=ko.dquan(vm,(8*gh),lb)
        v=ko.adi(r,(v1*gh),0,1)
        v=np.transpose(v)    ## eigent vector of main V
        for i in range(0,6):
            r1=va[(i*(mb-1)):((i+1)*(mb-1))]
            r2=vcp[(i*2):((i+1)*2)]
            r3=ko.dquan(r1,(8*gh1),r2)
            r4=ko.adi(r3,(vcf[i]*gh1),0,1)
            r4=np.transpose(r4)
            vv1=ko.adi(vv1,r4,0,0)             ## VV1 is generated
            
        ## to genrate all str
        ## tsm=number of rows in each 6 beat matrix
        k=k1
        si=[]
        tm=np.sum(tsm)
        k=int(k1)
        k1=int(k1+(tm*2*8))
        c1=c[k:k1]
        for i in range(0,int(tm*2)):
            x=c1[(i*8):((i+1)*8)]
            x1=rle.frbin(x,2,0)
            si.append(x1)
        s1=ko.alr(si,int(tm))   ## initals of str
        tsv=ko.bitgen(tsm)


        u=0
        w2=[]
        s2=[]
        w1=[]
        ts9=[]
        for i in range(0,int(tm)):
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
            k1=k+8
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
            f2=round(f/2)+1
            #print(i, len(w1), w, len(s2))
            #print(f1,f2,f3)
            #print('##############')
            mm=rle.rl1(1,f2,7,w1,(w2),s2)
            y=rle.decum(mm,x3,1)
            y=np.concatenate(([s1[i,0]],[s1[i,1]],y))
            #print(k1, len(y))
            ts9=ko.adi(ts9,y,0,0)
            w1=[]
            w2=[]
            s2=[]
            u=u+1
            gh=k1
            x3=[]

        g1=(lth-2)*mb
        g2=ko.sum(pd)
        g1=g1-g2
        g3=(g1*12*16)/len(c)
        print('compression ration is', g3)
            
        tsm=np.concatenate(([0],tsm))
        k=tsm[0]
        k1=tsm[1]
        fn2=[]
        fn4=[]
        for i in range(0,6):
            v2=vv1[(i*mb):((i+1)*mb)]
            
            ts=ts9[int(k):int(k1)]
            qn=tsv[int(k):int(k1)]
            if i<5:
                k=k+tsm[i+1]
                k1=k1+tsm[i+2]
            qb=ff2[(i*2):(i+1)*2]
            ts1=ko.dquan(ts,qn,qb)

            t=int(tsm[i+1])
            mn=ko.tke(ts1,(t-1),0)
            str2=ts1[0:(t-1)]
            fn=ko.antipca(v2,str2,mn)
            fn1=ko.bt_ld(fn,pd)
            fn2=ko.adi(fn2,fn1,0,0)
        mn2=ko.tke(fn2,5,0)
        st1=fn2[0:5]
        fn4=ko.antipca(v,st1,mn2)
        fn4=np.transpose(fn4)
        return(fn4,gh)
    
 
    


    
    
    
    


