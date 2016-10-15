# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:23:57 2016

@author: fudong
"""
# SmithForm

#import lib
import numpy as np
def ind2rc(shp,ind):
    c = ind%shp[1];
    r = int((ind-c)/shp[0]);
    rc=[r,c];
    return rc;
    
def Smith(myA):
    print('original input:')
    print(myA)
    sizemyA = myA.shape;
    if sizemyA[0]>sizemyA[1]:
        transind=1;
        sizemyA=myA.transpose().shape;
        myA=myA.transpose();
    else:
        transind=0;
    exA= np.zeros((sum(sizemyA),sum(sizemyA)),dtype=np.int);
    exA[0:sizemyA[0],0:sizemyA[1]]=myA;
    exA[sizemyA[0]:,0:sizemyA[1]]=np.identity(sizemyA[1]);
    exA[0:sizemyA[0]:,sizemyA[1]:]=np.identity(sizemyA[0]);
    i=0;
    while i < sizemyA[0]-1 :
        tt=abs(exA[i:sizemyA[0],i:sizemyA[1]]);
        minA = tt[np.nonzero(tt)].min();
        sizeA = exA[i:sizemyA[0],i:sizemyA[1]].shape;
        # for sparse matrix, there can be improved.
        if abs(exA[i:sizemyA[0],i:sizemyA[1]]%minA).sum()==0:#minA divides all elements
            rcA = ind2rc(sizeA,tt[np.nonzero(tt)].argmin())
            exA[[i,rcA[0]+i]] = exA[[rcA[0]+i,i]];
            exA=exA.transpose();
            exA[[i,rcA[1]+i]] = exA[[rcA[1]+i,i]];
            exA=exA.transpose();
            print('find the pivot,move to left-top corner:')
            print(exA)
            for kk in range(sizeA[0]-1):
                print('row_{} mines {}*row_{}:'.format(kk+1+i,int(exA[kk+1+i,i]/exA[i,i]),i))
                exA[kk+1+i,:]=exA[kk+1+i,:]-exA[kk+1+i,i]/exA[i,i]*exA[i,:];
                print(exA)
            for kk in range(sizeA[1]-1):
                print('col_{} mines {}*col_{}:'.format(kk+1+i,int(exA[i,kk+1+i]/exA[i,i]),i))
                exA[:,kk+1+i]=exA[:,kk+1+i]-exA[i,kk+1+i]/exA[i,i]*exA[:,i];
                print(exA)
            i+=1;
        else:
            p=int((exA[i,i]-exA[i,i]%exA[i+1,i])/exA[i+1,i]);
            if exA[i,i]-p*exA[i+1,i]>0:
                exA[i,:]=exA[i,:]-p*exA[i+1,:];
            else:
                exA[i,:]=-exA[i,:]+p*exA[i+1,:];
            print('row_{} mines p*row_{}'.format(i,i+1));
            print(exA);
    if exA[i,i]==0:
        sind=abs(exA[i,:sizemyA[1]]).argmax();
        exA=exA.transpose();
        exA[[i,sind]] = exA[[sind,i]];
        exA=exA.transpose();
        print('swaping:');
        print(exA);
        if exA[i,sind]<0:
            exA[:,i]=-exA[:,i];
            print('col_{} multipe by -1'.format(i));
            print(exA);
    print('final result');
    if transind==1:
        print(exA.transpose());
        return exA.transpose();
    else:
        print(exA)
        return exA
    
# following are examples.   
myA = np.array([[1,4,2],[0,1,2],[1,3,0],[2,3,-1]]);
# assuming nr<=nc
Smith(myA)
    

        