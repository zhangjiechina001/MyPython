import numpy as np
from hmmlearn import hmm
import tensorflow as tf
weight=tf.Variable(tf.random_normal([2,3],mean=0.3,stddev=0.1))

init_probs=np.array([0.5,0.8,0.5])
transform_probd=np.array([[0.7,0.2,0.1],[0.2,0.5,0.3],[0.2,0.4,0.4]])
chanin=[init_probs]
def chech_stable():
    if len(chanin)<3:
        return False
    for i in range(-2,-1):
        if not np.array_equal(np.around(chanin[i],2),np.around(chanin[i-1],2)):
            return False
        return True

for i in range(1000):
    chanin.append(chanin[0].dot(transform_probd))
    print('iter %s:%s'%(i,np.around(chanin[-1],2)))
    # if chech_stable():
    #     #     print('stabled!')
    #     #     break