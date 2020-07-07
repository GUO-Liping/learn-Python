#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
tutorial_05.py与tutorial_01.py类似
purpose: 爬取一张图片，并存入本地目录
'''

import requests
import os

url = "http://img.co188.com/ivp/images/product/367/427/266/48684328.jpg"
root = "F:\\GitHub\\learn-Python\\learn-Requests\\"
path = root + url.split('/')[-1]

try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print('文件保存成功')
	else:
		print('文件已存在')
except:
	print('爬取失败')

