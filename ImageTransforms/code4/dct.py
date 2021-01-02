# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:07:42 2018

@author: IIST
"""
from PIL import Image
import numpy as np
from scipy import fftpack as fftp
from matplotlib import pyplot as plt

def get_image(image_path,image_name):
    path=image_path+image_name
    print(path)
    img = Image.open(path)    
    
    img.load()
    data = np.asarray( img, dtype="float64" )
    find_dft(data)
    find_dct(data)


def find_dft(matrix):
    image_fft=fftp.fft2(matrix) 
    img_shft = np.fft.fftshift(image_fft)
    amp_fft=20*np.log(np.abs(img_shft))
    plt.figure()
    plt.imshow(amp_fft, cmap='gray')

def find_dct(matrix):
    image_fft=fftp.dct(matrix)
    img_shft = np.fft.fftshift(image_fft)
    amp_fft=20*np.log(np.abs(img_shft))
    plt.figure()
    plt.imshow(amp_fft, cmap='gray')
    
#get_image('C:/Users/IIST/Downloads/Ragja/3_SC18M003_Ragja_IP2018_latest/3_SC18M003_Ragja_IP2018/','horiz.png')
#get_image('C:/Users/IIST/Downloads/Ragja/3_SC18M003_Ragja_IP2018_latest/3_SC18M003_Ragja_IP2018/','vertical.png')
get_image('C:/Users/IIST/Downloads/Ragja/3_SC18M003_Ragja_IP2018_latest/3_SC18M003_Ragja_IP2018/','cameraman.tif')
