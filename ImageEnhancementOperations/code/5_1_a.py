# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 14:42:35 2018

@author: Student
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def get_image(image_name):
    image_path="C:/Users/Student/Downloads/ragja_iplab/".format(image_name);
    img = Image.open('C:/Users/Student/Downloads/ragja_iplab/mammogram.tif').convert('L')      
    img.load()
    data = np.asarray( img, dtype="float64" )
    negative=255
    negative_array=negative-data
    plt.figure()
    plt.imshow(negative_array,cmap='gray')
get_image('mammogram.tif')