# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:00:00 2018

@author: IIST
"""
import matplotlib.pyplot as plt
import numpy as np
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

B2=[[0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]]
B1=np.asarray(B1)
B2=np.asarray(B2)

B=np.flipud(B1)
A_new=np.zeros((A.shape))
for i in range(A.shape[0]):
    for j in range(A.shape[1]):        
        mask=A[i:i+B.shape[0],j:j+B.shape[1]]
        B_prime=B[:mask.shape[0],:mask.shape[1]]
        for k in range(B.shape[0]):
            for l in range(B.shape[1]):
                
A_new=np.flipud(A_new)                    
plt.imshow(A_org,cmap='gray')
plt.figure()
plt.imshow(A_new,cmap='gray')