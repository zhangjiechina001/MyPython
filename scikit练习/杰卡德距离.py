from numpy import *
import scipy.spatial.distance as dist
matV = mat([[1,1,1,1],[1,0,0,1]])
print( dist.pdist(matV,'jaccard'))