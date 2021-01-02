# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:47:44 2018

@author: IIST
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
from scipy import signal
from scipy.ndimage.filters import gaussian_filter
from skimage.filters import gaussian
img = Image.open('cameraman.tif').convert('L')
image = np.array(img)
h=gaussian(image, 0.5, mode='nearest')
plt.imshow(h,cmap='gray')
imgenh=np.zeros((256,256))
for i in range(0,256):
        for j in range(0,256):
            imgenh[i][j]=(math.log((image[i][j]+1)/h[i][j]))*255
plt.imsave('1_retinex.png',imgenh, cmap='gray')