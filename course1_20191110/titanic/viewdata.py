# -*- coding: utf-8 -*-
import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
pd.set_option('display.max_columns', None) # 显示所有DataFrame列

#data_train = pd.read_csv("Train.csv")
data_train = pd.read_csv('../data/train.csv')
print(data_train.columns)
#data_train[data_train.Cabin.notnull()]['Survived'].value_counts()

# (2)
print(data_train.info())

# (3)
print(data_train.describe())
