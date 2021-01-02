# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 01:35:42 2018

@author: IIST
"""

import numpy as np
from scipy import linalg
from PIL import Image
from matplotlib import pyplot as plt


def find_Hadamard(matrix):
    data = np.asarray( matrix, dtype="uint8" )
    #Plot original Image
    plt.figure()
    plt.imshow(data, cmap='gray')
    
    h = linalg.hadamard(8)
    #Plot Hadamard Matrix
    plt.figure()
    plt.imshow(h, cmap='gray')
    
    ht = h.T
    ght = np.dot(data,ht)
    hght = np.dot(h,ght)

    plt.figure()
    plt.imshow(hght, cmap='gray')

    a = hght
    ah = np.dot(a,h)
    htah = np.dot(ht,ah)

    plt.figure()
    plt.imshow(htah, cmap='gray')

find_Hadamard([[255,255,255,255,255,255,255,255],
     [255,255,255,100,100,100,255,255],
     [255,255,100,150,150,150,100,255],
     [255,255,100,150,200,150,100,255],
     [255,255,100,150,150,150,100,255],
     [255,255,255,100,100,100,255,255],
     [255,255,255,255,50,255,255,255],
     [50,50,50,50,255,255,255,255]])