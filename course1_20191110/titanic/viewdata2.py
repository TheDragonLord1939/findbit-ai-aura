# -*- coding: utf-8 -*-

# 这个ipython notebook主要是我解决Kaggle Titanic问题的思路和过程
# (1)
import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame


#data_train = pd.read_csv("Train.csv")
data_train = pd.read_csv('../data/train.csv')

print(data_train.columns)
#data_train[data_train.Cabin.notnull()]['Survived'].value_counts()

# (2)

print(data_train.info())

# (3)
print(data_train.describe())

# (4)
#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )
import matplotlib.pyplot as plt
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数

plt.subplot2grid((2,3),(0,0))             # 在一张大图里分列几个小图
data_train.Survived.value_counts().plot(kind='bar')# plots a bar graph of those who surived vs those who did not.
plt.title(u"Rescue (1 for rescued)") # puts a title on our graph
plt.ylabel(u"count")

plt.subplot2grid((2,3),(0,1))
data_train.Pclass.value_counts().plot(kind="bar")
plt.ylabel(u"count")
plt.title(u"passenger distribution")

plt.subplot2grid((2,3),(0,2))
plt.scatter(data_train.Survived, data_train.Age)
plt.ylabel(u"Age")                         # sets the y axis lable
plt.grid(b=True, which='major', axis='y') # formats the grid line style of our graphs
plt.title(u"Age distribution (1 for rescue)")

plt.subplot2grid((2,3),(1,0), colspan=2)
data_train.Age[data_train.Pclass == 1].plot(kind='kde')   # plots a kernel desnsity estimate of the subset of the 1st class passanges's age
data_train.Age[data_train.Pclass == 2].plot(kind='kde')
data_train.Age[data_train.Pclass == 3].plot(kind='kde')
plt.xlabel(u"Age")# plots an axis lable
plt.ylabel(u"Density")
plt.title(u"Age distribution of each classes")
plt.legend((u'first', u'2nd',u'3rd'),loc='best') # sets our legend for our graph.

plt.subplot2grid((2,3),(1,2))
data_train.Embarked.value_counts().plot(kind='bar')
plt.title(u"count per embark")
plt.ylabel(u"count")
plt.show()