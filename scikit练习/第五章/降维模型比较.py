from time import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import  NullFormatter
from sklearn import manifold,datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

Axes3D
n_points=1000
X,color=datasets.samples_generator.make_s_curve(n_points,random_state=0)
n_neighbors=10
n_cmponents=2

fig=plt.figure(figsize=(15,8))
ax=fig.add_subplot(251,projection='3d')
ax.scatter(X[:,0],X[:,1],X[:,2],c=color,cmap=plt.cm.Spectral)
ax.view_init(4,-72)

methods=['standard','ltsa','hessian']
labels=['LLE','LTSA','Hessian LLE']

for i,method in enumerate(methods):
    t0=time()
    Y=manifold.LocallyLinearEmbedding(n_neighbors,n_cmponents,eigen_solver='auto',method=method).fit_transform(X)
    t1=time()
    print('%s:%.2g sec'%(methods[i],t1-t0))

    ax=fig.add_subplot(252+i)

    #显示降维结果
    plt.scatter(Y[:,0],Y[:,1],c=color,cmap=plt.cm.Spectral)
    plt.title('%s(%.2g sec)'%(labels[i],t1-t0))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    plt.axis('tight')

#初始化六种降维模型
estimators=[(manifold.Isomap(n_neighbors,n_cmponents),'Isomap'),(manifold.MDS(n_cmponents,max_iter=100,n_init=1),'MDS'),
            (manifold.SpectralEmbedding(n_components=n_cmponents,n_neighbors=n_neighbors),'Laplace Eigenmaps'),
            (manifold.TSNE(n_cmponents,init='pca',random_state=0),'T-SNE'),(PCA(n_cmponents),'PCA'),(LDA(n_cmponents),'LDA'),]

#训练、显示六种降维模型
for idx,(estimator_obj,estimator_name) in enumerate(estimators):
    t0=time()
    if estimator_name=='LDA':
        continue
        Y=estimator_obj.fit_transform(X,color.astype(int))
    else:
        Y=estimator_obj.fit_transform(X)

    t1=time()
    print('%s:%.2g sec'%(estimator_name,t1-t0))
    ax=fig.add_subplot(2,5,5+idx)
    #显示降维结果
    plt.scatter(Y[:,0],Y[:,1],c=color,cmap=plt.cm.Spectral)
    plt.title('%s(%.2g sec)'%(estimator_name,t1-t0))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    plt.axis('tight')

plt.show()