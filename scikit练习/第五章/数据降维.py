import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

n_row,n_Col=2,4
n_components=n_row*n_Col
imae_shape=(64,64)

dataset=fetch_olivetti_faces(shuffle=True)#在线下载Olovetti人脸库

faces=dataset.data
n_samples,n_features=faces.shape#样本数，样本维度
faces-=faces.mean(axis=1).reshape(n_samples,-1)

#图像绘制函数
def plot_gallery(title,image,n_col=n_Col,n_row=n_row):
    plt.figure(figsize=(2.*n_Col,2.26*n_row))
    plt.suptitle(title,size=16)

    for i,comp in enumerate( ):
        plt.subplot(n_row,n_Col,i+1)
        vmax=max(comp.max(),-comp.min())
        plt.imshow(comp.reshape(imae_shape),cmap=plt.cm.gray,interpolation='nearest',vmin=-vmax,vmax=vmax)
        plt.xticks(())
        plt.yticks(())
plt.subplots_adjust(0.01,0.05,0.99,0.93,0.04,0.)
plot_gallery('Olivetti faces',faces[5:5+n_components])
#whiten去除一些信息，提高准确率
estimator=decomposition.PCA(n_components=n_components,svd_solver='randomized',whiten=True)
estimator.fit(faces)
plot_gallery('Eigen faces',estimator.components_[:n_components])
plt.show()