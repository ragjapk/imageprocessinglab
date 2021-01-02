# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:01:07 2018

@author: IIST
"""

from matplotlib import pyplot as plt
import numpy as np
def get_image():
    img = plt.imread('C:/Users/IIST/Downloads/Ragja/6_SC18M003_Ragja_IP2018/cameraman.tif')     
    data = np.asarray( img, dtype="float64" )
    img=img.flatten()
    plt.figure()
    cdf, bins, patch=plt.hist(img, bins=64, range=(0,256), normed=True, cumulative=True)    
    new_pixels = np.interp(img, bins[:-1], cdf*255)
    new_image = new_pixels.reshape(data.shape)
    plt.imshow(new_image, cmap='gray')    
    #cdf, bins, patche=plt2.hist(new_pixels, bins=256, range=(0,256), normed=True, color='blue', alpha=0.4, cumulative=True)    
 
get_image()