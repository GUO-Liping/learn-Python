#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from numpy import empty_like, mean, array, pi
from os import system
# 将numpy数组中对大于平均值的值求余弦，对小于平均值的数求正弦，最后返回

def func_compute(para_d):
	mean_value = mean(para_d)
	para_d_after = empty_like(para_d)
	for i in range(len(para_d)):
		if para_d[i] > mean_value:
			para_d_after[i] = para_d[i]
		elif para_d[i] < mean_value:
			para_d_after[i] = para_d[i]
		else:
			para_d_after[i] = para_d[i]
	return para_d_after


if __name__ == '__main__':
	test_array = array([-pi/4, 0, pi/4])
	test_array_after = func_compute(test_array)
	print('test_array = ', test_array)
	print('test_array_after = ', test_array_after)
	system("pause")  # 不要执行完立即关闭窗口
