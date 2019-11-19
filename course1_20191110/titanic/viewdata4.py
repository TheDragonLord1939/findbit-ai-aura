# -*- coding: utf-8 -*-

# 这个ipython notebook主要是我解决Kaggle Titanic问题的思路和过程
# (1)
import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )
import matplotlib.pyplot as plt
#data_train = pd.read_csv("Train.csv")
data_train = pd.read_csv("../data/train.csv")
print(data_train.columns)

# (6)
#看看各登录港口的获救情况
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数
Survived_0 = data_train.Embarked[data_train.Survived == 0].value_counts()
Survived_1 = data_train.Embarked[data_train.Survived == 1].value_counts()
df=pd.DataFrame({u'Survived':Survived_1, u'Not survived':Survived_0})
df.plot(kind='bar', stacked=True)
plt.title(u"Rescue status for each embark")
plt.xlabel(u"Embark")
plt.ylabel(u"count")
plt.show()
