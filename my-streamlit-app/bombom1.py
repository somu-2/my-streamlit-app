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
import pkdt



import compressfunc as comfnc
import decompressfunc as decomfnc


tsv=[4,4,6,6,8,8]
sf=1000




#######    1st function :    peakdt(sf,pq,crt,pts)
# sf= sampling frequency
# pq= 0: it will automatically take 104.csv_12 lead.......  1: panda will run
# crt= 0: NOP...   1: program will run
# pts: 1: plot will show.....    0: no plt
# return:   data and R-peak

pq=1
crt=0
pts=0
(data,pk)=pkdt.peakdt(sf,pq,crt,pts)
print('    peak detection end    ')
print('   ')
print('   ')
print('   ')
print('   ')





#######     dcom(tsv,crt,sf,mb,pq,momo):
# crt= always 1
# mb= 1,5,10,15 asyou wish
# momo= 0: No excess compresseion
# pq= number ofbeat compressed, if 0: system generated..    >0: pq number of beat matrix will be compressed
mb=5
pq=2
(ss1,q1,q2,q3,q4)=comfnc.dcom(tsv,1,sf,mb,pq,1)

print('****----    Data compression done----    ******')
print('   ')
print('   ')
print('   ')
print('   ')



########   decomdata(tsv,mm)
# mm: 1: plot will show.....    0: no plt
mm=0
(cr,er)=decomfnc.decomdata(tsv,mm)
ff=er[12,1]
ff1=er[12,0]
q21=q2*ff/ff1
ff=np.concatenate(([q1],[q3],[q4],[cr],[q2],[q21], [ff1], [ff]))
ff=np.round(ff,2)
ff1=list(ff)
#qall=[q1,q3,q4,cr,q2,er[12,0],er[12,1]]
#qall=np.arrray(qall)
#qall=round(qall,2)
print('   ')
print('   ')
print('   ')
print('   ')
print(ff1)
print('   ')
print('   ')
print('   ')
print('   ')
print('****----    Data re-construction done----    ******')

if mm==0:
    plt.show()
















