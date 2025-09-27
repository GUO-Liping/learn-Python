import numpy as np
import matplotlib.pyplot as plt

import matplotlib 
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([2, 3, 5, 7, 11])
x_error = 0.1*x_values
y_error = 0.1*y_values

fig, ax = plt.subplots()
ax.errorbar(x_values, y_values, xerr = x_error, fmt='o-', color='blue',ecolor='red', capsize=5, mfc='white', mec='blue', label='Data Set 1')
#ax.errorbar(x_values, y_values, yerr = y_error, fmt='^-', color='green',ecolor='purple', capsize=5, marker='D', mfc='white', mec='green', label='Data Set 2')
ax.fill_betweenx(y_values, x_values-x_error, x_values+x_error)

ax.errorbar(x_values+2, y_values, yerr = y_error, fmt='o-', color='blue',ecolor='red', capsize=5, mfc='white', mec='blue', label='Data Set 1')
ax.fill_between(x_values+2, y_values-y_error, y_values+y_error)


ax.errorbar(x_values+4, y_values, xerr = x_error, yerr = y_error, fmt='o-', color='blue',ecolor='red', capsize=5, mfc='white', mec='blue', label='Data Set 1')
ax.fill_between(x_values+4, y_values-y_error, y_values+y_error)

plt.plot(x_values, y_values,'-o',linewidth=2)   # 画线
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.title('xy绘图+x误差棒+y误差棒')
plt.show()