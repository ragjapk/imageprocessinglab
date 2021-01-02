# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:59:49 2018

@author: Student
"""

from sympy import Symbol
from sympy.polys.polytools import Poly
import numpy as np
from sympy import Matrix

def eigen_calc(M):
    x = Symbol('x')
    M = Matrix(M)
    I=Matrix([[x,0,0],[0,x,0],[0,0,x]])
    MI=M-I
    char_equation=MI.det()
    a = Poly(char_equation, x)
    eigen_values=np.roots(a.coeffs())
    return eigen_values

print(eigen_calc([[1,0,1],[0,1,1],[0,0,0]]))