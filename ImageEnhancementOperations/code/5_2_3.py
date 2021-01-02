# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 15:34:48 2018

@author: Student
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def get_image():
    img = Image.open('C:/Users/Student/Downloads/ragja_iplab/3_kidney.png').convert('L')      
    img.load()
    data = np.asarray( img, dtype="uint8" )
    print(data)
    new_image=np.zeros((data.shape[0],data.shape[1]))
    for i in range(0,data.shape[0]):
        for j in range(0,data.shape[1]):
            if data[i][j]>=100 and data[i][j]<=150:
                final_intensity=data[i][j]+150
                if(final_intensity>255):
                    new_image[i][j]=255
                else:
                    new_image[i][j]=data[i][j]+150
            else:
                new_image[i][j]=0
    print(new_image)
    plt.figure()
    plt.imshow(new_image,cmap='gray')

get_image()