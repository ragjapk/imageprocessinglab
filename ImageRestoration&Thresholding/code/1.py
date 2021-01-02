# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:12:11 2018

@author: IIST
"""
from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import fftpack as fftp
from degradation import return_degraded_image

def get_mean_avg_val_imge():
    img = plt.imread('degraded.png')     
    img=img.flatten()
    #plt.figure()
    cdf, bins, patch=plt.hist(img, bins=256, range=(0,256), normed=True, cumulative=False)
    grey_levels=np.arange(0,256,1)
    #print(grey_levels)
    uL=np.dot(grey_levels,cdf)
    theta=np.sum(cdf)
    u=uL/theta
    return u
def get_image():
    img = Image.open('Book.tif').convert('L')      
    img.load()
    I = np.asarray( img, dtype="uint8" )
    data=I
    l_2 = np.zeros((688,688))
    N=688
    pi=math.pi
    for n in range(0,data.shape[1]):
        t1=1/N**4
        t2=(N-5)**2
        t3=2*(N-5)*math.cos(2*pi*n/N)
        t4=2*(N-5)*math.cos(2*pi*n*(N-1)/N)
        t5=2*math.cos((2*pi*(N-2)*n)/N)
        l_2[0,n]=(t1*(t2+t3+t4+t5))
    for m in range(1,data.shape[0]):
        for n in range(0,data.shape[1]):
            l_2[m,n]=(1/N**4)*(25+2-(10*math.cos(2*math.pi*n/N)-10*math.cos((2*math.pi*(N-1)*n)/N)+2*math.cos((2*math.pi*(N-2)*n)/N)))
    gamma=10*30
    temp2=gamma*l_2
    g,H=return_degraded_image()
    u=get_mean_avg_val_imge()  
    G=fftp.fft2(g)
    temp=abs(H)**2
    M_temp=temp/(temp+temp2)
    M=M_temp/H
    F=G*M
    f=fftp.ifft2(F)
    f=f.real
    f=f+u*(10**-31)
    plt.imsave('restored_book.png',f,cmap='gray')
get_image()