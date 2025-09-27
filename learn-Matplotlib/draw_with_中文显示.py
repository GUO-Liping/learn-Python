import numpy as np
import matplotlib.pyplot as plt

import matplotlib 
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

plt.plot(x, y,'-o',linewidth=2)   # 画线
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.title('最简单的xy绘图')
plt.show()