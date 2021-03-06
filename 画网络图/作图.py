import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=Axes3D(fig)
x=np.arange(-10,10,0.2)
y=np.arange(-10,10,0.2)
x,y=np.meshgrid(x,y)
z=x+y**2
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
ax.contourf(x,y,z,zdir='z',offset=-2,cmap='rainbow')
plt.show()