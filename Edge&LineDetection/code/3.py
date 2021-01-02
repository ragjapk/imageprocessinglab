# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:58:31 2018

@author: IIST
"""
from PIL import Image
import matplotlib.pyplot as plt
from  scipy import signal
import scipy.misc
import math
import numpy as np
o=1.4
pi=math.pi
log=np.ones((9,9))
k=0
for i in range(-5,4):
    l=0
    for j in range(-5,4):
        log[k,l]=(-1)/(pi*o**4)*(1-(i**2+j**2)/(2*o**2))*math.exp(-(i**2+j**2)/(2*o**2))
        log[k,l]=log[k,l]*10**3
        #print(log[k,l])
        l=l+1
    k=k+1
log=log.astype(int)
print(log)

img2 = Image.open('gaussian_noise.png').convert('L')      
img2.load()
data1 = np.asarray( img2, dtype="uint8" )
ans1=signal.convolve2d(data1,log)       
plt.imshow(Image.fromarray(ans1),cmap='gray')