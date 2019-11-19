"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
from sklearn import svm
from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
print(X)
print(y)
clf.fit(X, y)

# method 1: pickle
import pickle
# save
# with open('a4_model_load/model/save/clf.pickle', 'wb') as f:
with open('save/clf.pickle', 'wb') as f:
    pickle.dump(clf, f)
# restore
# with open('a4_model_load/model/save/clf.pickle', 'rb') as f:
with open('save/clf.pickle', 'rb') as f:
   clf2 = pickle.load(f)
   print(clf2.predict(X[0:1]))

# method 2: joblib
from sklearn.externals import joblib
# Save
# joblib.dump(clf, 'a4_model_load/model/save/clf.pkl')
joblib.dump(clf, 'save/clf.pkl')
# restore
# clf3 = joblib.load('a4_model_load/model/save/clf.pkl')
clf3 = joblib.load('save/clf.pkl')
print(clf3.predict(X[0:1]))