# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:53:45 2018

@author: IIST
"""
from PIL import Image
import matplotlib.pyplot as plt
from  scipy import signal
import scipy.misc
import math
import numpy as np
from scipy.ndimage import filters

N = 9 #filter size
ff = np.zeros((N,N))
ff[int((N-1)/2)][int((N-1)/2)] = 1

g1=filters.gaussian_filter(ff, 0.5)
g2=filters.gaussian_filter(ff, 3)

gauss = g2 - g1

img2 = Image.open('gaussian_noise.png').convert('L')      
img2.load()
data1 = np.asarray( img2, dtype="uint8" )
ans1=signal.convolve2d(data1,gauss)       
plt.imshow(Image.fromarray(ans1),cmap='gray')