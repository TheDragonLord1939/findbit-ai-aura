from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import Lasso, LogisticRegression, LinearRegression
from sklearn.datasets import load_iris
iris = load_iris()
#GBDT作为基模型的特征选择
#print(SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target))
selector = SelectFromModel(GradientBoostingClassifier(), threshold="mean").fit(iris.data, iris.target)
# selector = SelectFromModel(GradientBoostingClassifier(), threshold="1.4*mean").fit(iris.data, iris.target)
# 随机森林
# selector = SelectFromModel(RandomForestClassifier(), threshold="mean").fit(iris.data, iris.target)
# L1正则的线性模型
# selector = SelectFromModel(Lasso(), threshold=1e-5).fit(iris.data, iris.target)
print(iris.data[0:5])
data = selector.transform(iris.data)
print(data[0:5])
if hasattr(selector.estimator_, 'feature_importances_'):
    print("feature importances:", selector.estimator_.feature_importances_)
else:
    print("coef:", selector.estimator_.coef_)
