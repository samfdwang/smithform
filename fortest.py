# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:10:09 2016

@author: fudong
"""

import numpy as np
def ind2rc(shp,ind):
    c = ind%shp[1];
    r = int((ind-c)/shp[0]);
    rc=[r,c];
    return rc;
    
myA = np.array([[20,24,4],[-6,2,12],[10,-4,-16]]);
# assuming nr<=nc
sizeA = myA.shape;
exA= np.zeros((sum(sizeA),sum(sizeA)),dtype=np.int);
exA[0:sizeA[0],0:sizeA[1]]=myA;
exA[sizeA[0]:,0:sizeA[1]]=np.identity(sizeA[0]);
exA[0:sizeA[0]:,sizeA[1]:]=np.identity(sizeA[1]);
A=myA.copy();
minA = abs(A).min();
# for sparse matrix, there can be improved.

rcA = ind2rc(sizeA,abs(A).argmin())
exA[[0,rcA[0]]] = exA[[rcA[0],0]];
exA=exA.transpose();
exA[[0,rcA[1]]] = exA[[rcA[1],0]];
exA=exA.transpose();
for kk in range(sizeA[0]-1):
    exA[kk+1,:]=exA[kk+1,:]-exA[kk+1,0]/exA[0,0]*exA[0,:];
for kk in range(sizeA[1]-1):
    exA[:,kk+1]=exA[:,kk+1]-exA[0,kk+1]/exA[0,0]*exA[:,0];