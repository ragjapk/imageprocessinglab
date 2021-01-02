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

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def svd_calc(M,size):
    g=np.array(M)
    g_transpose=np.transpose(g)
    gg_transpose=np.dot(g,g_transpose)

    eigen_val_1,eigen_vect_u=np.linalg.eigh(gg_transpose)
    eigen_val_1=list(eigen_val_1)
    eigen_vect_u=list(eigen_vect_u.T)
    #print(eigen_vect_u)
    v=np.zeros((size,size))
    u=np.zeros((size,size))
    eigen_val = [float(np_float) for np_float in eigen_val_1]
    basis=np.array([])
    to_be_zipped=(zip(eigen_val, eigen_vect_u))    
    eigen_val,eigen_vect_u=(list(t) for t in (zip(*sorted(to_be_zipped,key = lambda t: t[0], reverse=True))))

    for i in range(0,size):
        vector=np.array(eigen_vect_u[i])        
        u[i]=np.copy(vector)  
    print(u)
    for i in range(0,size):
        vector=np.array(eigen_vect_u[i],dtype='float')
        v_vector=np.dot(g,vector)
        v[i]=np.copy(v_vector)
    v=normalize(v)
    print(v)
    sing_values=np.sqrt(eigen_val)
    basis=np.zeros((size,size))
    for i in range(0,size):
        basis=basis+(sing_values[i]*(np.dot(u[i],v[i])))
        print(basis)
        #basis_img=Image.fromarray(basis.astype('uint8'))
       # plt.figure()
        #plt.imshow(basis_img, cmap = 'gray')

svd_calc([[0,1,0],[1,0,1],[0,1,0]],3)