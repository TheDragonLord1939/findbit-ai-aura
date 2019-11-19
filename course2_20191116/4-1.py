# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.animation as animation
import numpy as np

mpl.style.use('seaborn-paper')
def linediv(x,y):
    if(x+y<0.5):
        return '+'
    elif(x+y>1.5):
        return '+'
    else:
        return 'o'
line = np.linspace(0,1,101)
tr = np.diag(np.linspace(0,1,11))  #  Extract a diagonal or construct a diagonal array.
matx = np.matmul(tr,np.ones([11,101]))-0.5
maty = np.ones([11,101])*line-0.5
def sigmoid(rt):
    return 1/(1+np.exp(-rt))
def space_tor(xx,yy):
    mx=[]
    my=[]
    for x,y in zip(xx,yy):
        mat=np.array([[1.5,0.5],
                      [0.5,1.5]])
        cst=np.array([0,  0])
        re=np.matmul(np.array([x,y]),mat)
        mx.append(re[0])
        my.append(re[1])
    return np.array(mx),np.array(my)

for itr in range(len(matx)):
    xx1,yy1 = space_tor(matx[itr],maty[itr])
    xx2,yy2 = space_tor(maty[itr],matx[itr])
    cont=0
    for x1,x2,x3,x4 in zip(xx1,yy1,matx[itr],maty[itr]):
        if(cont%20==0):
            mk = linediv(x3,x4)
            plt.plot([x1,x3],[x2,x4],alpha=0.05,c='k')
            plt.scatter([x1],[x2],marker=mk,s=40,c='r',alpha=0.6)
            plt.scatter([x3],[x4],marker=mk,s=40,alpha=0.6)
        cont+=1
    xx1,yy1 = space_tor(matx[itr],maty[itr])
    xx2,yy2 = space_tor(maty[itr],matx[itr])
    plt.plot(matx[itr],maty[itr],c='r',alpha=0.15)
    plt.plot(maty[itr],matx[itr],c='r',alpha=0.15)
    plt.plot(xx1,yy1,c='b',alpha=0.15)
    plt.plot(xx2,yy2,c='b',alpha=0.15)
plt.show()