from  sklearn.naive_bayes import  BernoulliNB

clf=BernoulliNB(binarize=1)
X=[[0.23,0.2],[1.1,1.3],[1.2,2.1]]
y=[0,1,1]
clf.fit(X,y)
predict=clf.predict([[1.0,1.1]])
print(predict)