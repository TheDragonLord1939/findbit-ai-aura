# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

np.random.seed(0)  # seed()用于指定随机数生成时所用算法开始的整数值。
mean, cov, n = [0, 0], [[1, 1], [1, 1.5]], 10  # 设置多元随机数生成的均值，协方差矩阵，生成点个数
x = np.random.multivariate_normal(mean, cov, n)  # 随机数生成
print (x)
''''' 
x值 
[[-0.2314987   0.08387106] 
 [ 0.66963671  1.38535319] 
 [ 0.97355908  0.04134561] 
 [ 0.38108224  0.9434845 ] 
 [ 0.11467758 -0.72613803]] 
'''
pca = PCA(n_components=2)
#pca = mlpy.PCA()  # 定义算法训练器pca
pca.fit(x)  # 给pca算法输入值，训练模型
coeff = pca.components_  # 获取模型训练结果的参数
''''' 
coef系数值 
[[-0.6165097  -0.78734731] 
 [-0.78734731  0.6165097 ]] 
'''

fig = plt.figure(1)  # 创建figure对象fig
plot1 = plt.plot(x[:, 0], x[:, 1], 'o')  # x[:, 0]相当于x,x[:, 1]相当于y 'o'为绘制散点图
plot2 = plt.plot([0, coeff[0, 0]], [0, coeff[1, 0]], linewidth=4, color='r')  # 主成分分量1，标红线
plot3 = plt.plot([0, coeff[0, 1]], [0, coeff[1, 1]], linewidth=4, color='g')  # 主成分分量2，标绿线
xx = plt.xlim(-4, 4)
yy = plt.ylim(-4, 4)

pca = PCA(n_components=1)
pca.fit(x)
z = pca.transform(x)  # 设置主成分的个数
print (z)
plt.show()
exit()
xnew = pca.inverse_transform(z)
fig2 = plt.figure(2)  # 创建figure对象fig2
plot1 = plt.plot(xnew[:, 0], xnew[:, 1], 'o')
xx = plt.xlim(-4, 4)
yy = plt.ylim(-4, 4)
plt.show()  # 会同时显示2个图