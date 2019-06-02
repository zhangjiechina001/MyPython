import matplotlib.image as imp
import matplotlib.pyplot as plt
import cv2

src=imp.imread('afterCutImg.png')
src=cv2.cvtColor(src,cv2.COLOR_GRAY2RGB)
# src=src[20:80,:]
plt.imshow(src)
plt.xlabel('w',fontproperties='SimHei',fontsize=15)
plt.ylabel('h',fontproperties='SimHei',fontsize=15)
plt.xticks([])
plt.yticks([])
plt.show()