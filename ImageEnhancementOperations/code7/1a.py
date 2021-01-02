# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:47:44 2018

@author: IIST
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
img = Image.open('cameraman.tif').convert('L')
image = np.array(img)
h= np.ones((3,3))
h=np.float_(h)
h=h/(9)
f_image=np.fft.fft2(image)
final_filter = np.zeros((256,256))
final_filter[:h.shape[0],:h.shape[1]] = h

f_filter=np.fft.fft2(final_filter)

final_image=f_image*f_filter
image2=np.fft.ifft2(final_image)

unsharp_image = np.subtract(image,image2)
imgenh=np.zeros((256,256))
for i in range(0,256):
        for j in range(0,256):
            if(unsharp_image[i,j]<=-50):
                imgenh[i,j]=0
            elif(unsharp_image[i,j]>=50):
                imgenh[i,j]=255
            else:
                imgenh[i,j]=image[i,j]
plt.imsave('1_a_unmask_sharpening.png',imgenh, cmap='gray')