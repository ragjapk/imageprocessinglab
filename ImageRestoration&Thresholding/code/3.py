# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:22:23 2018

@author: IIST
"""

from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
def get_image():
    img = Image.open('cameraman.tif').convert('L')   
    data = np.asarray( img, dtype="float64" )
    new_image=np.zeros((data.shape[0],data.shape[1]))
    img.load()
    img = plt.imread('cameraman.tif')     
    img=img.flatten()
    #plt.figure()
    cdf, bins, patch=plt.hist(img, bins=256, range=(0,256), normed=True, cumulative=False)
    grey_levels=np.arange(0,256,1)
    #print(grey_levels)
    uL=np.dot(grey_levels,cdf)
    theta=np.sum(cdf)
    u=uL/theta
    sigma_sqr_b=np.NINF
    i=0
    diff=1
    while(diff>0 and i<256):
        print(i)
        ut=np.dot(grey_levels[:i],cdf[:i])
        thetat=np.sum(cdf[:i])
        num=(ut-u*thetat)**2
        den=thetat*(1-thetat)
        if(den==0):
            i=i+1
            continue
        sigma_sqr_b_new=num/den
        diff=sigma_sqr_b_new-sigma_sqr_b  
        print(diff)
        sigma_sqr_b=sigma_sqr_b_new
        i=i+1
    for k in range(0,data.shape[0]):
        for j in range(0,data.shape[1]):
            if data[k][j]>=i-1:
                new_image[k][j]=255
            else:
                new_image[k][j]=0
    plt.imsave('cameraman_otsu_thresholding.png',new_image,cmap='gray')
get_image();