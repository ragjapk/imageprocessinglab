# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:36:27 2018

@author: IIST
"""

import numpy as np
from PIL import Image
from scipy import signal
import matplotlib.pyplot as plt

img=Image.open('gaussian_noise.png').convert('L')
img=np.asarray(img)

#vertical kernel
fx=[[-1,0,1],[-2,0,2],[-1,0,1]]

#horizontal kernel
fy=[[-1,-2,-1],[0,0,0],[1,2,1]]

vertical=signal.convolve2d(img,fy)
horizontal=signal.convolve2d(img,fx)

plt.imshow(Image.fromarray(vertical),cmap='gray')
plt.figure()
plt.imshow(Image.fromarray(horizontal),cmap='gray')