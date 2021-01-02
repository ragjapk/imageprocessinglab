# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 11:22:42 2018

@author: IIST
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:38:03 2018

@author: IIST
"""

import scipy.io
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt2
from PIL import Image

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def get_histograms_ready():
    mat = scipy.io.loadmat('histG1_1.mat')
    hist_array=mat['histG']
    hist_array=np.array(hist_array)
    sum=0
    for i in range(len(hist_array)):
        sum=sum+hist_array[i]
    hist_array=hist_array/sum
    cdf_array=np.zeros((len(hist_array)))
    for i in range(len(hist_array)):
        if i==0:
            cdf_array[i]=hist_array[i]
        else:
            cdf_array[i]=cdf_array[i-1]+hist_array[i]
    cdf_array=255*cdf_array
    #plt.plot(cdf_array)     
    img2 = Image.open('C:/Users/IIST/Downloads/Ragja/6_SC18M003_Ragja_IP2018/0.png').convert('L')
    data=np.array(img2)
    
    historg=np.array(img2.histogram())/(data.shape[0]*data.shape[1])
    cdf2_array=np.zeros((len(historg)))
    for i in range(len(historg)):
        if i==0:
            cdf2_array[i]=historg[i]
        else:
            cdf2_array[i]=cdf2_array[i-1]+historg[i]
            
    cdf2_array=255*cdf2_array      
    #plt.plot(cdf2_array)        
    hist_specification(hist_array,cdf_array,cdf2_array,data)
    
    
def hist_specification(pdf1,cdf1,cdf2,data):
    look_up=np.zeros((cdf1.shape[0]))
    
    for i in range(cdf1.shape[0]):        
        look_up[i]=find_nearest(cdf2,cdf1[i])
        
    imgeq=np.zeros((data.shape[0],data.shape[1]))
    for i in range(0,data.shape[0]):
        for j in range(0, data.shape[1]):
            imgeq[i,j] = look_up[int(data[i,j])]
            
    imgfinal = Image.fromarray((imgeq).astype('uint8'))
    imgfinal.save('equalized_image.png')
    #print(final_probability)
    plt.subplot(313),plt.hist(imgeq),plt.title('after histogram equalization')
    #plt.subplot(313),plt.hist(imgeq),plt.title('after histogram equalization')
get_histograms_ready()