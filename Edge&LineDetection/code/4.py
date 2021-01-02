# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:51:59 2018

@author: IIST
"""

from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from PIL import Image

def Sobel(img, direction):
    if(direction == 'x'):
       fx=[[-1,0,1],[-2,0,2],[-1,0,1]]
       edge=signal.convolve2d(img,fx)
    if(direction == 'y'):
       fy=[[-1,-2,-1],[0,0,0],[1,2,1]]
       edge=signal.convolve2d(img,fy)
    return edge


def normalize(img):
    img = img/np.max(img)
    return img

def nonmaxima_supression(Gmag, Grad):
    NMS = np.zeros(Gmag.shape)
    for i in range(1, int(Gmag.shape[0]) - 1):
        for j in range(1, int(Gmag.shape[1]) - 1):
            if((Grad[i,j] >= -22.5 and Grad[i,j] <= 22.5) or (Grad[i,j] <= -157.5 and Grad[i,j] >= 157.5)):
                if((Gmag[i,j] > Gmag[i,j+1]) and (Gmag[i,j] > Gmag[i,j-1])):
                    NMS[i,j] = Gmag[i,j]
                else:
                    NMS[i,j] = 0
            if((Grad[i,j] >= 22.5 and Grad[i,j] <= 67.5) or (Grad[i,j] <= -112.5 and Grad[i,j] >= -157.5)):
                if((Gmag[i,j] > Gmag[i+1,j+1]) and (Gmag[i,j] > Gmag[i-1,j-1])):
                    NMS[i,j] = Gmag[i,j]
                else:
                    NMS[i,j] = 0
            if((Grad[i,j] >= 67.5 and Grad[i,j] <= 112.5) or (Grad[i,j] <= -67.5 and Grad[i,j] >= -112.5)):
                if((Gmag[i,j] > Gmag[i+1,j]) and (Gmag[i,j] > Gmag[i-1,j])):
                    NMS[i,j] = Gmag[i,j]
                else:
                    NMS[i,j] = 0
            if((Grad[i,j] >= 112.5 and Grad[i,j] <= 157.5) or (Grad[i,j] <= -22.5 and Grad[i,j] >= -67.5)):
                if((Gmag[i,j] > Gmag[i+1,j-1]) and (Gmag[i,j] > Gmag[i-1,j+1])):
                    NMS[i,j] = Gmag[i,j]
                else:
                    NMS[i,j] = 0

    return NMS

def hysterisis_threshold(img):
    highThresholdRatio = 0.2  
    lowThresholdRatio = 0.15 
    GSup = np.copy(img)
    h = int(GSup.shape[0])
    w = int(GSup.shape[1])
    highThreshold = np.max(GSup) * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio    
    x = 0.1
    oldx=0
    while(oldx != x):
        oldx = x
        for i in range(1,h-1):
            for j in range(1,w-1):
                if(GSup[i,j] > highThreshold):
                    GSup[i,j] = 1
                elif(GSup[i,j] < lowThreshold):
                    GSup[i,j] = 0
                else:
                    if((GSup[i-1,j-1] > highThreshold) or 
                        (GSup[i-1,j] > highThreshold) or
                        (GSup[i-1,j+1] > highThreshold) or
                        (GSup[i,j-1] > highThreshold) or
                        (GSup[i,j+1] > highThreshold) or
                        (GSup[i+1,j-1] > highThreshold) or
                        (GSup[i+1,j] > highThreshold) or
                        (GSup[i+1,j+1] > highThreshold)):
                        GSup[i,j] = 1
        x = np.sum(GSup == 1)
    
    GSup = (GSup == 1) * GSup 
    
    return GSup

img = misc.imread("gaussian_noise.png") 
img = ndimage.gaussian_filter(img, sigma=1.2) 


gx = Sobel(img, 'x')
gx = normalize(gx)

gy = Sobel(img, 'y')
gy = normalize(gy)

dx = ndimage.sobel(img, axis=1) 
dy = ndimage.sobel(img, axis=0) 


G = np.hypot(gx,gy)
G = normalize(G)

mag = np.hypot(dx,dy)
mag = normalize(mag)

Gradient = np.degrees(np.arctan2(gy,gx))

gradient = np.degrees(np.arctan2(dy,dx))

NMS = nonmaxima_supression(G, Gradient)
NMS = normalize(NMS)

image = hysterisis_threshold(NMS)
plt.imshow(image, cmap = plt.get_cmap('gray'))
plt.show()
