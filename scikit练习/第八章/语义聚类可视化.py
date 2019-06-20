from sklearn.datasets import fetch_20newsgroups

twenty_train=fetch_20newsgroups(subset='train',download_if_missing=True)
sentences=[]
for doc in twenty_train:
    sentence=[word for word in doc if word.isdigit()]
    sentences.append(sentence)
print(len(sentences))
# print(sentences)
from gensim.models.word2vec import Word2Vec

model=Word2Vec(sentences,size=10,window=10,min_count=200,workers=4)
vocab=list(model.wv.vocab)
X=model[vocab]

from sklearn.manifold import TSNE
tsne=TSNE(n_components=2)
X_tsne=tsne.fit_transform(X)

import matplotlib.pyplot as plt
from adjustText import adjust_text

fig,ax=plt.subplot()
plt.plot(X_tsne[:,0],X_tsne[:,1],vocab)
texts=[]
for x,y,s in zip(X_tsne[:,0],X_tsne[:,1],vocab):
    texts.append(plt.text(x,y,s))
adjust_text(texts,arrowprops=dict(arrowstyle='->',color='red'))
plt.show()