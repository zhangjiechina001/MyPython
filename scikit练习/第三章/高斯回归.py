import numpy as np
from matplotlib import pyplot as plt

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import ConstantKernel as C,Product,Sum

def f(X):
    return X*np.sin(X)-3*X

X=np.linspace(0,10,20)
y=f(X)+np.random.normal(0,0.5,X.shape[0])
x=np.linspace(0,10,200)

kernel=Product(C(0.1),RBF(10,(1e-2,1e2)))

gp=GaussianProcessRegressor(kernel=kernel,n_restarts_optimizer=3,alpha=0.3)
gp.fit(X.reshape(-1,1),y)

y_pred,sigma=gp.predict(x.reshape(-1,1),return_std=True)

fig=plt.figure()
plt.plot(x,f(x),'r:',label=u'$f(x)=x\,\sin(x)-3x$')
plt.plot(X,y,'r.',markersize=10,label=u'Observations')
plt.plot(x,y_pred,'b-',label=u'Prediction')
plt.fill(np.concatenate([x,x[::-1]]),np.concatenate([y_pred-2*sigma,(y_pred+2*sigma)[::-1]]),alpha=.3,fc='b',label='95% confidence')
plt.legend(loc='lower left')
plt.show()