# -*- coding: utf-8 -*-

import numpy as np
import scipy
import sympy as sym
import matplotlib
sym.init_printing()

print("NumPy version:", np.__version__)
print("SciPy version:", scipy.__version__)
print("SymPy version:", sym.__version__)
print("Matplotlib version:", matplotlib.__version__)

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

mpl.style.use('seaborn-darkgrid')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1 = np.linspace(1, 3, 20)
x2 = np.linspace(2, 4, 20)
x1, x2 = np.meshgrid(x1, x2)

z = x1 ** 2 + x2 ** 2 - 4 * x1 - 6 * x2

ax.plot_surface(x1, x2, z, rstride=1, cstride=1)
ax.contourf(x1, x2, z, zdir='z', offset=-13)

u = 2 * x1 - 4
v = 2 * x2 - 6

fig = plt.figure(2)
plt.quiver(x1, x2, -u, -v)
plt.show()

# 最速下降法
def func(x, y):
    return x**2+3*y**2-4*x-6*y
def dfunc(x, y):
    return 2*x-4, 6*y-6


x, y = 0, 0
for itr in range(200):
    gx, gy = dfunc(x, y)
    x+=-0.01*gx
    y+=-0.01*gy
    if(itr%20==0):
        print("%.f %.5f %.5f"%(x, y, func(x, y)))

x, y = 0, 0
x1 = np.linspace(0,4,20)
x2 = np.linspace(0,4,20)
x1,x2=np.meshgrid(x1,x2)
u, v = dfunc(x1, x2)
plt.quiver(x1,x2,-u,-v)
for itr in range(200):
    gx, gy = dfunc(x, y)
    xo,yo=x,y
    x+=-0.1*gx
    y+=-0.1*gy
    plt.plot([xo,x],[yo,y])
    plt.scatter([xo],[yo])
    if(itr%20==0):
        print("%.f %.5f %.5f"%(x, y, func(x, y)))

def func3(x, y):
    return 4 + x**2 - 2 * y + 2*y**2 - x*2 - x*y
def dfunc3(x, y):
    return 2*x-y-2, 4*y-x-2

x, y = 2.5, 4
x1 = np.linspace(0,4,20)
x2 = np.linspace(0,4,20)
x1,x2=np.meshgrid(x1,x2)
u, v = dfunc3(x1, x2)
plt.quiver(x1,x2,-u,-v)
for itr in range(200):
    gx, gy = dfunc3(x, y)
    xo,yo=x,y
    x+=-0.1*gx
    y+=-0.1*gy
    plt.plot([xo,x],[yo,y])
    plt.scatter([xo],[yo])
    if(itr%20==0):
        print("%.f %.5f %.5f"%(x, y, func3(x, y)))

def func2(x, y):
    return x*(x-1)*(x-2)*(x-3)*y*(y-1)*(y-2)*(y-3)
def dfunc2(x, y):
    return 2*(-3 + 11*x - 9*x**2 + 2*x**3)*(-3 + y)*(-2 + y)*(-1 + y)*y, 2*(-3 + x)*(-2 + x)*(-1 + x)*x*(-3 + 11*y - 9*y**2 + 2*y**3)

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
x1 = np.linspace(-0,3.5,40)
x2 = np.linspace(-0,3.5,40)
x1,x2=np.meshgrid(x1,x2)

z=func2(x1, x2)

ax.plot_surface(x1, x2, z, rstride=1, cstride=1)
ax.contourf(x1, x2, z, zdir='z', offset=-13)
ax.set_zlim3d(-2, 2)
fig = plt.figure(2)
x, y = 2., 1.5
x1 = np.linspace(0,3,20)
x2 = np.linspace(0,3,20)
x1,x2=np.meshgrid(x1,x2)
u, v = dfunc2(x1, x2)
plt.quiver(x1,x2,-u,-v)
for itr in range(200):
    gx, gy = dfunc2(x, y)
    xo,yo=x,y
    x+=-0.01*gx
    y+=-0.01*gy
    plt.plot([xo,x],[yo,y])
    plt.scatter([xo],[yo])
    if(itr%20==0):
        print("%.f %.5f %.5f"%(x, y, func(x, y)))

# 牛顿法

def func3(x, y):
    return 4 + x**2 - 2 * y + 2*y**2 - x*2 - x*y
def dfunc3(x, y):
    return 2*x-y-2, 4*y-x-2

def Hessian(x, y):
    return np.array([[4, -1],[-1, 2]])

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
x1 = np.linspace(-0,3.5,40)
x2 = np.linspace(-0,3.5,40)
x1,x2=np.meshgrid(x1,x2)

z=func3(x1, x2)

ax.plot_surface(x1, x2, z, rstride=1, cstride=1)
ax.contourf(x1, x2, z, zdir='z', offset=-13)
#ax.set_zlim3d(-2, 2)
fig = plt.figure(2)
x, y = 2.5, 4
x1 = np.linspace(0,4,40)
x2 = np.linspace(0,4,40)
x1,x2=np.meshgrid(x1,x2)
u, v = dfunc3(x1, x2)
plt.quiver(x1,x2,-u,-v)
for itr in range(200):
    gx, gy = dfunc3(x, y)
    H = Hessian(x, y)
    iH=np.linalg.inv(H)
    v=np.array([[gx],[gy]])
    hg=np.dot(iH, v)
    gx, gy = hg[0,0], hg[1, 0]
    xo,yo=x,y
    x+=-0.1*gx
    y+=-0.1*gy
    plt.plot([xo,x],[yo,y])
    plt.scatter([xo],[yo])
    if(itr%20==0):
        print("%.f %.5f %.5f"%(x, y, func3(x, y)))

# 高斯牛顿法
def func3(x, y):
    return 4 + x**2 - 2 * y + 2*y**2 - x*2 - x*y
def dfunc3(x, y):
    return 2*x-y-2, 4*y-x-2
def J(x, y):
    return np.array([[2*x-y-2, 4*y-x-2]])

fig = plt.figure(2)
x, y = 2.5, 4
x1 = np.linspace(0,4,40)
x2 = np.linspace(0,4,40)
x1,x2=np.meshgrid(x1,x2)
u, v = dfunc3(x1, x2)
plt.quiver(x1,x2,-u,-v)
for itr in range(200):
    gx, gy = dfunc3(x, y)
    fj=J(x,y)
    H = np.dot(fj.T,fj)
    iH=np.linalg.inv(H+0.3*np.eye(2))
    v=np.array([[gx],[gy]])
    hg=np.dot(iH, fj.T)*func3(x, y)
    gx, gy = hg[0,0], hg[1, 0]
    xo,yo=x,y
    x+=-0.1*gx
    y+=-0.1*gy
    plt.plot([xo,x],[yo,y])
    plt.scatter([xo],[yo])
    if(itr%20==0):
        print("%.f %.5f %.5f"%(x, y, func3(x, y)))
        