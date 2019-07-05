from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import socket

iris=load_iris()
clf=RandomForestClassifier(n_estimators=20,bootstrap=True,oob_score=True)
clf.fit(iris.data,iris.target)
print(clf.oob_score_)