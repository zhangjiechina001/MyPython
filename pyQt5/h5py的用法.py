import h5py
f = h5py.File('pretectNumModel.h5', 'r')
print (list(f.keys()))
dset = f['model_weights']
dense_1 = f['/model_weights/dense_1/dense_1']
dense_1_kernel = dense_1['kernel:0'][:]
print (dense_1_kernel)