#coding: UTF-8
# 信息利用率低：不同的机器学习算法和模型对数据中信息的利用是不同的，之前提到在线性模型中，使用对定性特征哑编码可以达到非线性的效果。类似地，对定量变量多项式化，或者进行其他的转换，都能达到非线性的效果。

import numpy as np
from sklearn.preprocessing import OneHotEncoder
data = np.array([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
print(data)
enc = OneHotEncoder()
enc.fit(data)
print(enc.n_values_)
print(enc.feature_indices_)
print(enc.transform([[0, 1, 1]]).toarray())
