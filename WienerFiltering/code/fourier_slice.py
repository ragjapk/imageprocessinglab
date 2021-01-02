# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:07:10 2018

@author: Student
"""

import matplotlib.pyplot as plt
from scipy import fftpack as fftp
from skimage.io import imread
from skimage import data_dir
from skimage.transform import radon, iradon
from scipy.ndimage import zoom
import numpy as np
import math
from scipy.misc import toimage
from PIL import Image
image = Image.open("phantom.png").convert('L')
image = image.resize((180,180))
image.save("phantom_mod.png")
data = np.matrix( image, dtype="uint8" )
pr = radon(data)
#toimage(pr).show()
F=np.zeros((180,180))
P=np.zeros((pr.shape[0],pr.shape[1]),dtype="complex")
#plt.plot(projections);
for theta in range(pr.shape[1]):
    column=pr[:,theta]
    ffted=fftp.fft(column)
    P[:,theta]=ffted

for rho in range(180):
    for theta in range(180):
        f_cos=abs(math.floor(rho*(math.cos(math.radians(theta)))))
        f_sin=abs(math.floor(rho*(math.sin(math.radians(theta)))))   
        F[f_cos,f_sin]=P[rho,theta]
imgreal=np.real(fftp.ifftshift((fftp.ifft2(F))))
#maxim=max(imgreal.flatten())
#minm=min(imgreal.flatten())
#for u in range(180):
#    for v in range(180):
#        imgreal[u,v] = round(((imgreal[u,v] - minm) / (maxim - minm) ) * (255 - 0) + 0)
#toimage(imgreal.show())
plt.imsave('original_image.png',imgreal)