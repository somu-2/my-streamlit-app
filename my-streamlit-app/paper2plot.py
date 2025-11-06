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

ar=genfromtxt('104s0306lre.csv', delimiter=',')
ar1=ar[544:1200]
savetxt('ar1.csv', ar1, delimiter=',')
ar1=np.transpose(ar1)
(v,str1,mn,sw)=ko.pca(ar1,0,0,0)
savetxt('str1.csv', str1, delimiter=',')
p1=ko.tke(str1,0,0)
plt.figure(1)
plt.plot(ar1)
##plt.show()
t3=[]
tr2 = tqwt(p1, 6.7,2,15)
tr3=tr2.real

for p in range(0,(16)):
    w1=tr2[(p):(p+1)]
    w2=w1[0]
    w2=np.array(w2)
    
    w3=w2.real
    if p==0:
        savetxt('h1.csv', w3, delimiter=',')
    if p==14:
        savetxt('h14.csv', w3, delimiter=',')
    if p==15:
        savetxt('h15.csv', w3, delimiter=',')
    t3.append(w3)
    plt.figure(p)
    plt.plot(w2)












    

