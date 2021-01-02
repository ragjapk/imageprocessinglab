# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 16:03:53 2018

@author: Student
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import skimage.util as skp
import math
from scipy import signal
from scipy.misc import imsave
def get_image():
    img = Image.open('C:/Users/Student/Downloads/ragja_iplab/cameraman.tif').convert('L')      
    img.load()
    data = np.asarray( img, dtype="uint8" )
    noise_creation_gaussian(data)
    
def noise_creation_gaussian(data):
    noise=skp.random_noise(data,mode='gaussian')
    imsave('gaussian_noise.png',noise)
    
def get_image2():
    img = Image.open('C:/Users/Student/Downloads/ragja_iplab/impulse_noise.png').convert('L')      
    img.load()
    data = np.asarray( img, dtype="uint8" )
    noise_removal_median_filter(data,3)
    #noise_removal_mean_filter(data,11)

def noise_removal_median_filter(data,size):  # size = 3 -> radius = 1
    radius=size-2
    filtered=np.zeros(shape=(data.shape[0],data.shape[1]))
    for y in range(0,data.shape[0]-1):
        top = max(y - radius, 0)
        bottom = min(y + radius,data.shape[0]-1)    
        for x in range(0,data.shape[1]-1):
            left = max(x - radius, 0)
            right = min(x + radius, data.shape[1]-1) 
            values = list()    
            for v in range(top, bottom):
                for u in range(left,right):
                    values.append(data[v][u])
            filtered[y][x] = np.median(values)
    plt.figure()
    plt.imshow(filtered,cmap='gray')
    imsave('impulse_noise_removed_median_3-.png',filtered)
    
def noise_removal_mean_filter(data,size):
    h=np.ones(shape=(size,size))
    h=np.float_(h)
    h=h/size*size
    h=np.array(h)
    image=signal.convolve2d(data,h)
    plt.figure()
    plt.imshow(image,cmap='gray')
    imsave('gaussian_noise_removed_mean_11.png',image)

'''def noise_removal_median_filter_actual(data,size):
   for i in range(0,data.shape[0]):
       for j in range(0,data.shape[1]-1):'''
           
    
get_image2()