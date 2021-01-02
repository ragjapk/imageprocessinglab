# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 21:39:02 2018

@author: IIST
"""

A = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
      [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
      [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

B = [0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0]

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



def W_calculation(x,y):
    k=list()
    x = x+2
    y = y+2    
    for i in range(x-2,x+3):
        for j in range(y-2,y+3):
            k.append(a1[i][j])
    return k        
A=np.array(A)
A_new = np.copy(A)

a1 = np.pad(A_new, ((1,1),(1,1)), 'constant')
a1 = np.pad(a1, ((1,1),(1,1)), 'constant')

for i in range(A_new.shape[0]):
    for j in range(A_new.shape[1]):
        neighbors = W_calculation(i,j)
        if (neighbors == B): 
            rx = i
            ry = j
            
            
l1 = np.arange(rx-2,rx+3)
l2 = np.arange(ry-2,ry+3)

for i in range(A_new.shape[0]):
    for j in range(A_new.shape[1]):
        if not((i in l1) and (j in l2)):
            A_new[i][j] = 0

plt.imshow(Image.fromarray(A*255))
plt.figure()
plt.imshow(Image.fromarray(A_new*255))