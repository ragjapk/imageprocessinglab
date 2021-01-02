# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:53:21 2018

@author: IIST
"""
from PIL import Image
from skimage.measure import block_reduce
import numpy as np
import imageio



def interpolate(image):
    new_image=block_reduce(image, block_size=(2, 2), func=np.sum)
    img=imageio.imwrite('1_a.png',new_image)
    
def interpolate2(image):
    new_image=block_reduce(image, block_size=(4, 4), func=np.sum)
    img=imageio.imwrite('1_a_4.png',new_image)
    
def get_image():
    img = Image.open('C:/Users/IIST/Downloads/Ragja/3_SC18M003_Ragja_IP2018/peppers.png').convert('L')
    img.load()
    data = np.asarray( img, dtype="float64" )
    imageio.imwrite('peppers_salt.png',data)
    interpolate2(data)

get_image()