import datetime
import numpy as np
from matplotlib import cm,pyplot as plt
from matplotlib.dates import DayLocator
from hmmlearn.hmm import GaussianHMM

def load_samples_stock():
    import csv
    ret=[]
    with open('CSV.csv',newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for idx,row in enumerate(reader):
            ret.append((datetime.datetime.strptime(row['Date'], '%Y-%m-%d'),float(row['Close']),float(row['Volume'])))
    return ret

quote=load_samples_stock()
dates=np.array([q[0] for q in quote],dtype=datetime.datetime)[1:]
close_v=np.array([q[1] for q in quote])
volume=np.array([q[2] for q in quote])[1:]

diff=np.diff(close_v)

X=np.column_stack([diff,volume])
model=GaussianHMM(n_components=3,covariance_type='diag',n_iter=5000)
model.fit(X)

print('Model means:%s'%(model.means_))#平跌涨
print('Model Covariance is %s'%(model.covars_))
print('Model Trans is \n %s '%(model.transmat_))
X=X[-26:]
dates=dates[-26:]
close_v=close_v[-26:]
hidden_states=model.predict(X)