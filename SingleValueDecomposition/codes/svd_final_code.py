# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:50:25 2018

@author: Student
"""
#from lab3_eigenvalues import eigen_calc
import numpy as np
import math
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt2
from numpy.lib import scimath as sm
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def svd_calc(M,size):
    g=np.array(M)
    g_transpose=np.transpose(g)
    gg_transpose=np.dot(g,g_transpose)
    g_transposeg=np.dot(g_transpose,g)
    eigen_val_1,eigen_vect_u=np.linalg.eigh(gg_transpose)
    eigen_val_2,eigen_vect_v=np.linalg.eigh(g_transposeg)
    
    #eigen_vect_u=list(eigen_vect_u.T)
    #eigen_vect_v=list(eigen_vect_v.T)

    v=np.zeros((size,size))
    u=np.zeros((size,size))
    
    #eigen_val = [float(np_float) for np_float in eigen_val_1]
    basis=np.array([])
    
    #to_be_zipped=(zip(eigen_val, eigen_vect_u)) 
    #to_be_zipped2=(zip(eigen_val, eigen_vect_v))     
   
    #eigen_val,eigen_vect_u=(list(t) for t in (zip(*sorted(to_be_zipped,key = lambda t: t[0], reverse=True))))
    #eigen_val,eigen_vect_v=(list(t) for t in (zip(*sorted(to_be_zipped2,key = lambda t: t[0], reverse=True))))
    index = eigen_val_1.argsort()[::-1]
    sing_values=sm.sqrt(eigen_val_1[index])
    eigen_vect_u=eigen_vect_u[:,index]
    eigen_vect_v=eigen_vect_v[:,index]
    #size=size-3
    for i in range(0,size):
        vector=np.array(eigen_vect_u[i])        
        u[i]=np.copy(vector)   
    #print(u)
    for i in range(0,size):
        vector=np.array(eigen_vect_v[i])
        v[i]=np.copy(vector)
    #print(v)    
   
    print(sing_values)
    for i in range(0,size):
        basis=np.zeros((size,size))
        outer_product=np.outer(u[:,i],v[i,:])
        #print(outer_product)
        basis=basis+(sing_values[i]*outer_product)
        #print(basis)
        basis_img=Image.fromarray(basis.astype('uint8'))
        plt.figure()
        plt.imshow(basis.real, cmap = 'gray')
   
#svd_calc([[0,1,0],[1,0,1],[0,1,0]],3)
svd_calc([[255,255,255,255,255,255,255,255],
     [255,255,255,100,100,100,255,255],
     [255,255,100,150,150,150,100,255],
     [255,255,100,150,200,150,100,255],
     [255,255,100,150,150,150,100,255],
     [255,255,255,100,100,100,255,255],
     [255,255,255,255,50,255,255,255],
     [50,50,50,50,255,255,255,255]],8)