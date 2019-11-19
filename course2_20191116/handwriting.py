import numpy as np

data = np.load("MNIST_data/train.npz")
batch_xs, batch_ys = data["images"][:6000,:], data["labels"][:6000,:]
U, A, V = np.linalg.svd(batch_xs, full_matrices=True)

m=np.shape(U)[0]
n=np.shape(V)[0]
mn = np.min([m, n])
Lambda = np.zeros([m, n])
print(m)
Lambda[:30,:30] = np.diag(A)[:30,:30]

A

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
mpl.style.use('seaborn-darkgrid')

plt.scatter(U[:,1],U[:,2])
plt.show()

# SVD U矩阵
colors=['aliceblue',
'aquamarine',
'azure',
'beige',
'bisque',
'black',
'blanchedalmond',
'blue',
'blueviolet',
'brown',
'burlywood',
'cadetblue']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
UL=np.dot(U, Lambda)
for itr in range(10):
    ax.scatter(UL[batch_ys[:,itr]==1,0],
               UL[batch_ys[:,itr]==1,1],
               UL[batch_ys[:,itr]==1,2],
               color=colors[itr],
              label="N:%d"%itr)
plt.legend()
plt.show()
input("Press Enter to continue...")

# 前三十维
m=np.shape(U)[0]
n=np.shape(V)[0]
mn = np.min([m, n])
Lambda = np.zeros([m, n])
print(m)
Lambda[:30,:30] = np.diag(A)[:30,:30]

NEW=np.dot(U, np.dot(Lambda, V))
fig = plt.figure()
for itrx in range(3):
    for itry in range(3):
        for itmg, itlb in zip(NEW, batch_ys):
            la=np.where(itlb==np.max(itlb))[0][0]
            if(la==itrx*3+itry+1):
                ax=fig.add_subplot(3,3,la)
                ax.imshow(np.reshape(itmg,[28,28]))
                plt.text(0,0,"label:%d"%la)
                plt.xticks([])
                plt.yticks([])
                break
plt.show()

np.shape(V)
# V 重构
fig = plt.figure()
ax=[]
for itr in range(1,82):
    ax.append(fig.add_subplot(9,9,itr))
for idx, itmg in enumerate(V[:81,:]):
    ax[idx].imshow(np.reshape(itmg,[28,28]))
plt.show()
input("Press Enter to continue...")


NEW=np.dot(U, np.dot(Lambda, V))
fig = plt.figure()
ax=[]
for itr in range(1,10):
    ax.append(fig.add_subplot(3,3,itr))
for itmg, itlb in zip(np.dot(U,Lambda)[:,:30], batch_ys):
    la=np.where(itlb==1)[0][0]
    ax[la-1].plot(itmg)
plt.show()

input("Press Enter to continue...")

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn-darkgrid')
from sklearn import datasets
from sklearn.decomposition import PCA

pca = PCA(n_components=10)
X_r = pca.fit(batch_xs).transform(batch_xs)

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
mpl.style.use('seaborn-darkgrid')


colors=['aliceblue',
'aquamarine',
'azure',
'beige',
'bisque',
'black',
'blanchedalmond',
'blue',
'blueviolet',
'brown',
'burlywood',
'cadetblue']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for itr in range(10):
    ax.scatter(X_r[batch_ys[:,itr]==1,0],
               X_r[batch_ys[:,itr]==1,1],
               X_r[batch_ys[:,itr]==1,2],
               color=colors[itr],
              label="N:%d"%itr)
plt.legend()
plt.show()
input("Press Enter to continue...")


fig = plt.figure()
ax=[]
for itr in range(1,10):
    ax.append(fig.add_subplot(3,3,itr))
for itmg, itlb in zip(X_r, batch_ys):
    la=np.where(itlb==1)[0][0]
    ax[la-1].plot(itmg)
plt.show()
input("Press Enter to continue...")


data = np.load("MNIST_data/train.npz")
batch_xs, batch_ys = data["images"][:6000,:], data["labels"][:6000,:]
array1=batch_xs[batch_ys[:,1]==1]
array2=batch_xs[batch_ys[:,2]==1]
array=np.concatenate([array1,array2],axis=0)
print(len(array1),len(array2))


import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn-darkgrid')

pca = PCA(n_components=3)
X_r = pca.fit(array).transform(array)

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
mpl.style.use('seaborn-darkgrid')
fig = plt.figure()
ax = fig.add_subplot(111)
len1=len(array1)
ax.scatter(X_r[len1:,0],X_r[len1:,1],color="brown",label="1")
ax.scatter(X_r[:len1,0],X_r[:len1,1],color="blue",label="2")
plt.legend()
plt.show()
input("Press Enter to continue...")


import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
mpl.style.use('seaborn-darkgrid')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
len1=len(array1)
ax.scatter(X_r[len1:,0],X_r[len1:,1],X_r[len1:,2],color="brown")
ax.scatter(X_r[:len1,0],X_r[:len1,1],X_r[:len1,2],color="blue")
plt.show()
input("Press Enter to continue...")
