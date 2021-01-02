# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 21:37:23 2018

@author: IIST
"""
import numpy as np
from PIL import Image
import imageio

def interpolation(image):   
    width,height =image.shape
    out_image = np.zeros(2*height*2*width).reshape(2*height,2*width)
    for m in range(height-1):
       for n in range(width-1):
           out_image[2*m][2*n] = image[m][n]
           out_image[2*m][2*n+1]= (image[m][n] + image[m][n + 1])/2
           out_image[2*m + 1][2*n] = (image[m][n] + image[m + 1][n])/2
           out_image[2*m+1][2*n+1] = (image[m][n]+image[m+1][n]+image[m][n+1]+image[m+1][n + 1])/4
    
    im =Image.fromarray(out_image.astype('int8'),'L')
    im.show()
    return im

def sampleby4(data):
    data = np.asarray( data, dtype="int64" )  
    im=interpolation(data)
    data = np.asarray( im, dtype="int64" ) 
    imageio.imwrite('upsampled_bilinear2.png',data)

def get_image():
    img = Image.open('C:/Users/IIST/Downloads/Ragja/3_SC18M003_Ragja_IP2018_latest/3_SC18M003_Ragja_IP2018/1_a.png').convert('L')
    img.load()
    data = np.asarray( img, dtype="int64" )    
    #interpolated=interpolation(data)
   
    sampleby4(data)
    
get_image()