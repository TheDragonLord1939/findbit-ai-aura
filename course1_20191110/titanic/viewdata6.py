# -*- coding: utf-8 -*-

# 这个ipython notebook主要是我解决Kaggle Titanic问题的思路和过程
# (1)
import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )
import matplotlib.pyplot as plt
#data_train = pd.read_csv("Train.csv")
data_train = pd.read_csv("../data/train.csv")
print(data_train.columns)

#看看各性别的获救情况
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数

Survived_m = data_train.Survived[data_train.Sex == 'male'].value_counts()
Survived_f = data_train.Survived[data_train.Sex == 'female'].value_counts()
df=pd.DataFrame({u'男性':Survived_m, u'女性':Survived_f})
df.plot(kind='bar', stacked=True)
plt.title(u"Rescue status for each gender")
plt.xlabel(u"Gender")
plt.ylabel(u"count")
plt.show()
