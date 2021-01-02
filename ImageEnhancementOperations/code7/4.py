# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:43:20 2018

@author: IIST
"""

import numpy as np
from PIL import Image
from scipy import fftpack as fftp
from matplotlib import pyplot as plt
from degradation import return_degraded_image

image_array,H=return_degraded_image()
G=fftp.fft2(image_array)

F=np.zeros((688,688),dtype="complex")
H_=np.zeros((688,688),dtype="complex")
avg_filter_value=H[0,0]
H_=H_+avg_filter_value
F=np.divide(G,H)        

image2=np.fft.ifft2(F)
plt.imsave('restored_image.png',image2.real, cmap='gray')


