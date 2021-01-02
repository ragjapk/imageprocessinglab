# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:40:39 2018

@author: IIST
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from PIL import Image
from scipy.misc import imsave
from scipy import fftpack as fftp
import imageio
import skimage.util as skp

lpf=np.matrix([[-1,-1,-1],[-1,8,-1,],[-1,-1,-1]])
hpf=np.matrix([[1,1,1],[1,1,1],[1,1,1]])
lpf = np.float_(lpf)
lpf=lpf/9
hpf = np.float_(hpf)
hpf=hpf/9

final_filter = np.zeros((256,256))
final_filter[:hpf.shape[0],:hpf.shape[1]] = hpf
print(final_filter)
f_filter=np.fft.fft2(final_filter)

final_filter2 = np.zeros((256,256))
final_filter2[:lpf.shape[0],:lpf.shape[1]] = lpf
print(final_filter2)
f_filter2=np.fft.fft2(final_filter2)

img = Image.open('C:/Users/IIST/Downloads/Ragja/6_SC18M003_Ragja_IP2018/gaussian_noise.png')
img.load()
data = np.asarray( img, dtype="float64" )

noise=skp.random_noise(data,mode='gaussian')
imsave('gaussian_noise_only.png',noise)

image_fft=fftp.fft2(data) 

final_image=image_fft*f_filter
image=np.fft.ifft2(final_image)
img_shft = np.fft.fftshift(final_image)
amp_fft=20*np.log(np.abs(img_shft))
plt.figure()
plt.imshow(amp_fft, cmap='gray')

final_image2=image_fft*f_filter2
image2=np.fft.ifft2(final_image2)
img_shft = np.fft.fftshift(final_image2)
amp_fft=20*np.log(np.abs(img_shft))
plt.figure()
plt.imshow(amp_fft, cmap='gray')
    
img=imageio.imwrite('5_inverse_lpf.png',image2)

img=imageio.imwrite('5_inverse_hpf.png',image)
