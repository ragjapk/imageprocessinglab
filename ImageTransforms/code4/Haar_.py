# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:09:51 2018

@author: IIST
"""

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def get_image(matrix):
    data = np.asarray( matrix, dtype="uint8" )
    #Plot original Image
    #plt.figure()
    #plt.imshow(data, cmap='gray')
    #Obtain Haar Matrix
    h=haarMatrix(8)
    plt.figure()
    plt.imshow(h, cmap='gray')
    ht = h.T
    ght = np.dot(data,ht)
    hght = np.dot(h,ght)
    haarimg = Image.fromarray(hght.astype('uint8'))
    #plt.figure()
   # plt.imshow(haarimg, cmap='gray')
    #Obtain Reconstructed Image
    a = hght
    ah = np.dot(a,h)
    htah = np.dot(ht,ah)
    #plt.figure()
    #plt.imshow(htah, cmap='gray')
    
def haarMatrix(n, normalized=True):
    n = 2**np.ceil(np.log2(n))
    if n > 2:
        h = haarMatrix(n / 2)
    else:
        return np.array([[1, 1], [1, -1]])
    h_n = np.kron(h, [1, 1])
    if normalized:
        h_i = np.sqrt(n/2)*np.kron(np.eye(len(h)), [1, -1])
    else:
        h_i = np.kron(np.eye(len(h)), [1, -1])
    h = np.vstack((h_n, h_i))
    return h


get_image([[255,255,255,255,255,255,255,255],
     [255,255,255,100,100,100,255,255],
     [255,255,100,150,150,150,100,255],
     [255,255,100,150,200,150,100,255],
     [255,255,100,150,150,150,100,255],
     [255,255,255,100,100,100,255,255],
     [255,255,255,255,50,255,255,255],
     [50,50,50,50,255,255,255,255]])


