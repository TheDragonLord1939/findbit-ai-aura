# -*- coding: utf-8 -*-
# 加载相关模块和库
import sys
import io
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
from sklearn.model_selection import learning_curve
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
import pandas as pd #数据分析
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from util import set_Cabin_type, set_missing_ages, plot_learning_curve, one_hot_encoding
# (1) 读取数据集
data_train = pd.read_csv("data/train.csv")

# (2) 特征工程 - 处理缺失值
data_train, rfr = set_missing_ages(data_train)
data_train = set_Cabin_type(data_train)

# (3) 特特工程 - 类目型的特征离散/因子化
df = one_hot_encoding(data_train)
# select specific coloumn
train_df = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
#print(train_df.describe())
train_np = train_df.as_matrix()
# y即Survival结果
y = train_np[:, 0]
# X即特征属性值
X = train_np[:, 1:]

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(2)
print(X.shape)
X = poly.fit_transform(X)
print(X.shape)

# # (5) 模型构建与训练
clf = RandomForestClassifier(criterion='gini', max_depth=1, n_estimators=1, verbose=0)
# (6) 绘制learning curve
plot_learning_curve(clf, u"学习曲线", X, y, cv = 10)

# (5) 模型构建与训练 - 训练集精度提升明显
clf = RandomForestClassifier(criterion='gini', max_depth=30, n_estimators=1, verbose=0)
# (6) 绘制learning curve

plot_learning_curve(clf, u"学习曲线-", X, y, cv =10)

# (5) 模型构建与训练 - 可以适当减缓过拟合
clf = RandomForestClassifier(criterion='gini', max_depth=6, n_estimators=30, verbose=0)
# (6) 绘制learning curve
plot_learning_curve(clf, u"学习曲线--", X, y, cv = 10)
