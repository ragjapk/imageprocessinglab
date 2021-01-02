# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:09:25 2018

@author: IIST
"""

from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
def get_image():
    img = Image.open('Book.tif').convert('L')   
    data = np.asarray( img, dtype="float64" )
    new_image=np.zeros((data.shape[0],data.shape[1]))
    img.load()
    img = plt.imread('Book.tif')     
    img=img.flatten()
    plt.figure()
    cdf, bins, patch=plt.hist(img, bins=255, range=(0,256), normed=True, cumulative=False)
    for i in range(0,data.shape[0]):
        for j in range(0,data.shape[1]):
            if data[i][j]>=150 or data[i][j]<=50:
                new_image[i][j]=255
            else:
                new_image[i][j]=0
    #print(new_image)
    plt.imsave('book_bin_thresholding.png',new_image,cmap='gray')
    #plt.show()    
    
get_image();