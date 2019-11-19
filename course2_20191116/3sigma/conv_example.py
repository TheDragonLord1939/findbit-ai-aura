# -*- coding: utf-8 -*-
"""
@author: 蔚蓝的天空Tom
Talk is cheap, show me the code
Aim：计算两个维度的协方差covariance
"""

import numpy as np


class CCovariance(object):
    '''计算X,Y这俩维度的协方差
    '''

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

        self.Covariance_way1()
        self.Covariance_way2()
        self.Covariance_way3()

    def Covariance_way1(self):
        '''
        协方差公式法计算两个等长向量的协方差convariance
        '''
        X, Y = np.array(self.X), np.array(self.Y)
        meanX, meanY = np.mean(X), np.mean(Y)
        n = np.shape(X)[0]
        # 按照协方差公式计算协方差，Note:分母一定是n-1
        # multiply: 数组和矩阵对应位置相乘，输出与相乘数组/矩阵的大小一致
        covariance = sum(np.multiply(X - meanX, Y - meanY)) / (n - 1)
        print('协方差公式法求得的协方差:', covariance)
        return covariance

    def Covariance_way2(self):
        '''
        向量中心化方法计算两个等长向量的协方差convariance
        '''
        X, Y = np.array(self.X), np.array(self.Y)
        n = np.shape(X)[0]
        centrX = X - np.mean(X)
        centrY = Y - np.mean(Y)
        convariance = sum(np.multiply(centrX, centrY)) / (n - 1)
        print('向量中心化方法求得协方差:', convariance)
        return convariance

    def Covariance_way3(self):
        '''
        numpy.conv(X,Y)提供的协方差函数求协方差
        '''
        conv = np.cov(self.X, self.Y)
        print('np.cov(X,Y)求得的X的方差:', conv[0, 0])
        print('np.cov(X,Y)求得的Y的方差:', conv[1, 1])
        print('np.cov(X,Y)求得的X和Y的协方差:', conv[0, 1])


if __name__ == '__main__':
    X = [10, 15, 23, 11, 42, 9, 11, 8, 11, 21]
    Y = [15, 46, 21, 9, 45, 48, 21, 5, 12, 20]
    c = CCovariance(X, Y)
