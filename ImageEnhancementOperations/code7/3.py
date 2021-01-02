# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:49:39 2018

@author: IIST
"""
import numpy as np
import math
from PIL import Image
from scipy import fftpack as fftp
import imageio
import cmath
from matplotlib import pyplot as plt

img = Image.open('C:/Users/IIST/Downloads/Ragja/7_SC18M003_Ragja_IP2018/Book.tif')
img.load()
data = np.asarray( img, dtype="float64" )

image_fft=fftp.fft2(data)
a=0.1
k=0.00025
T=1 
H=np.zeros((688,688),dtype="complex")

for u in range(1,689):
    for v in range(1,689):
        den=u**2+v**2
        exponent=k*(den**(5/6))        
        H[u-1,v-1]=math.exp(-exponent)
        
final_image2=image_fft*H
image2=np.fft.ifft2(final_image2)
imgfinal = Image.fromarray((image2).astype('uint'))
#imgfinal.save('equalized_image.png')
plt.imsave('3_low_turbulence.png',image2.real, cmap='gray')
#img=imageio.imwrite('inverse_filtered.png',image2)
