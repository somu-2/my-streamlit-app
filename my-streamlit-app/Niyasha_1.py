import numpy as np
from numpy import savetxt
from numpy import genfromtxt
import csv
import korboi as ko
import matplotlib.pyplot as plt
import sys
import time
from numpy import random




a1=[]
# Taking MECG data at 'aa' of 12 lead, 1 beat length
#aa=ko.get(0)
# main file has 15 leads, from which 12 leads are taken in ad1
# then a beat length is taken of 617 sample in aa
aa=genfromtxt('5s0021are.csv', delimiter=',')
ad=np.transpose(aa)
ad1=ad[0:12]
aa=np.transpose(ad1)
aa=aa[160:(160+1058-446)]

###########################################





# taking 8 independent leads and transposing for PCA decomposition
for i in range(0,8):
    xe=[0,1,6,7,8,9,10,11]
    a=ko.tke(aa,xe[i],1)
    a1=ko.adi(a1,a,1,0)
a1=np.transpose(a1)  # BEAT before PCA at 'a1'
###########################################





# PCA decomposition using function ko.pca
# first input is a1(8*617)
# second input is either 0: for taking dominanat PCs with Energy 90%.
# second input is 2: All PCs will be visible
# output: v: Eigent vectors 8*8
# output: str1(8*617)/str2(5*617): PC matrix with decreasing order of varience/energy
# mn(1*617): mean matrix of a1
(v,str1,mn,sw)=ko.pca(a1,0,0,0)
(v,str2,mn,sw)=ko.pca(a1,2,0,0)
str1=np.transpose(str1)
str2=np.transpose(str2)
###############################################








# Adding bias for clear visualization in plot
m3=0
m4=np.zeros(8)

for i in range(0,8):
    s1=ko.tke(str2,i,1)
    s1.shape
    m1=min(s1);
    m2=max(s1)
    m3=m2-m1+m3+0.3
    m4[i]=m3

s2=[]

for i in range(0,8):
    s1=ko.tke(str2,i,1)
    s1=s1+m4[i]
    s2=ko.adi(s2,s1,1,0)
m3=0
m4=np.zeros(8)

for i in range(0,5):
    s1=ko.tke(str1,i,1)
    s1.shape
    m1=min(s1);
    m2=max(s1)
    m3=m2-m1+m3+0.3
    m4[i]=m3
ss2=[]
for i in range(0,5):
    s1=ko.tke(str1,i,1)
    s1=s1+m4[i]
    ss2=ko.adi(ss2,s1,1,0)
#####################################################




    
# to find antiPCA using str1, which is reduced PC matrix, using other PCs as zero-arrays
# fn1 is the reconstructed 8*617 leads
str1=np.transpose(str1)
(fn1)=ko.antipca(v,str1,mn)
fn1=np.transpose(fn1)
###############################






aa=np.transpose(aa)

# Recalculating the 12 leads from 8 leads in d1(12*617)
## computing PRD, PRDN, MAE, MSE, SNP, PSNR usng 12 leads between aa(original), d1(reconstructed) beat-matrix
# bg is error matrix
d1=ko.fnl(a1,0)   
bg=ko.err(d1,aa,1,0)
###############################


aa=np.transpose(aa)
a1=np.transpose(a1)
d1=np.transpose(d1)




##   pltting everything
plt.figure(1)
plt.subplot(211)
plt.plot(a1)
plt.title("Original_8 Indepoendent Leads")
plt.subplot(212)
plt.plot(fn1)
plt.title("Reconstructed_8 Indepoendent Leads using 5 Dominant PCs")




plt.figure(2)
plt.subplot(211)
plt.plot(s2)
plt.title("8 PCs")
plt.subplot(212)
plt.plot(ss2)
plt.title("Dominant 5 PCs")

plt.figure(3)
plt.title("Original & Reconstructed 12 Leads")
for i in range(0,12):
    q1=ko.tke(aa,i,1)+0.3
    q2=ko.tke(d1,i,1)
    plt.subplot(3,4,(i+1))
    plt.plot(q1)
    plt.plot(q2)
    




plt.show()


       













