# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 00:47:08 2018

@author: IIST
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from mpl_toolkits.mplot3d import Axes3D

A = Image.open('line.jpg').convert('L')
B = np.copy(A)
A = np.array(A)

count = 0
index = 0
theta = np.linspace(-90, 90, 180)
r, c = np.shape(A)

for i in range(0, r):
    for j in range(0, c):
        if A[i, j] != 255:
            count = count + 1


y = list([] for j in range(0,count))


for i in range(0, r):
    for j in range(0, c):
        if A[i, j] != 255:
            y[index] = (r-i)*np.cos(np.deg2rad(theta)) + j*np.sin(np.deg2rad(theta)) 
            index = index + 1    

for i in range(0,count):
    plt.plot(theta, y[i], color='red')
    
detect = cv2.line(B,(0,3),(324,321),(255,0,0),2)
dimg = Image.fromarray(detect)
plt.figure()
plt.imshow(dimg)