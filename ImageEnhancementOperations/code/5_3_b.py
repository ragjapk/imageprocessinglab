# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 15:38:31 2018

@author: Student
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def get_image():
    img = plt.imread('C:/Users/IIST/Downloads/Ragja/3_SC18M003_Ragja_IP2018_latest/3_SC18M003_Ragja_IP2018/cameraman.tif')     
    pixels = img.flatten()
    plt.figure()
    plt.hist(pixels, bins=64, range=(0,256), normed=False, cumulative=True, color='red', alpha=0.4)    
    plt.title("Histogram of Cameraman")
    plt.xlabel("Pixel")
    plt.ylabel("Intensity")
    plt.show()
get_image()