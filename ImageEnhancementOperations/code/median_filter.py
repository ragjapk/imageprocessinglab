# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:11:42 2018

@author: IIST
"""

from PIL import Image
import numpy as np
from scipy.misc import imsave
from matplotlib import pyplot as plt

def get_image2():
    img = Image.open('C:/Users/IIST/Downloads/Ragja/5_SC18M003_Ragja_IP2018/ragja_iplab/gaussian_noise.png').convert('L')
    data = np.asarray( img, dtype="uint8" )
    noise_removal_median_filter(img,data,3)
    
def noise_removal_median_filter(img,data,size):    
    filter_ = [(0,0)] *size*size
    newimg = Image.new("L",(data.shape[0],data.shape[1]),"white")
    for i in range(1,data.shape[0]-1):
        for j in range(1,data.shape[1]-1):
            filter_[0] = img.getpixel((i-1,j-1))
            filter_[1] = img.getpixel((i-1,j))
            filter_[2] = img.getpixel((i-1,j+1))
            filter_[3] = img.getpixel((i,j-1))
            filter_[4] = img.getpixel((i,j))
            filter_[5] = img.getpixel((i,j+1))
            filter_[6] = img.getpixel((i+1,j-1))
            filter_[7] = img.getpixel((i+1,j))
            filter_[8] = img.getpixel((i+1,j+1))
            filter_.sort()
            newimg.putpixel((i,j),(filter_[4]))
    plt.figure()
    plt.imshow(newimg,cmap='gray')
    imsave('gaussian_noise_removed_median_3_latest.png',newimg)
    
get_image2()