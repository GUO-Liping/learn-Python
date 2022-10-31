#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 该程序用于pandas读取excel数据并进行合并操作
# It takes 318.116 second, 远大于pandas读取txt文件的时长

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

time_start = time.time()
input_xlsx_path = 'G:\\Python_IDLE\\working\\20191211_braker_760t_3phi16_225dm.xlsx'

data_sheet1 = pd.read_excel(input_xlsx_path, header=0, sheet_name='Sheet1', skiprows=[1])
data_sheet2 = pd.read_excel(input_xlsx_path, header=None, sheet_name='Sheet2', names=data_sheet1.columns)
data_sheet3 = pd.read_excel(input_xlsx_path, header=None, sheet_name='Sheet3', names=data_sheet1.columns)
data_sheet4 = pd.read_excel(input_xlsx_path, header=None, sheet_name='Sheet4', names=data_sheet1.columns)

data_sheet1234 = data_sheet1.append([data_sheet2, data_sheet3, data_sheet4], ignore_index=True)

out_txt_path = 'G:\\Python_IDLE\\working\\20191211_braker_3phi16_3rd_760t_225dm.txt'
data_sheet1234.to_csv(out_txt_path, sep='\t', index=False, header=True)

time_end = time.time()
print('The type of the data is',type(data_sheet1))
print(data_sheet1234.head(n=5))
print('It takes', '%.3f'%(time_end - time_start), 'second')
