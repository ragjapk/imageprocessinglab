# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:07:52 2018

@author: IIST
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from PIL import Image
from scipy.misc import imsave
from scipy import fftpack as fftp
import imageio
import skimage.util as skp
import math

def get_image_horiz():
    img = Image.open('C:/Users/IIST/Downloads/Ragja/6_SC18M003_Ragja_IP2018/horiz.png')
    img.load()
    data = np.asarray( img, dtype="float64" )    
    log_transform(data)
def get_image_vertical():
    img = Image.open('C:/Users/IIST/Downloads/Ragja/6_SC18M003_Ragja_IP2018/vertical.png')
    img.load()
    data = np.asarray( img, dtype="float64" )
    log_transform(data)
def get_image_cameraman():
    img = Image.open('C:/Users/IIST/Downloads/Ragja/6_SC18M003_Ragja_IP2018/cameraman.tif')
    img.load()
    data = np.asarray( img, dtype="float64" )
    log_transform(data)    
def log_transform(data):
    C=10
    row,cols=data.shape
    new_data=np.zeros((row,cols))
    for i in range(row):
        for j in range(cols):
            new_data[i,j]=C*math.log(data[i,j]+1)
    print(new_data)
    plt.figure()
    plt.imshow(new_data,cmap='gray')

get_image_horiz()
get_image_vertical()
get_image_cameraman()