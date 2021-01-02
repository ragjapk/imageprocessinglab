# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:02:29 2018

@author: IIST
"""

import numpy as np
from PIL import Image
from scipy import signal
import matplotlib.pyplot as plt

img=Image.open('gaussian_noise.png').convert('L')
img=np.asarray(img)

fx=[[1,0],[0,-1]]
fy=[[0,1,],[-1,0]]
horizontal=signal.convolve2d(img,fx)
vertical=signal.convolve2d(img,fy)

plt.imshow(Image.fromarray(horizontal),cmap='gray')
plt.figure()
plt.imshow(Image.fromarray(vertical),cmap='gray')