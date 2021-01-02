# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:00:00 2018

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

A=np.asarray(A)

B1=[[0, 0, 0],
    [0, 0, 0],
    [0, 1, 1]]


B2=[[0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]]
B1=np.asarray(B1)
B2=np.asarray(B2)
B=B1
A_new=np.zeros((A.shape))
for i in range(A.shape[0]):
    for j in range(A.shape[1]):        
        mask=A[i:i+B.shape[0],j:j+B.shape[1]]
        B_prime=B[:mask.shape[0],:mask.shape[1]]
        print(mask.shape[0],mask.shape[1],B_prime.shape[0],B_prime.shape[1])
        for k in range(mask.shape[0]):
            for l in range(mask.shape[1]):
                if(mask[k,l]==B_prime[k,l] and mask[k,l]==1):
                    A_new[i,j]=1
                    break
print(A_new)
plt.imshow(A,cmap='gray')
plt.figure()
plt.imshow(A_new,cmap='gray')
        #if(sum(np.multiply(mask,B))!=0):
            #A_new[i,j]=1
#print(A_new)