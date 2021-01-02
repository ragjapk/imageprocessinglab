# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:28:43 2018

@author: IIST
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
A=[[0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0],
   [0, 1, 1, 1, 0],
   [0, 0, 1, 1, 0],
   [0, 0, 0, 1, 0],
   [0, 0, 0, 0, 0]]  

A_org=np.asarray(A)
A=np.flipud(A_org)

B1=[[0, 0, 0],
    [0, 0, 0],
    [1, 1, 0]]
#B1=[0, 0, 0,0, 0, 0,1, 1, 0]

B2=[[0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]]
B1=np.asarray(B1)
B2=np.asarray(B2)

B=np.flipud(B1)
index=np.where(B)
l1=np.ndarray.tolist(index[0])
l2=np.ndarray.tolist(index[1])
print(l1,l2)
A_new=np.zeros((A.shape))
for k in range(len(l1)):
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):   
            x=l1[k]
            y=l2[k]
            if(i+x<A.shape[0] and j+y<A.shape[1]):
                if(A[i,j]==1):
                    A_new[i+x,j+y]=1
A_new=np.flipud(A_new)                    
plt.imshow(A_org,cmap='gray')
plt.figure()
plt.imshow(A_new,cmap='gray')
        