import korboi as ko
import rle
import numpy as np


def tsvadd(tsv,c):
    if c==0:
       
        y1=rle.tobin((tsv[0]-3), 2, 2, 0)
        cx=y1
        y1=rle.tobin((tsv[1]-3), 2, 2, 0)
        cx=np.concatenate((cx,y1))
        y1=rle.tobin((tsv[2]-4), 2, 2, 0)
        cx=np.concatenate((cx,y1))
        y1=rle.tobin((tsv[3]-4), 2, 2, 0)
        cx=np.concatenate((cx,y1))
        y1=rle.tobin((tsv[4]-5), 2, 2, 0)
        cx=np.concatenate((cx,y1))
        y1=rle.tobin((tsv[5]-5), 2, 2, 0)
        cx=np.concatenate((cx,y1))
        
    
    else:
        ss1=tsv
        j1=int(rle.frbin(ss1[0:2],2,0))+3
        j2=int(rle.frbin(ss1[2:4],2,0))+3
        j3=int(rle.frbin(ss1[4:6],2,0))+4
        j4=int(rle.frbin(ss1[6:8],2,0))+4
        j5=int(rle.frbin(ss1[8:10],2,0))+5
        j6=int(rle.frbin(ss1[10:12],2,0))+5
        #print(j1,j2,j3,j4,j5,j6)
        tsv=[]
        cx=[j1,j2,j3,j4,j5,j6]
        
        
     



    return(cx)
