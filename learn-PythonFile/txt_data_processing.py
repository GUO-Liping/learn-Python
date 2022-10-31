#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 该程序用于读取txt文件并对其进行操作以及输出、绘图
# Author: Liping0_0
# Date: 20221031

import pandas as pd
import matplotlib.pyplot as plt

# 导入txt格式的数据
data = pd.read_csv('AI1-02.txt', sep=',', skiprows=[0,1,3,4], header=0, encoding='utf-8', on_bad_lines='skip')  # header为指定作为列名的行（先跳过skiprows）
print(data.shape)
print(data.head(n=50))

x_data = data.iloc[:,0]  # 提取第1列的数据
y_data = data.iloc[:,1]  # 提取第2列的数据

# 绘图-matplotlib
plt.plot(x_data, y_data)
plt.xlabel(data.columns[0])  # data.columns[0]表示列名称，panda库中可根据列名称索引列数据
plt.ylabel(data.columns[1])  # data.columns[1]表示列名称，panda库中可根据列名称索引列数据
plt.show()

# 导出选定的行部分到excel
start_row = int(6244*1000)
end_row = int(6245*1000)
output_data=data.iloc[start_row:end_row]
output_data.to_excel('excel_data.xlsx', header=True, index=False)
