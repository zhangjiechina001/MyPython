import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

label_font = {
    'color': 'c',
    'size': 15,
    'weight': 'bold'
}


def randrange(n, vmin, vmax):
    r = np.random.rand(n)  # 随机生成n 个介于0-1之间的数
    return (vmax - vmin) * r + vmin  # 得到n个[vmin，vmax]之间的随机数


fig = plt.figure(figsize=(16, 12))  # 参数依然是图片大小
ax = fig.add_subplot(111, projection='3d')  # 确定子坐标轴，111表示1行1列的第一个图   要同时画好几个图的时候可以用这个

# 准备数据
n = 200
for zlow, zhigh, c, m, l in [(4, 15, 'r', 'o', 'posirtive'),
                             (13, 40, 'g', '*', 'negative')]:  # 用两个tuple（画笔）,是为了将形状和颜色区别开来
    x = randrange(n, 15, 40)
    y = randrange(n, -5, 25)
    z = randrange(n, zlow, zhigh)
    ax.scatter(x, y, z, c=c, marker=m, label=l, s=z * 10)  # marker的尺寸和z的大小成正比

ax.set_xlabel("X axis", fontdict=label_font)
ax.set_ylabel("Y axis", fontdict=label_font)
ax.set_zlabel("Z axis", fontdict=label_font)
ax.set_title("Scatter plot", alpha=0.6, color="b", size=25, weight='bold', backgroundcolor="y")  # 子图（其实就一个图）的title
ax.legend(loc="upper left")  # legend的位置位于左上

plt.show()


