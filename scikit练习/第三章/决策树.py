
# -*-coding:utf-8-*-
from sklearn import tree
import pydotplus

X=[[20,30000,400],[37,13000,0],[50,26000,0],[28,10000,3000],[31,19000,1500000],[46,7000,6000]]
Y=[1,0,0,0,1,0]
clf=tree.DecisionTreeClassifier(criterion='gini')
clf=clf.fit(X,Y)
predict=clf.predict([[40,6000,100]])
print(predict)
import graphviz
# decode("utf-8").encode("gbk")
from sklearn.externals.six import StringIO
# dot_data=StringIO()
dot_data=tree.export_graphviz(clf,out_file=None,feature_names=[u'年龄',u'收入',u'存款'],class_names=[u'普通',u'VIP'],filled=True,rotate=True)
graph=graphviz.Source(dot_data)
graph.render('mytree01')
# graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf('mytree.pdf')
# dot -Tpng E:\MyPython\scikit练习\第三章\mytree01 -o E:\MyPython\scikit练习\第三章\example.png