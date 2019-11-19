# -*- coding: utf-8 -*-

import numpy as np
import math


# 信息熵
pro = [4.0, 3.0, 2.0]
proEntropy = []










for i in pro:
    p = i / np.sum(pro)
    proEntropy.append(- p * np.log2(p))

print (np.sum(proEntropy))
z = 1
exit()


# 条件熵
pro = [[4.0, 1.0],[],[]]

exit()

from math import log

#创建简单数据集
def creatDataset():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    dataSet = [[1,1,'yes'],[1,1,'yes'],[0,1,'no'],[0,1,'no']]

    labels = ['no surfacing','flippers']
    return dataSet,labels

#计算信息熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for vec in dataSet:
        currentLabel = vec[-1]
        if currentLabel not in labelCounts.keys():  #为所有可能的分类建立字典
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

#简单测试
myDat,labels = creatDataset()
print (myDat)
print (calcShannonEnt(myDat))