#!/usr/bin/env python
# -*- coding: UTF-8 -*-

with open('G:\\Python_IDLE\\working\\TXTFile\\inputFile.txt', 'r') as inputFile:  # 打开待读取.txt文件
	data = inputFile.readlines()  # 按行读入原始数据

	for line in data:  # 按原始数据的行数进行循环
		test = line.split('\t', -1)  # 对每一行data中的元素按占位符'\t'进行分割
		print(test)
		with open('G:\\Python_IDLE\\working\\TXTFile\\outputFile.txt', 'a') as outputFile:  # 打开待写入.txt文件
			for row in range(len(test)):
				if len(test[row]) <= 10:
					outputFile.write(' '*(10-(len(test[row]))) + test[row])
				else:
					raise ValueError('原始数据中存在位数大于10的数字，请核实后再进行操作!!!')
			outputFile.close()
	inputFile.close()
