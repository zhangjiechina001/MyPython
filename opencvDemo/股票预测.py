import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

date = np.linspace(1,15,15)
endPrice = np.array([2511.90,2538.26,2510.68,2591.66,2732.98,2701.69,2701.29,2678.67,2726.50,2681.50,2739.17,2715.07,2823.58,2864.90,2919.08]
)
beginPrice = np.array([2438.71,2500.88,2534.95,2512.52,2594.04,2743.26,2697.47,2695.24,2678.23,2722.13,2674.93,2744.13,2717.46,2832.73,2877.40])
print(date)
plt.figure()
for i in range(0,15):
    # 1 柱状图
    dateOne = np.zeros([2])
    dateOne[0] = i;
    dateOne[1] = i;
    priceOne = np.zeros([2])
    priceOne[0] = beginPrice[i]
    priceOne[1] = endPrice[i]
    if endPrice[i]>beginPrice[i]:
        plt.plot(dateOne,priceOne,'r',lw=8)
    else:
        plt.plot(dateOne,priceOne,'g',lw=8)
plt.show()