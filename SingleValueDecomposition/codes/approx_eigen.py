# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:22:12 2018

@author: IIST
"""
from PIL import Image
import numpy as np
from numpy import linalg
import random
from matplotlib import pyplot as plt
import math
def get_image(image_path,image_name):
    path=image_path+image_name
    print(path)
    img = Image.open(path)       
    img.load()
    data = np.asarray( img, dtype="float64" )
    approx_svd(data,data.shape[0])
    
def approx_svd(image,size):
    u,sing,vt = linalg.svd(image)   
    rank=len(sing)
    sing2=list(sing)
    print(rank)
    k=50
    for i in range(0,len(sing2)):
        if i>=k:
            sing2[i]=0
    print(sing2) 
    basis=np.zeros((size,size))
    for i in range(0,k):
       ui = u[:,i]
       vi = vt[i,:]
       appr = np.outer(ui,vi)
       appr=sing2[i]*appr
       basis=basis+appr
    #plt.figure()
    #plt.imshow(basis.real, cmap = 'gray')
    #Error via difference of actual and basis squared
    error=image-basis
    error_sum=np.sum(np.square(error))
    print(error_sum)
    #Error via sum of omitted singular values  
    err = 0
    #Calculation of Error
    for i in range(50,256):
        err = err + (sing[i]**2)
    print(err)
    
    #Plotting error
    err = list()
    for i in range(0,256):
        k = 0
        if i==255:
            break
        for j in range(i+1,256):
            k = k + sing[j] 
        err.append(k)

    err.append(0)
    kv = np.arange(0,256)
    plt.plot(kv,err)
    plt.title('k v/s Error plot')
    plt.xlabel('k')
    plt.ylabel('Error')


    
def noise_svd(image,size):    
    noise = np.random.randint(20,255, size=(size, size))
    imgnoise = image + noise
    plt.imshow(imgnoise.real, cmap='gray')
    
    noised_image_array = np.array(imgnoise)
    u, sing, vt = np.linalg.svd(noised_image_array)
    sing2=list(sing)
    basis=np.zeros((size,size))
    k=50
    for i in range(0,len(sing2)):
        if i>=k:
            sing2[i]=0
    print(sing2) 
    for i in range(0,k):
       ui = u[:,i]
       vi = vt[i,:]
       appr = np.outer(ui,vi)
       appr=sing[i]*appr
       basis=basis+appr
    plt.figure()
    plt.imshow(basis.real, cmap = 'gray')
    
    err = 0
    #Calculation of Error
    for i in range(51,256):
        err = err + (sing[i]**2)
    print(math.sqrt(err))
    #for i in range()
    # plotting the error
    '''err = list()
    #err = np.zeros((1,256))
    for i in range(0,256):
        k = 0
        if i==255:
            break
        for j in range(i+1,256):
            k = k + s[j] 
        err.append(k)
    
    #aerr = np.array(err)
    
    err.append(0)
    kv = np.arange(1,257)
    plot(kv,err)
    title('k v/s Error plot')
    xlabel('k')
    ylabel('Error')'''
get_image('C:/Users/IIST/Downloads/Ragja/3_SC18M003_Ragja_IP2018_latest/3_SC18M003_Ragja_IP2018/','cameraman.tif')