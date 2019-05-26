import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img=mpimg.imread('bestimg.jpg')
ax1=plt.subplot(121)
ax1.imshow(img)
ax2=plt.subplot(122)
ax2.hist(img.ravel(),bins=1000)

plt.show()