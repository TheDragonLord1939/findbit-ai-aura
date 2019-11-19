# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.animation as animation
import numpy as np

import matplotlib.image as mpimg # mpimg 用于读取图片
img = mpimg.imread('img/jin.jpg')
img = img[:560, :560, :]/255.0


print(np.shape(img))
plt.imshow(img)
plt.show()

a1, a2, a3 = 0.2989, 0.5870, 0.1140
img_gray = img[:,:,0]*a1+img[:,:,1]*a2+img[:,:,2]*a3
plt.imshow(img_gray, cmap=plt.get_cmap("gray"))
plt.show()

from numpy import linalg as LA
U, A, V = np.linalg.svd(img_gray, full_matrices=True)
Lambda=np.diag(A)

re_img=U.dot(Lambda).dot(V)

plt.imshow(np.real(re_img), cmap=plt.get_cmap("gray"))
plt.show()

dim = 100

re_img1=U[:,:dim].dot(Lambda[:dim,:dim]).dot(V[:dim,:])
plt.imshow(np.real(re_img1), cmap=plt.get_cmap("gray"))
plt.show()
