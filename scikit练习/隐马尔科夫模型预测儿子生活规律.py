import numpy as np
import csv
from sklearn.datasets import fetch_20newsgroups
twenty_train=fetch_20newsgroups(subset='train')
emission_probability=np.array([[0.4,0.3,0.3]#晴的隐藏状态：0.4打球，0.3读书，0.3访友
                                  ,[0.2,0.3,0.5],#阴的隐藏状态是：0.2打球，0.3读书，0.5访友
                               [0.1,0.8,0.1]])#雨的隐藏状态是：0.1打球，0.8读书，0.1访友

transition_probabilty=np.array([[0.7,0.2,0.1],#晴天：晴0.6，阴0.2，雨0.1
                                [0.3,0.5,0.2],#阴天：晴0.3，阴0.5，雨0.2
                                [0.3,0.4,0.3]])#雨天：晴0.3，阴0.4，雨0.3

start_probability=np.array([0.5,0.2,0.3])
from hmmlearn import hmm
model=hmm.MultinomialHMM(n_components=3)
model.startprob_=start_probability
model.transmat_=transition_probabilty
model.emissionprob_=emission_probability
dic=[]
dic.append('晴天')
dic.append('阴天')
dic.append('雨天')
observer=[]
observer.append('打球')
observer.append('读书')
observer.append('访友')

observerstr=[]
predictstr=[]
observe_chain=np.array([0,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,0]).reshape(-1,1)
predict=model.predict(observe_chain)
print(predict)
temp=[0,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,0]
for i in list(predict):
    predictstr.append(dic[i])
    # predictstr.append(dic[j])
for i in temp:
    observerstr.append(observer[i])
    # predictstr.append(dic[j])
print('显示层：',observerstr)
print('预测层：',predictstr)
print(model.score(observe_chain))