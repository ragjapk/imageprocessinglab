# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:37:31 2018

@author: IIST
"""

import numpy as np

from PIL import Image
import matplotlib.pyplot as plt
from  scipy import signal
import scipy.misc
def get_image():
    #img1 = Image.open('cameraman.png').convert('L')      
    #img1.load()
    img2 = Image.open('gaussian_noise.png').convert('L')      
    img2.load()
    data1 = np.asarray( img2, dtype="uint8" )
    laplacian=[[0,1,0],[1,-4,1],[0,1,0]]
    #log=[[-12,-24,-12],[-24,-40,-24],[-12,-24,-12]]
    ans1=signal.convolve2d(data1,laplacian)       
    plt.imshow(Image.fromarray(ans1),cmap='gray')
get_image()
