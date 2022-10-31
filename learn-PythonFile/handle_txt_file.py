#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 该程序用于读取txt文件并对其进行操作以及输出、绘图

import os
import pandas as pd
import matplotlib.pyplot as plt

os.getcwd()
data = pd.read_csv('F:\\Python_IDLE\\working\\1phi16_1st_and_2nd.txt', sep='\s+', header=0, encoding='utf-8')

rele_time = data['time[s]']
A02_acc = data['AI1-02[g]']
# A03_acc = data['AI1-03[g]']
A06_acc_E = data['AI1-06[g]']
plt.plot(rele_time, A06_acc_E*9.81, label='A06-Electric Accelerate')
plt.plot(rele_time, A02_acc*9.81, label='A02-IEPE Accelerate')
# plt.plot(rele_time, A03_acc, label='A03-IEPE Accelerate')

plt.xlabel('time (s)')
plt.ylabel('accelerate (m/s²)')


'''

data_select = data[(data['time[s]']< 557.5) & (data['time[s]']> 556)]

rele_time_select = data_select['time[s]']
A01_acc_select = data_select['AI1-02[m/s²]']
plt.plot(rele_time_select, A01_acc_select)
data_select.to_csv('G:\\Python_IDLE\\working\\3phi16_1st_out.txt', sep='\t', float_format='%.3f', header=1, index=0)
print(data_select.head())
'''
plt.legend(loc='upper right')
plt.show()
